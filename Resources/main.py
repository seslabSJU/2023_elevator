import logging
import datetime
import time
import threading
import queue

import Make_Dirs
import Pic_and_Show
import cv2_Detection
#import GetPressure
import Raspi_Shoot
import Video_To_Image

from config import Config_Detection, Config_Log, Config_DefaultPath, Config_Test
#from GetPressure import Get_Pressure

Raspi_Number = "No4"    # Raspi_Number should be like "No#"
stop_pressure = False
result_queue = queue.Queue()

def Capture_Video():
    cnt_max = 1
    time_per_cnt = 20 * Raspi_Shoot.second
    
    Video_File_Path, start_timestamp = Raspi_Shoot.shoot(Raspi_Number, cnt_max, time_per_cnt)
    result_queue.put((Video_File_Path, start_timestamp))
    
    global stop_pressure
    stop_pressure = True
    
    return Video_File_Path, start_timestamp
    
# def Capture_Sensor():
#     global stop_pressure
#
#     while not stop_pressure:
#         Get_Pressure()
#         time.sleep(1)
def Test_Linux(Raspi_Number):
    total_time = 0

    Make_Dirs.make_dir_and_files_Linux(Raspi_Number)
    #Pic_and_Show.get_sample_and_label()

    start = time.time()
    capture_video_thread = threading.Thread(target=Capture_Video)
    capture_video_thread.start()
    capture_video_thread.join()

    Video_File_Path, start_timestamp = result_queue.get()
    end = time.time()
    print("Interval Capturing Video : {} second".format(end - start))
    total_time += end - start

    start = time.time()
    picture_folder_name = start_timestamp.strftime("%Y%m%d_%H%M%S")
    picture_location = fr"{Config_DefaultPath.picture_default_path}\{Raspi_Number}\{picture_folder_name}"
    Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp, second=-1)
    end = time.time()
    print("Interval Extract Frames : {} second".format(end - start))
    total_time += end - start

    start = time.time()
    Config_Detection.Detection_path['image_folder_path'] = picture_location
    cv2_Detection.Run()
    end = time.time()
    print("Interval Button Detection : {}".format(end - start))
    total_time += end - start

    print("Total Time Spent is : {} second".format(total_time))

def Test_Windows(Raspi_Number):
    total_time = 0 

    video_list = Make_Dirs.video_list_from_folder(Config_Test.Video_sample_folder_path_Windows)
    if len(video_list) >= 1:
        for video_path in video_list:
            Raspi_Number, start_timestamp = Make_Dirs.get_Raspi_Number(video_path)
            start_timestamp = datetime.datetime.strptime(start_timestamp, '%Y%m%d%H%M%S')
            timestamp_str = start_timestamp.strftime("%Y%m%d_%H%M%S")

            Make_Dirs.make_dir_and_files_Windows(Raspi_Number)
            print("Skip Taking Videos due to Videos Already Found")

            start = time.time()
            picture_location = fr"{Config_DefaultPath.picture_default_path}\{Raspi_Number}\{timestamp_str}"
            Video_To_Image.extract_frames(video_path, picture_location, start_timestamp, second=30*60*10)
            end = time.time()
            print("Interval Extract Frames : {} second".format(end - start))
            total_time += end - start

            start = time.time()
            Config_Detection.Detection_path['image_folder_path'] = picture_location
            cv2_Detection.Run()
            end = time.time()
            print("Interval Button Detection : {}".format(end - start))
            total_time += end - start

            print("Total Time Spent is : {} second".format(total_time))

    else:
        Make_Dirs.make_dir_and_files_Windows(Raspi_Number)
        #Pic_and_Show.get_sample_and_label()

        start = time.time()
        capture_video_thread = threading.Thread(target=Capture_Video)
        capture_video_thread.start()
        capture_video_thread.join()

        Video_File_Path, start_timestamp = result_queue.get()
        end = time.time()
        print("Interval Capturing Video : {} second".format(end - start))
        total_time += end - start

        start = time.time()
        picture_folder_name = start_timestamp.strftime("%Y%m%d_%H%M%S")
        picture_location = fr"{Config_DefaultPath.picture_default_path}\{Raspi_Number}\{picture_folder_name}"
        Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp, second=-1)
        end = time.time()
        print("Interval Extract Frames : {} second".format(end - start))
        total_time += end - start

        start = time.time()
        Config_Detection.Detection_path['image_folder_path'] = picture_location
        cv2_Detection.Run()
        end = time.time()
        print("Interval Button Detection : {}".format(end - start))
        total_time += end-start

        print("Total Time Spent is : {} second".format(total_time))
    return 0

def Real():
    total_time = 0 
        
    Make_Dirs.make_dirs_for_program()
    Make_Dirs.make_files_for_program()
    
    Video_File_Path, start_timestamp = Capture_Video()

    picture_folder_name = start_timestamp.strftime("%Y%m%d_%H%M%S")
    picture_location = f"{Config_DefaultPath.picture_default_path}/{picture_folder_name}"

    start = time.time()
    Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp, second=-1)
    #Video_To_Image.extract_frames(test_video_location, picture_location, datetime.datetime.now(), PROP=3000000)
    end = time.time()
    print("Interval Extract Frames : {} second".format(end-start))
    total_time += end-start
    
    start = time.time()
    Video_To_Image.Rotate_Frames(picture_location)
    end = time.time()
    print("Interval Rotate Frames : {} second".format(end-start))
    total_time += end-start

    start = time.time()
    #picture_location = '/home/user/Videos/Pictures/20230904_183111'
    Config_Detection.Detection_path['image_folder_path'] = picture_location
    cv2_Detection.Run()

    end = time.time()
    print("Interval Button Detection : {}".format(end - start))
    total_time += end-start
    
    print("Total Time Spent is : {} second".format(total_time))

if __name__ == '__main__':
    Test_Windows(Raspi_Number)

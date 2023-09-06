import os
import sys
import logging, traceback
import datetime
import time
import threading
import queue

import Make_Dirs
import cv2_Detection
import GetPressure
import Raspi_Shoot
import Video_To_Image

from config import Config_Detection, Config_Log, Config_DefaultPath
from GetPressure import Get_Pressure

#test_video_location = f'/home/user/Videos/vid/No1_2023-06-30-14:50.h264'
#video_name = f'No1_2023-06-30-14:50.h264'

stop_pressure = False
result_queue = queue.Queue()
logging.basicConfig(filename='/home/user/Desktop/service_log.log', level=logging.ERROR)

def Capture_Video():
    cnt_max = 1
    time_per_cnt = 10 * Raspi_Shoot.second
    
    Video_File_Path, start_timestamp = Raspi_Shoot.shoot(cnt_max, time_per_cnt)
    result_queue.put((Video_File_Path, start_timestamp))
    
    global stop_pressure
    stop_pressure = True
    
    return Video_File_Path, start_timestamp
    
def Capture_Sensor():
    global stop_pressure
    
    while not stop_pressure:
        Get_Pressure()
        time.sleep(1)

def Test():
    total_time = 0 
    
    Make_Dirs.make_dirs_for_program()
    Make_Dirs.make_files_for_program()
    
    start = time.time()
    #Get_Pressure()
    capture_video_thread = threading.Thread(target=Capture_Video)
    capture_video_thread.start()
    capture_video_thread.join()
    Video_File_Path, start_timestamp = result_queue.get()
    #Video_File_Path, start_timestamp = "/home/user/Videos/No1_2023-06-30-14:50.h264", datetime.datetime.now().replace(microsecond=0)
    end = time.time()
    print("Interval Capturing Video : {} second".format(end-start))
    total_time += end-start
    
    start = time.time()
    picture_folder_name = start_timestamp.strftime("%Y%m%d_%H%M%S")
    picture_location = f"{Config_DefaultPath.picture_default_path}/{picture_folder_name}"
    Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp, second=30*60*30)
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
    Config_Detection.Detection_path['image_folder_path'] = picture_location
    cv2_Detection.Run()
    end = time.time()
    print("Interval Button Detection : {}".format(end - start))
    total_time += end-start
    
    print("Total Time Spent is : {} second".format(total_time))

def Test2():
    total_time = 0 
    
    Make_Dirs.make_dirs_for_program()
    Make_Dirs.make_files_for_program()
    
    start = time.time()
    '''
    capture_video_thread = threading.Thread(target=Capture_Video)
    capture_pressure_thread = threading.Thread(target=Capture_Sensor)
    
    capture_video_thread.start()
    capture_pressure_thread.start()

    # Wait for both threads to finish (you can set a termination condition)
    capture_video_thread.join()
    capture_pressure_thread.join()
    
    Video_File_Path, start_timestamp = result_queue.get()
    '''
    Get_Pressure()
    Video_File_Path, start_timestamp = "/home/user/Videos/No1_2023-06-30-14:50.h264", datetime.datetime.now().replace(microsecond=0)
    end = time.time()
    print("Interval Capturing Video : {} second".format(end-start))
    total_time += end-start
    
    start = time.time()
    picture_folder_name = start_timestamp.strftime("%Y%m%d_%H%M%S")
    picture_location = f"{Config_DefaultPath.picture_default_path}/{picture_folder_name}"
    Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp, second=30*60*30)
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
    Config_Detection.Detection_path['image_folder_path'] = picture_location
    cv2_Detection.Run()
    end = time.time()
    print("Interval Button Detection : {}".format(end - start))
    total_time += end-start
    
    print("Total Time Spent is : {} second".format(total_time))

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


def Runner():
    Test()
    #Real()
    #Test2()

if __name__ == '__main__':
    Runner()

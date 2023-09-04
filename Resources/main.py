import os, sys
import datetime
import time
import multiprocessing

import cv2_Detection
import GetPressure
import Raspi_Shoot
import Video_To_Image

from config import Config_Detection, Config_Log

#test_video_location = f'/home/user/Videos/vid/No1_2023-06-30-14:50.h264'
#video_name = f'No1_2023-06-30-14:50.h264'
    
def Capture_Video(result_queue):
    cnt_max = 1
    time_per_cnt = 3 * Raspi_Shoot.second
    
    Raspi_Shoot.shoot(cnt_max, time_per_cnt, result_queue)
    
def Capture_Sensor(terminate_event):
    GetPressure.Get_Pressure(terminate_event)

def Runner():
    total_time = 0
    
    start = time.time()
    result_queue = multiprocessing.Queue()
    terminate_event = multiprocessing.Event()
    
    thread_cap_video = multiprocessing.Process(target=Capture_Video, args=(result_queue, ))
    thread_cap_sensor = multiprocessing.Process(target=Capture_Sensor, args=(terminate_event, ))

    thread_cap_video.start()
    thread_cap_sensor.start()
    
    thread_cap_video.join()
    
    terminate_event.set()
    thread_cap_sensor.join()
    
    end = time.time()
    print("Interval Recording : {} second".format(end-start))
    total_time += end-start

    Video_File_Path, start_timestamp = result_queue.get()

    picture_folder_name = start_timestamp.strftime("%Y%m%d_%H%M%S")
    picture_location = Config_Log.image_folder_path + picture_folder_name

    start = time.time()
    Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp)
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
    
    Config_Log.log_file_path = Config_Log.log_default_path + f"{picture_folder_name}"
    Config_Log.timelist_log_file_path = Config_Log.log_default_path + f"{picture_folder_name}"
    
    cv2_Detection.Run()
    end = time.time()
    print("Interval Button Detection : {}".format(end - start))
    total_time += end-start
    
    print("Total Time Spent is : {} second".format(total_time))
    

if __name__ == '__main__':
    Runner()

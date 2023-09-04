import datetime
import os, sys
import time
import cv2_Detection
import Raspi_Shoot
import Video_To_Image

from config import Config_Detection

test_video_location = f'/home/user/Videos/vid/No1_2023-06-30-14:50.h264'
video_name = f'No1_2023-06-30-14:50.h264'
picture_location = f'/home/user/Videos/Pictures/' + video_name

def Runner():
    total_time = 0
    cnt_max = 3
    time_per_cnt = 30 * Raspi_Shoot.minute
    try:
        #   Video_File_Path, start_timestamp = Raspi_Shoot.shoot(cnt_max, time_per_cnt)
        pass
    except:
        pass

    start = time.time()
    #Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp)
    #Video_To_Image.extract_frames(test_video_location, picture_location, datetime.datetime.now(), PROP=3000000)
    end = time.time()
    print("Interval Extract Frames : {} second".format(end-start))
    total_time += end-start
    
    start = time.time()
    #Video_To_Image.extract_frames(Video_File_Path, picture_location, start_timestamp)
    #Video_To_Image.Rotate_Frames(picture_location)
    end = time.time()
    print("Interval Extract Frames : {} second".format(end-start))
    total_time += end-start

    start = time.time()
    Config_Detection.Detection_path['image_folder_path'] = picture_location
    cv2_Detection.Run()
    end = time.time()
    print("Interval Button Detection : {}".format(end - start))
    total_time += end-start
    
    print("Total Time Spent is : {} second".format(total_time))
    

if __name__ == '__main__':
    Runner()

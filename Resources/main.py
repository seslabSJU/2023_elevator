import datetime
import os, sys
import time
import cv2_Detection
import Raspi_Shoot
import Video_To_Image

test_video_location = f'/home/user/Videos/vid/No1_2023-06-30-14:50.h264'
picture_location = f'/home/user/Videos/Pictures'
def Runner():
    cnt_max = 3
    time_per_cnt = 30 * Raspi_Shoot.minute
    try:
        #   Video_File_Path, start_timestamp = Raspi_Shoot.shoot(cnt_max, time_per_cnt)
        pass
    except:
        pass

    start = time.time()
    Video_To_Image.extract_frames(test_video_location, picture_location, datetime.datetime.now())
    end = time.time()

if __name__ == '__main__':
    Runner()
import os
import datetime
import subprocess
import multiprocessing
from threading import Thread
from config import Config_VideoCapture, Config_DefaultPath

second = 1000
minute = 60 * second
hour = 60 * minute
day = 24 * hour
timestamp = datetime.datetime.now().replace(microsecond=0)

def create_folder(Raspi_Number):
    if Config_DefaultPath.video_capture_default_path is None:
        print("In Raspi Shoot, Config_DefaultPath.video_capture_default_path is None")
        exit(0)
                
    dir_name = fr"{Raspi_Number}/{timestamp.strftime('%Y%m%d%H%M%S')}"

    os.chdir(Config_DefaultPath.video_capture_default_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    os.chdir(dir_name)
    video_capture_dir_path = os.getcwd()
    
    dir_name = "Result"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    os.chdir(dir_name)
    video_capture_result_dir_path = os.getcwd()
    
    Config_VideoCapture.video_capture_dir_path = video_capture_dir_path
    Config_VideoCapture.video_capture_result_dir_path = video_capture_result_dir_path

def create_log(log_file_name, message):
    os.chdir(Config_VideoCapture.video_capture_result_dir_path)
    timestamp_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    log_message = f"[Time :{timestamp_str}] -> {message}"
    txt_name = f"{log_file_name}.txt"

    with open(txt_name, "a") as log_file:
        log_file.write(log_message + "\n")


def run_Windows(Raspi_Number, shoot_time, log_file_name):
    vid_command = "libcamera-vid"
    vid_width = " --width 1080"
    vid_height = " --height 1920"
    vid_time = f" --framerate 30 -t {shoot_time} -o "
    timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")
    
    vid_output = fr"{Config_VideoCapture.video_capture_dir_path}\{Raspi_Number}\{Raspi_Number}_{timestamp_str}.h264"
    command = vid_command + vid_width + vid_height + vid_time + vid_output

    message = "Video Start"
    create_log(log_file_name, message)

    thr = Thread(target=run_commad, args=(command,))

    thr.start()
    thr.join()

    message = "Video End"
    create_log(log_file_name, message)

    return vid_output, timestamp
    
def run_Linux(Raspi_Number, shoot_time, log_file_name):
    vid_command = "libcamera-vid"
    vid_width = " --width 1080"
    vid_height = " --height 1920"
    vid_time = f" --framerate 15 -t {shoot_time} -o "
    timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")
    
    vid_output = fr"{Config_VideoCapture.video_capture_dir_path}/{Raspi_Number}_{timestamp_str}.h264"
    command = vid_command + vid_width + vid_height + vid_time + vid_output

    message = "Video Start"
    create_log(log_file_name, message)

    thr = Thread(target=run_commad, args=(command,))

    thr.start()
    thr.join()

    message = "Video End"
    create_log(log_file_name, message)

    return vid_output, timestamp

def run_commad(command):
    print(command)
    os.system(command)

def shoot(Raspi_Number, cnt_max, time_per_cnt):
    create_folder(Raspi_Number)
    cnt = 0
    video_file_path = None
    start_timestamp = None

    while cnt != cnt_max:
        log_file_name = f"{Raspi_Number}_{timestamp.strftime('%Y%m%d%H%M')}"

        video_file_path, start_timestamp = run_Linux(Raspi_Number, time_per_cnt, log_file_name)
        #video_file_path, start_timestamp = run_Windows(Raspi_Number, time_per_cnt, log_file_name)
        cnt = cnt + 1

    if (video_file_path is None) or (start_timestamp is None):
        print("Error in Raspi Shoot, Video_File_Path is None or start_timestamp is None")
        exit(1)
    else:
        return video_file_path, start_timestamp

def take_one_picture(picture_path):
    command = f"libcamera-jpeg --width 1080 --height 1920 -o {picture_path}"
    os.system(command)
    
    return picture_path

if __name__ == '__main__':
    cnt_max = 1
    time_per_cnt = 5 * second
    shoot(cnt_max, time_per_cnt)


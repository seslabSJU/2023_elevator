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

def create_folder():
    #now = datetime.datetime.now()

    if Config_DefaultPath.video_capture_default_path is None:
        print("In Raspi Shoot, Config_DefaultPath.video_capture_default_path is None")
        exit(0)
                
    dir_name = timestamp.strftime("%Y%m%d%H%M%S")

    os.chdir(Config_DefaultPath.video_capture_default_path)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    os.chdir(dir_name)
    video_caputure_dir_path = os.getcwd()
    
    dir_name = "Result"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        
    os.chdir(dir_name)
    video_capture_result_dir_path = os.getcwd()
    
    #print(video_caputure_dir_path)
    #print(video_capture_result_dir_path)
    Config_VideoCapture.video_capture_dir_path = video_caputure_dir_path
    Config_VideoCapture.video_capture_result_dir_path = video_capture_result_dir_path

def create_log(log_file_name, message):
    os.chdir(Config_VideoCapture.video_capture_result_dir_path)
    timestamp_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    log_message = f"[Time :{timestamp_str}] -> {message}"
    txt_name = f"{log_file_name}.txt"

    with open(txt_name, "a") as log_file:
        log_file.write(log_message + "\n")


def run(shoot_time, log_file_name):
    vid_command = "libcamera-vid"
    vid_width = " --width 1920"
    vid_height = " --height 1080"
    vid_time = f" -t {shoot_time} -o "
    timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")
    
    vid_output = f"{Config_VideoCapture.video_capture_dir_path}" + f"/No_{timestamp_str}.h264"
    # stream_output = " --save-pts " + folder_name + f"/Result/timestamps.txt"
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
    #print(command)
    os.system(command)

def shoot(cnt_max, time_per_cnt):
    create_folder()
    cnt = 0
    video_file_path = None
    start_timestamp = None

    while cnt != cnt_max:
        log_file_name = f"No1_{timestamp.strftime('%Y%m%d%H%M')}"

        video_file_path, start_timestamp = run(time_per_cnt, log_file_name)
        cnt = cnt + 1

    if (video_file_path is None) or (start_timestamp is None):
        print("Error in Raspi Shoot, Video_File_Path is None or start_timestamp is None")
        exit(1)
    else:
        return video_file_path, start_timestamp

def take_one_picture(picture_path):
    command = f"libcamera-jpeg --width 1920 --height 1080 -o {picture_path}"
    os.system(command)
    
    return picture_path

if __name__ == '__main__':
    cnt_max = 1
    time_per_cnt = 5 * second
    shoot(cnt_max, time_per_cnt)


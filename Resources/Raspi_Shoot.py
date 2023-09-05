import os
import datetime
import logging
import traceback
import subprocess
import multiprocessing
from threading import Thread
from config import Config_VideoCapture, Config_DefaultPath

second = 1000
minute = 60 * second
hour = 60 * minute
day = 24 * hour
timestamp = datetime.datetime.now().replace(microsecond=0)

logging.basicConfig(filename='./test.log', level=logging.INFO)


def create_folder():
    #now = datetime.datetime.now()

    if Config_DefaultPath.video_capture_deafult_path is None:
        print("In Raspi Shoot, Config_DefaultPath.video_capture_deafult_path is None")
        exit(0)
                
    dir_name = timestamp.strftime("%Y%m%d%H%M")

    os.chdir(Config_DefaultPath.video_capture_deafult_path)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    os.chdir(dir_name)
    video_caputure_dir_path = os.getcwd()
    
    dir_name = "Result"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        
    os.chdir(dir_name)
    video_caputure_result_dir_path = os.getcwd()
    
    print(video_caputure_dir_path)
    print(video_caputure_result_dir_path)
    Config_VideoCapture.video_caputure_dir_path = video_caputure_dir_path
    Config_VideoCapture.video_caputure_result_dir_path = video_caputure_result_dir_path

def create_log(log_file_name, message):
    try:
        os.chdir(Config_VideoCapture.video_caputure_result_dir_path)
        timestamp = now.strftime("%Y%m%d%H%M%S")
        log_message = f"[Time :{timestamp}] -> {message}"

        log_file_name = f"{log_file_name}.txt"

        with open(log_file_name, "a") as log_file:
            log_file.write(log_message + "\n")
    except:
        logging.error(traceback.format_exc())


def run(shoot_time, log_file_name):
    try:
        
        vid_command = "libcamera-vid"
        vid_width = " --width 1920"
        vid_height = " --height 1080"
        vid_time = f" -t {shoot_time} -o "

        vid_output = f"{Config_VideoCapture.video_caputure_dir_path}" + f"/No_{timestamp}.h264"
        # stream_output = " --save-pts " + folder_name + f"/Result/timestamps.txt"
        command = vid_command + vid_width + vid_height + vid_time + vid_output

        message = "Video Start"
        create_log(log_file_name, folder_name, message)

        start_timestamp = now

        thr = Thread(target=run_commad, args=(command,))

        thr.start()
        thr.join()

        message = "Video End"
        create_log(log_file_name, message)

        return vid_output, start_timestamp
    except:
        logging.error(traceback.format_exc())


def run_commad(command):
    print(command)
    os.system(command)

def shoot(cnt_max, time_per_cnt):
    create_folder()
    cnt = 0
    while cnt != cnt_max:
        log_file_name = "No3_"

        Video_File_Path, start_timestamp = run(time_per_cnt, log_file_name)
        cnt = cnt + 1
    
    return Video_File_Path, start_timestamp


if __name__ == '__main__':
    cnt_max = 1
    time_per_cnt = 5 * second
    try:
        shoot(cnt_max, time_per_cnt)
    except:
        logging.error(traceback.format_exc())


import os
import datetime
import logging
import traceback
import subprocess
from threading import Thread

default_path = f'/home/user/Videos/libcamera_vid/'
second = 1000
minute = 60 * second
hour = 60 * minute
day = 24 * hour
logging.basicConfig(filename='./test.log', level=logging.INFO)


def create_folder():
    now = datetime.datetime.now()

    folder_name = now.strftime("%Y%m%d%H%M")
    folder_path = default_path + folder_name
    result_folder_path = folder_path + "/Result"

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        os.mkdir(result_folder_path)

    return folder_name


def create_log(log_file_name, folder_name, message):
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        log_message = f"[Time :{timestamp}] -> {message}"

        path = "/home/user/Videos/libcamera_vid/" + folder_name + f"/Result/{log_file_name}.txt"

        with open(path, "a") as log_file:
            log_file.write(log_message + "\n")
    except:
        logging.error(traceback.format_exc())


def run(folder_name, shoot_time, log_file_name):
    try:
        vid_command = "libcamera-vid"
        vid_width = " --width 1920"
        vid_height = " --height 1080"
        vid_time = f" -t {shoot_time}"

        now = datetime.datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")

        vid_output = f" -o /home/user/Videos/libcamera_vid/" + folder_name + f"/Result/No1_{time}.h264"
        # stream_output = " --save-pts " + folder_name + f"/Result/timestamps.txt"
        command = vid_command + vid_width + vid_height + vid_time + vid_output

        message = "Video Start"
        create_log(log_file_name, folder_name, message)

        # os.system(command)
        thr = Thread(target=run_commad, args=(command,))

        thr.start()
        thr.join()

        message = "Video End"
        create_log(log_file_name, folder_name, message)

        return 0
    except:
        logging.error(traceback.format_exc())


def run_commad(command):
    print(command)
    os.system(command)

def shoot(cnt_max):
    folder_name = create_folder()
    cnt = 0
    while cnt != cnt_max:
        # shoot_time = 1 * minute
        shoot_time = 10 * second
        log_file_name = "No1_Vid1"

        run(folder_name, shoot_time, log_file_name)
        cnt = cnt + 1

    return 0


if __name__ == '__main__':
    cnt_max = 3
    try:
        shoot(cnt_max)
    except:
        logging.error(traceback.format_exc())


import os
import datetime

second = 1000
minute = 60 * second

def create_log(log_file_name, message):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    log_message = f"[Time :{timestamp}] -> {message}"

    with open(f"Result/{log_file_name}.txt", "a") as log_file:
        log_file.write(log_message + "\n")

def run(shoot_time):
    vid_command = "libcamera-vid"
    vid_width = " --width 1920"
    vid_height = " --height 1080"
    vid_time = f" -t {shoot_time}"

    now = datetime.datetime.now()

    time = now.strftime("%Y%m%d%H%M%S")
    log_file_name = time

    vid_output = f" -o Result/No1_{time}.h264"

    command = vid_command + vid_width + vid_height + vid_time + vid_output

    message = "Video Start"
    create_log(log_file_name, message)

    os.system(command)

    message = "Video End"
    create_log(log_file_name, message)

def shoot(cnt_max):
    cnt = 0
    while cnt != cnt_max:
        shoot_time = 1 * second
        run(shoot_time)
        cnt = cnt + 1

cnt_max = 10
shoot(cnt_max)
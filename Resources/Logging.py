import os

try:
    from config import Config_Log
    config_LOG = Config_Log

except Exception as e:
    pass
def log_green_button(config, previous_green_button_list, now_green_button_list):
    basename = os.path.basename(config.Detection_path['image_file_path'])
    frame_str = basename.replace("frame_", "").replace(".jpg", "")
    frame_number = int(frame_str)

    if not previous_green_button_list == now_green_button_list:
        log = "Condition Changed at {}\nPrevious Condition was : {}\nLatest Condition is : {}\n\n".format(basename, previous_green_button_list, now_green_button_list)

        with open(config_LOG.log_file_path, "a") as f:
            f.write(log)
        return frame_number

    else:
        return None

def log_interval(interval):
    log = "Interval Between Previous Conditional Change is : {}s\n\n".format(interval)
    with open(config_LOG.timelist_log_file_path, "a") as f:
        f.write(log)
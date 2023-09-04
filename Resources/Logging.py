import os

try:
    from config import Config_Log
    config_LOG = Config_Log

except Exception as e:
    pass
def log_green_button(config, previous_green_button_list, now_green_button_list):
    basename = os.path.basename(config.Detection_path['image_file_path'])
    
    if not os.path.exists(config_LOG.log_file_path):
        os.mkdir(config_LOG.log_file_path)

    if not previous_green_button_list == now_green_button_list:
        log = "Condition Changed at {}\nPrevious Condition was : {}\nLatest Condition is : {}\n\n".format(basename, previous_green_button_list, now_green_button_list)

        with open("Log_Conditions.txt", "a") as f:
            f.write(log)
        return now_green_button_list

    else:
        return None

def log_interval(interval):
    if not os.path.exists(Config_Log.timelist_log_file_path):
        os.makedirs(Config_Log.timelist_log_file_path)
        
    log = "Interval Between Previous Conditional Change is : {}s\n\n".format(interval)
    with open("Log_Floor_Lists.txt", "a") as f:
        f.write(log)
        
def log_timelist(Text):
    if not os.path.exists(Config_Log.timelist_log_file_path):
        os.mkdir(Config_Log.timelist_log_file_path)
        
    with open("Log_Floor_Lists.txt", "a") as f:
        f.write(Text)
    
def log_sensor(Text):
    if not os.path.exists(Config_Log.sensor_log_file_path):
        os.mkdir(Config_Log.sensor_log_file_path)
    
    print("ASD {}".format(Config_Log.sensor_log_file_path))
    with open("Sensors.txt", "a") as f:
        f.write(Text)

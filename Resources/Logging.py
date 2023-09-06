import os

try:
    from config import Config_DefaultPath

except Exception as e:
    pass
def log_green_button(config, previous_green_button_list, now_green_button_list):
    if Config_DefaultPath.log_default_path is None:
        print("Error in Logging, Log Default Path is None\n")
        exit(1)

    else:
        txt_name = "Log_Condition.txt"
        basename = os.path.basename(config.Detection_path['image_file_path'])

        os.chdir(Config_DefaultPath.log_default_path)
        if not previous_green_button_list == now_green_button_list:
            log = "Condition Changed at {}\nPrevious Condition was : {}\nLatest Condition is : {}\n\n".format(basename, previous_green_button_list, now_green_button_list)

            with open(txt_name, "a") as f:
                f.write(log)
            return now_green_button_list

        else:
            return None

def log_interval(interval):
    if Config_DefaultPath.log_default_path is None:
        print("Error in Logging, Log Default Path is None\n")
        exit(1)

    else:
        os.chdir(Config_DefaultPath.log_default_path)
        txt_name = "Log_Floor_Lists.txt"
        log = "Interval Between Previous Conditional Change is : {}s\n\n".format(interval)
        with open(txt_name, "a") as f:
            f.write(log)
        
def log_timelist(Text):
    if Config_DefaultPath.log_default_path is None:
        print("Error in Logging, Log Default Path is None\n")
        exit(1)
    else:
        os.chdir(Config_DefaultPath.log_default_path)
        txt_name = "Log_Floor_Lists.txt"
        with open("Log_Floor_Lists.txt", "a") as f:
            f.write(Text)
    
def log_sensor(Text):
    if Config_DefaultPath.log_default_path is None:
        print("Error in Logging, Log Default Path is None\n")
        exit(1)
    
    else:
        os.chdir(Config_DefaultPath.log_default_path)
        txt_name = "Log_Sensors.txt"
        with open(txt_name, "a") as f:
            f.write(Text)

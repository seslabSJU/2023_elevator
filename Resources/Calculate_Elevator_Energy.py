import os
import re
import config

try:
    from config import Config_Elevator_SW, Config_Elevator_HW, Config_Log
    config_EH = config.Config_Elevator_HW
    config_ES = config.Config_Elevator_SW

    usage_intensity = config_EH.Usage_Intensity
    default_location = config_ES.Default_Location

    floors = config_ES.Location_Weight.keys()

    Height_Per_Floor = config_EH.Height_Per_Floor
    First_floor_altitude = config_EH.First_Floor_Altitude
    current_floor_altitude = config_EH.Current_Floor_Altitude

    log_sensor = config.Config_Log.sensor_log_file_path

except Exception as e:
    pass
def Calculate_Current_Floor(log_sensor):
    with open(log_sensor, 'r') as f:
        text = f.read()

    altitude_pattern = r"Altimeter : (-?\d+\.\d+)m"
    temperature_pattern = r"Temperature : (\d+\.\d+) Degree Celsius"

    altitude_match = re.search(altitude_pattern, text)
    temperature_match = re.search(temperature_pattern, text)

    if altitude_match and temperature_match:
        altitude = float(altitude_match.group(1))
        temperature = float(temperature_match.group(1))

        current_floor_altitude = altitude - First_floor_altitude
        current_floor = current_floor_altitude / Height_Per_Floor

        return round(altitude,4), round(current_floor, 4)
    else:

        return None

def Calculate_Usage_Intesity_Category(Intensity, Usage_Intensity):
    for index, key in enumerate(Usage_Intensity):
        if Intensity - Usage_Intensity[key] < 0:
            return index+1
    return 6

def Calculate_Average_Travel_Distance(Usage_Intensity, Stopping_Floors):
    if Usage_Intensity<=0 or 7<=Usage_Intensity or Stopping_Floors<=1:
        print("Calculate_Average_Travel_Distance: Argument range Invalid")
        return 0
    else:
        if Stopping_Floors == 2:
            return 1.00
        elif Stopping_Floors == 3:
            return 0.67
        else:
            if Usage_Intensity <=3:
                return 0.49
            elif Usage_Intensity == 4:
                return 0.44
            elif Usage_Intensity == 5:
                return 0.39
            elif Usage_Intensity == 6:
                return 0.32

if __name__ == '__main__':
    #pass
    alt, flr = Calculate_Current_Floor(log_sensor)
    print("{} {}".format(alt, flr))
    # intensity = Calculate_Usage_Intesity_Category(2500, usage_intensity)
    # sav = Calculate_Average_Travel_Distance(intensity, 5)
    # print(sav)

    # for floor in floors:
    #     if default_location == floor:
    #         print(config_ES.Location_Weight[floor])
import re
import datetime
import Detect_Color
import Sort_image
import classid
import List_Button_On_Floor
import Calculate_Elevator_Energy
import Logging

try:
    from config import Config_Detection, Config_Elevator_SW, Config_Log, Config_DefaultPath
    config_DETECT = Config_Detection
    config_ELEVATOR_SW = Config_Elevator_SW

except Exception as e:
    pass

def make_list(timestamp_str, Root_List, delta):
    alt, flr = Calculate_Elevator_Energy.Calculate_Current_Floor()
    parsed_datetime = datetime.datetime.strptime(timestamp_str, '%Y%m%d_%H%M%S')

    #Text = "Current Altimeter : {}m, Floor is {}\n".format(alt, flr)
    if Root_List.head is None:
        node = Root_List.addNode(parsed_datetime)
        node.set_currentFloor(flr)
        node.set_pressedButton(delta)
        node.set_InOut(1)
        
    else:
        last = Root_List.last
        last.timestamp = parsed_datetime
        
        if parsed_datetime - last.timestamp >= datetime.timedelta(seconds=5):
            delta_not_last_pressed = [x for x in delta if x not in last.pressedButton]
            for floor in delta_not_last_pressed:
                last.add_pressedButton(floor)
        else:
            node = Root_List.addNode(parsed_datetime)
            node.set_currentFloor(flr)
            node.set_pressedButton(delta)
            node.set_InOut(1)

    Root_List.printAllNodes()
    Text = Root_List.printLastNodes()
    
    return Text

def check_differential(timestamp_str, previous, now, root_List):
    bigger = previous if len(previous) > len(now) else now
    smaller = now if bigger == previous else previous

    delta = [x for x in bigger if x not in smaller]

    #print("f is {}, prev is {}, now is {}".format(frame, previous, now))
    # print("bigger is {}, smaller is {}".format(bigger, smaller))
    Text = ""
    if len(previous) > len(now):
        if len(delta) == 1:
            Text += "Elevator Stops At {}th Floor".format(delta[0])
            
        elif len(delta) >= 2:
            Text += "Elevator Stops At {}th Floor or Camera Blocked by Something".format(delta[0])
        Text += make_list(timestamp_str, root_List, now)
    elif len(previous) < len(now):
        Text += "Somebody Pressed the button "
        Text += make_list(timestamp_str, root_List, delta)
    elif len(previous) == len(now) and previous != now:
        Text += "Button List has Changed "
        Text += make_list(timestamp_str, root_List, now)

    Logging.log_timelist(Text)

def Extract_datetime(img_path):
    if Config_DefaultPath.picture_default_path is None:
        print("Error in Calculate_Elevator_Energy, picture_default_path is None\n")
        exit(1)

    else:
        pattern = r'(\d{8}_\d{6})\.jpg'
        match = re.search(pattern, img_path)

        if match:
            desired_string = match.group(1)
            return desired_string
        else:
            return None

def Detect(img_path):
    class_list = classid.get_class_id_list(config_DETECT.Detection_path['yaml_path'])

    now_green_button_list = Detect_Color.detect_color(img_path, config_DETECT.Detection_path['label_txt_path'], class_list)
    return now_green_button_list

def Run():
    images = Sort_image.get_images(Config_DefaultPath.picture_default_path)

    root_list = List_Button_On_Floor.TimeList()
    previous_green_button_list = []

    previous_frame = -1
    count = 1

    for img_path in images:
        timestamp_str = Extract_datetime(img_path)
        
        print("Reading Button Log From image {}...".format(img_path))
        config_DETECT.Detection_path['image_file_path'] = img_path

        now_green_button_list = Detect(img_path)

        frame = Logging.log_green_button(config_DETECT, previous_green_button_list, now_green_button_list)

        if frame is not None:
            if previous_frame == -1:
                previous_frame = frame
            if previous_green_button_list != now_green_button_list:
                check_differential(timestamp_str, previous_green_button_list, now_green_button_list, root_list)
            else:
                interval = float((frame-previous_frame)/30)
                Logging.log_interval(interval)
                previous_frame = frame

        previous_green_button_list = now_green_button_list

if __name__ == '__main__':
    Run()
    # config = Config_Detection
    # class_list = classid_list.get_class_id_list(config.Detection_path['yaml_path'])
    # class_list = classid_list.append_class_id_list_with_flag(class_list)
    #
    # Detect_Color.detect_color(config.Detection_path['sample_file_path'], config.Detection_path['label_txt_path'], class_list)
    # pass

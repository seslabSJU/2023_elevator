import datetime
import Detect_Color
import Sort_image
import classid_list
import Elevator_TimeList
import Calculate_Elevator_Energy

try:
    from config import Config_Detection, Config_Elevator_SW, Config_Log
    config = Config_Detection
    config_ES = Config_Elevator_SW
    log_sensor = Config_Log.sensor_log_file_path
except Exception as e:
    pass

def check_differential(frame, previous, now, Root_List):
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
        Text += make_list(frame, Root_List, now)
    elif len(previous) < len(now):
        Text += "Somebody Pressed the button "
        Text += make_list(frame, Root_List, delta)
    elif len(previous) == len(now) and previous != now:
        Text += "Button List has Changed "
        Text += make_list(frame, Root_List, now)
    Elevator_TimeList.log_timelist(frame, Text)

def make_list(frame, Root_List, delta):
    alt, flr = Calculate_Elevator_Energy.Calculate_Current_Floor(log_sensor)
    #Text = "Current Altimeter : {}m, Floor is {}\n".format(alt, flr)
    if Root_List.head is None:
        node = Root_List.addNode()
        node.set_time(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        node.set_frame(frame)
        node.set_currentFloor(flr)
        node.set_pressedButton(delta)
        node.set_InOut(1)
    else:
        last = Root_List.last
        if frame - last.frame <= 30*5:
            ddelta = [x for x in delta if x not in last.pressedButton]
            for floor in ddelta:
                last.add_pressedButton(floor)
            last.set_frame(frame)
        else:
            node = Root_List.addNode()
            node.set_time(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
            node.set_frame(frame)
            node.set_currentFloor(flr)
            node.set_pressedButton(delta)
            node.set_InOut(1)

    Text = Root_List.printLastNodes()
    return Text

def Detect_and_Show():
    images = Sort_image.get_images(config.Detection_path['image_folder_path'])

    class_list = classid_list.get_class_id_list(config.Detection_path['yaml_path'])
    class_list = classid_list.append_class_id_list_with_flag(class_list)

    Root_List = Elevator_TimeList.TimeList()

    previous_green_button_list = []
    previous_frame = -1

    count = 1
    division = 10
    flag = 0

    for img_path in images:
        print("Reading Button Log From image {}...".format(img_path))
        config.Detection_path['image_file_path'] = img_path

        now_green_button_list = Detect_Color.detect_color(img_path, config.Detection_path['label_txt_path'], class_list)

        if count == 0:
            flag = 1
        else:
            flag = 0

        frame = classid_list.log_green_button(config, previous_green_button_list, now_green_button_list)

        if frame is not None:
            if previous_frame == -1:
                previous_frame = frame
            if previous_green_button_list != now_green_button_list:
                check_differential(frame, previous_green_button_list, now_green_button_list, Root_List)
            else:
                interval = float((frame-previous_frame)/30)
                classid_list.log_interval(interval)
                previous_frame = frame

            # Text = "Frame at {} : ".format(frame) + make_tree(Start_tree, now_green_button_list, flag) + "\n"
            # classid_list.log_Tree(Text, Config_Log.tree_log_file_path)

        previous_green_button_list = now_green_button_list

        count = (count+1)%division

if __name__ == '__main__':
    Detect_and_Show()
    # config = Config_Detection
    # class_list = classid_list.get_class_id_list(config.Detection_path['yaml_path'])
    # class_list = classid_list.append_class_id_list_with_flag(class_list)
    #
    # Detect_Color.detect_color(config.Detection_path['sample_file_path'], config.Detection_path['label_txt_path'], class_list)
    # pass
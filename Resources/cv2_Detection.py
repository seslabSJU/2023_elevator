import os, sys
import Detect_Color
import Sort_image
import classid_list
import Elevator_Linklist
import Elevator_Tree

try:
    from config import Config_Detection, Config_Elevator_SW
except Exception as e:
    pass

def make_tree(tree, elem, count, status=True):
    _, node = Elevator_Tree.return_Node_and_List_From_Root(tree, elem)
    if node is None:
        tree.append_Node(elem)
    Elevator_Tree.print_all_Nodes(tree)

def Detect_and_Show():
    config = Config_Detection
    config_ES = Config_Elevator_SW

    images = Sort_image.get_images(config.Detection_path['image_folder_path'])

    class_list = classid_list.get_class_id_list(config.Detection_path['yaml_path'])
    class_list = classid_list.append_class_id_list_with_flag(class_list)

    tree = Elevator_Tree.LinkedList()
    tree.set_Root()

    previous_green_button_list = []
    previous_frame = -1

    count = 1

    for img_path in images:
        print("Reading Button Log From image {}...".format(img_path))
        config.Detection_path['image_file_path'] = img_path

        now_gree_button_list = Detect_Color.detect_color(img_path, config.Detection_path['label_txt_path'], class_list)

        # for i, e in enumerate(now_gree_button_list):
        #     elem = config_ES.Location_Weight[e[0]]
        #     status = e[1]
        #     make_tree(tree, elem, count, status)


        frame = classid_list.log_green_button(config, previous_green_button_list, now_gree_button_list)

        if frame is not None:
            if previous_frame == -1:
                previous_frame = frame
            else:
                interval = float((frame-previous_frame)/30)
                classid_list.log_interval(interval)
                previous_frame = frame

        previous_green_button_list = now_gree_button_list

        count = (count+1)%30

if __name__ == '__main__':
    Detect_and_Show()
    # config = Config_Detection
    # class_list = classid_list.get_class_id_list(config.Detection_path['yaml_path'])
    # class_list = classid_list.append_class_id_list_with_flag(class_list)
    #
    # Detect_Color.detect_color(config.Detection_path['sample_file_path'], config.Detection_path['label_txt_path'], class_list)
    # pass
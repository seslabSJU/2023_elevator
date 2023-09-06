import os
import re
import natsort

def extract_frame_number(path):
    match = re.search(r'(\d+)\.jpg', path)
    if match:
        return int(match.group(1))
    return -1

def get_images(path):
#    formats = ['.jpg']
#    path_list = []
    
#    natsort.natsorted(os.listdir(path))

#    for root, dir, files in os.walk(path):
#        for file in files:
#            file_path = os.path.join(root, file)
#            file_path = file_path.replace('\\','/')
#            path_list.append(file_path)
#
#    sorted_img = sorted(path_list, key=extract_frame_number)
    list_of_picture_path = natsort.natsorted(os.listdir(path))
    
    return list_of_picture_path

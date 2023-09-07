import cv2
import View_Label
import Video_To_Image
import Raspi_Shoot
from config import Config_DefaultPath, Config_Detection

def get_sample_and_label():
	if Config_DefaultPath.sample_default_path is None:
		print("ERROR in Pic_and_Show, Config_DefaultPath.sample_default_path is None")
		exit(1)
	
	else:
		sample_name = "sample.jpg"
		image_path = f"{Config_DefaultPath.sample_default_path}/{sample_name}"
		
		image_path = Raspi_Shoot.take_one_picture(image_path)	
		#Video_To_Image.Rotate_Picture(image_path)
		
		image = cv2.imread(image_path)
		View_Label.display_label_info(image, Config_Detection.Detection_path['label_txt_path'])

if __name__ == '__main__':
	pass
	
	

import os
from config import Config_DefaultPath

def make_dirs_for_videocapture():
	default_path = os.getcwd()
	
	os.chdir(os.path.expanduser('~'))
	home_path = os.getcwd()
	
	os.chdir('Desktop')
	desktop_path = os.getcwd()
	
	dir_name = "Elevator_Results"
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
				
	os.chdir(dir_name)
	folder_deafult_path = os.getcwd()
	
	dir_name = "Videos"
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
				
	os.chdir(dir_name)
	video_capture_deafult_path = os.getcwd()

	Config_DefaultPath.home_path = home_path
	Config_DefaultPath.default_path = default_path
	Config_DefaultPath.folder_deafult_path = folder_deafult_path
	Config_DefaultPath.video_capture_deafult_path = video_capture_deafult_path
	
	os.chdir(default_path)
	
def make_dirs_for_logs(folder_deafult_path):
	if folder_deafult_path is None:
		print("Elevator_Results Folder Dont Exists!")
		exit(0)
	
	else:
		os.chdir(folder_deafult_path)
		
		dir_name = "Logs"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
		
		os.chdir(dir_name)
		log_default_path = os.getcwd()
		
		os.chdir(folder_deafult_path)
		
		dir_name = "Pictures"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
		
		os.chdir(dir_name)
		picture_default_path = os.getcwd()
		
		Config_DefaultPath.log_default_path = log_default_path
		Config_DefaultPath.picture_default_path = picture_default_path
	
if __name__ == '__main__':
	make_dirs_for_videocapture()
	make_dir_for_logs(Config_DefaultPath.folder_deafult_path)

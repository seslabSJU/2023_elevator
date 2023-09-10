import os
import shutil
import glob
import re
from config import Config_DefaultPath, Config_Detection

def video_list_from_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Error in Video_To_Image, video folder not found")
        exit(1)
    else:
        target = os.path.join(folder_path, '**/*.h264')
        video_list = glob.glob(target, recursive=True)

        if video_list is None:
            print("Error in Video_To_Image, video list is None")
            return None
        else:
            return video_list

def get_Raspi_Number(video_path):
	if not os.path.exists(video_path):
		print("Error in Video_To_Image, video_path not found")
		exit(1)
	else:
		pattern = r"(No\d+)_(\d{14})+\.h264"

		match = re.search(pattern, video_path)
		if match:
			Raspi_Number = match.group(1)
			start_timestamp = match.group(2)
			return Raspi_Number, start_timestamp
		else:
			print("Error in Video_To_Image, Raspi Number is None. Wrong Video name")
			return None

def make_dirs_for_program_Linux():
	default_path = os.getcwd()
	
	os.chdir(os.path.expanduser('~'))
	home_path = os.getcwd()
	
	os.chdir('Desktop')
	desktop_path = os.getcwd()
	
	dir_name = "Elevator_Results"
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)
				
	os.chdir(dir_name)
	folder_default_path = os.getcwd()

	Config_DefaultPath.home_path = home_path
	Config_DefaultPath.code_default_path = default_path
	Config_DefaultPath.folder_default_path = folder_default_path

def make_dirs_for_Elevator_Result_Linux(Raspi_Number):
	if Config_DefaultPath.folder_default_path is None:
		print("Error in Make_Dirs, Elevator_Results Folder Dont Exists!")
		exit(1)

	else:
		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Logs/{Raspi_Number}"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir(f"Logs/{Raspi_Number}")
		log_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Pictures/{Raspi_Number}"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir("Pictures")
		picture_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Sample"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir(dir_name)
		sample_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Videos/{Raspi_Number}"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir("Videos")
		video_capture_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = "Configs"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir(dir_name)
		config_default_path = os.getcwd()

		Config_DefaultPath.log_default_path = log_default_path
		Config_DefaultPath.picture_default_path = picture_default_path
		Config_DefaultPath.sample_default_path = sample_default_path
		Config_DefaultPath.video_capture_default_path = video_capture_default_path
		Config_DefaultPath.config_default_path = config_default_path

def make_files_for_program_Linux(Raspi_Number):
	if Config_DefaultPath.config_default_path is None:
		print("Error in Make_Dirs, Config_DefaultPath.config_default_path is None")
		exit(1)

	else:
		os.chdir(Config_DefaultPath.code_default_path)
		os.chdir('config')

		label_txt_name = fr"label_{Raspi_Number}.txt"
		yaml_name = "data.yaml"
		log_sensor_txt_name = "Log_Sensors.txt"

		shutil.copy(label_txt_name, Config_DefaultPath.config_default_path)
		shutil.copy(yaml_name, Config_DefaultPath.config_default_path)
		shutil.copy(log_sensor_txt_name, Config_DefaultPath.log_default_path)

		Config_Detection.Detection_path['label_txt_path'] = f"{Config_DefaultPath.config_default_path}/{label_txt_name}"
		Config_Detection.Detection_path['yaml_path'] = f"{Config_DefaultPath.config_default_path}/{yaml_name}"

def make_dirs_for_program_Windows():
	default_path = os.getcwd()

	os.chdir('../..')
	home_path = os.getcwd()

	dir_name = "Elevator_Results"
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)

	os.chdir(dir_name)
	folder_default_path = os.getcwd()

	#print("{}\n{}\n{}\n".format(home_path, default_path, folder_default_path))
	Config_DefaultPath.home_path = home_path
	Config_DefaultPath.code_default_path = default_path
	Config_DefaultPath.folder_default_path = folder_default_path

def make_dirs_for_Elevator_Result_Windows(Raspi_Number):
	if Config_DefaultPath.code_default_path is None:
		print("Error in Make_Dirs, Elevator_Results Folder Dont Exists!")
		exit(1)

	else:
		os.chdir(Config_DefaultPath.code_default_path)
		# print("Default Path is {}".format(folder_default_path))

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Logs\{Raspi_Number}"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir(f"Logs\{Raspi_Number}")
		log_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Pictures\{Raspi_Number}"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir("Pictures")
		picture_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Sample"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir(dir_name)
		sample_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = f"Videos\{Raspi_Number}"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir("Videos")
		video_capture_default_path = os.getcwd()

		os.chdir(Config_DefaultPath.folder_default_path)
		dir_name = "Configs"
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		os.chdir(dir_name)
		config_default_path = os.getcwd()

		#print("{}\n{}\n{}\n{}\n{}\n".format(log_default_path,picture_default_path,sample_default_path,video_capture_default_path,config_default_path))
		Config_DefaultPath.log_default_path = log_default_path
		Config_DefaultPath.picture_default_path = picture_default_path
		Config_DefaultPath.sample_default_path = sample_default_path
		Config_DefaultPath.video_capture_default_path = video_capture_default_path
		Config_DefaultPath.config_default_path = config_default_path

		os.chdir(Config_DefaultPath.folder_default_path)

def make_files_for_program_Windows(Raspi_Number):
	if Config_DefaultPath.config_default_path is None:
		print("Error in Make_Dirs, Config_DefaultPath.config_default_path is None")
		exit(1)

	else:
		os.chdir(Config_DefaultPath.code_default_path)
		#print(Config_DefaultPath.code_default_path)
		os.chdir('config')

		label_txt_name = fr"label_{Raspi_Number}.txt"
		yaml_name = "data.yaml"
		log_sensor_txt_name = "Log_Sensors.txt"

		shutil.copy(label_txt_name, Config_DefaultPath.config_default_path)
		shutil.copy(yaml_name, Config_DefaultPath.config_default_path)
		shutil.copy(log_sensor_txt_name, Config_DefaultPath.log_default_path)

		Config_Detection.Detection_path['label_txt_path'] = fr"{Config_DefaultPath.config_default_path}\{label_txt_name}"
		Config_Detection.Detection_path['yaml_path'] = fr"{Config_DefaultPath.config_default_path}\{yaml_name}"

def make_dir_and_files_Linux(Raspi_Number):
	if Config_DefaultPath.folder_default_path is None:
		make_dirs_for_program_Linux()
	else:
		print("PATH info already exists")
	make_dirs_for_Elevator_Result_Linux(Raspi_Number)
	make_files_for_program_Linux(Raspi_Number)

def make_dir_and_files_Windows(Raspi_Number):
	if Config_DefaultPath.folder_default_path is None:
		make_dirs_for_program_Windows()
	else:
		print("PATH info already exists")
	make_dirs_for_Elevator_Result_Windows(Raspi_Number)
	make_files_for_program_Windows(Raspi_Number)


if __name__ == '__main__':
	# Raspi_Number = "No4"
	# make_dir_and_files_Linux()
	# make_dir_and_files_Windows(Raspi_Number)
	#
	# folder_path = rf"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Videos"
	# l = video_list_from_folder(folder_path)
	# for path in l:
	# 	get_Raspi_Number(path)
	pass

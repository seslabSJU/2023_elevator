class Config_Detection:
    # Detection_path = {
    #     'image_folder_path': f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Vid_No3_2023-06-30-15-03',
    #     'sample_folder_path': f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Sample',
    #     'sample_file_path': f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Vid_No3_2023-06-30-15-03\\frame_20130.jpg',
    #     'image_file_path': f'',
    #     'label_txt_path': f"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\cv2\config\Base3.txt",
    #     'yaml_path': r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\cv2\config\data.yaml",
    # }
    Detection_path = {
        'image_folder_path': f'/home/user/Videos/Pictures',
        'image_file_path': f'',
        'sample_folder_path': f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Sample',
        'sample_file_path': f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Real\Vid_No3_2023-06-30-15-03\\frame_20130.jpg',
        'label_txt_path': f"/home/user/Videos/configs/label.txt",
        'yaml_path': r"/home/user/Videos/configs/data.yaml"
    }
    Detection_Range = {
        'MinCircleArea': 0.0,
        'ClassificationRange': 0.15
    }


class Config_Color:
    Color_Base = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    # In cv2 it default use BGR instead of RGB
    Color_CV2 = {
        'red': (0, 0, 255),
        'green': (0, 255, 0),
        'blue': (255, 0, 0),
        'cv2_inrange_lowest': [130, 185, 60],  # [170, 235, 30]
        'cv2_inrange_highest': [225, 245, 120]  # [245, 255, 245]
    }


class Config_Label:
    Text = {
        'height': 20,
        'margin': 30,
        'font_scale': 0.75,
        'font_size': 2
    }


class Config_Elevator_HW:
    Motor = {

    }
    Accelerator = {
        'Velocity': -5.5
    }
    Usage_Intensity = {
        'Verylow': 75,
        'Low': 200,
        'Medium': 500,
        'High': 1000,
        'Very High': 2000,
        'Extremely High': 2500,
    }
    Stopping_Floors = {
        '2': 2,
        '3': 3
    }
    First_Floor_Altitude = 0.0
    Current_Floor_Altitude = None
    Height_Per_Floor = 4.5
    Height = 3.0
    Trip = 0
    Energy_per_Cycle = {
        'Short_Cycle': 1.0,

    }


class Config_Elevator_SW:
    Default_Location = "1"
    Location_Weight = {
        'Open': 999,
        'Close': 999,
        'B5': -5,
        'B4': -4,
        'B3': -3,
        'B2': -2,
        'B1': -1,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        '11': 11,
        '12': 12,
        'Panel': 999
    }
    Location_List = [999, 999, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 999]
    Lowest_Weight = -5
    Highest_Weight = 12
    Current_Floor = -1


class Config_Log:
    # log_file_path = r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Log\Button_Logs\Log_Condition.txt"
    # timelist_log_file_path = r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Log\Button_Logs\Log_Floor.txt"
    # sensor_log_file_path = r"E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Log\Button_Logs\Log_Sensors.txt"
    # extract_pattern = r": \[\['\w+', (?:True:False)\]\]"
    extract_pattern = r"\['(\w+)', (?:True|False)\]"

class Config_VideoCapture:
    video_capture_dir_path = None
    video_capture_result_dir_path = None

class Config_DefaultPath:
    home_path = None
    default_path = None
    folder_default_path = None
    video_capture_default_path = None
    log_default_path = None
    picture_default_path = None
    config_default_path = None
    label_txt_default_path = None
    yaml_default_path = None

class Config_Model:
    Model_Train = {
        'data': f'datasets/SAI Elevator.v1i.yolov8.yaml',
        'imgsz': 640,
        'epochs': 50,
        'batch': 8,
        'name': 'CC'
    }

    Model_Test = {
        'source': f'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Elevator_Sample',
        'imgsz': 640,
        'conf': 0.5,
        'save': True
    }

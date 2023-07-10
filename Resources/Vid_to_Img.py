import cv2
import os
import time
from tqdm import tqdm
from multiprocessing import Pool

Video_Folder_Path = os.path.join(os.getcwd(), '/ML/Videos')
Image_Save_Path = 'E:\ML\Images'
frame_interval = 30

num_processes = os.cpu_count()
def Extract_Img_From_Video(args):
    Video_Path, Save_Path, frame_interval = args

    frame_count = 0

    if os.path.isfile(Video_Path):	

        cap = cv2.VideoCapture(Video_Path)
    else:
        print("Error: File not Exist")

    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))	# width frame 
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))	# height frame

    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Resolution: {frameWidth}x{frameHeight}")
    print(f"FPS: {fps}")

    pbar = tqdm(total=18000 // frame_interval, unit='frames', ncols=80,
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:3.0f}%]')

    start_time = time.time()
    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            break

        # Check if it's time to save a frame
        if frame_count % frame_interval == 0:
            rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(f'{Save_Path}\\frame_{frame_count}.jpg', rotated_frame)
            pbar.update()
            #print(f"Saved frame {frame_count}")

        frame_count += 1

    # Release the video file
    cap.release()
    pbar.close()

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

    print("Frame extraction completed.")

def process_videos(video_folder_path, image_save_path, frame_interval):
    video_files = os.listdir(video_folder_path)
    video_infos = []

    for video_file in video_files:
        video_name = os.path.splitext(video_file)[0]
        video_path = os.path.join(video_folder_path, video_file)
        save_path = os.path.join(image_save_path, f'Vid_{video_name}')

        if video_name.startswith('No') and os.path.isfile(video_path):
            os.makedirs(save_path, exist_ok=True)
            #Extract_Img_From_Video(video_path, save_path, frame_interval)
            video_infos.append((video_path, save_path, frame_interval))
        else:
            print(f"Ignoring {video_file}: Invalid video name format")

    print(f"Total videos to process: {len(video_infos)}")

    with Pool(processes=num_processes) as pool:
        pool.map(Extract_Img_From_Video, video_infos)
    print("Processing of all videos completed.")

if __name__ == '__main__':
    process_videos(Video_Folder_Path, Image_Save_Path, frame_interval)
import glob
import os
import time
import datetime
import cv2


def extract_frames(video_path, output_folder, start_timestamp, second=-1):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        extract_frames_logic(video_path, output_folder, start_timestamp, second)

    elif len(os.listdir(output_folder)) == 0:
        extract_frames_logic(video_path, output_folder, start_timestamp, second)

    else:
        print("Picture Already Exists in this folder")
        exit(1)

def extract_frames_logic(video_path, output_folder, start_timestamp, second=-1):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    if second == -1:
        ret, frame = cap.read()
        while ret:
            timestamp = start_timestamp + datetime.timedelta(seconds=frame_count/15.0)

            if frame_count % 15 == 0:
                timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")

                # Save the frame as an image
                frame_filename = os.path.join(output_folder, f'{timestamp_str}.jpg')

                print(f"Frames extracted and saved to {output_folder} as {timestamp_str}.jpg")
                cv2.imwrite(frame_filename, frame)

            frame_count += 1
            ret, frame = cap.read()
        cap.release()
    else:
        count = 0
        while count != second:
            # Read a frame from the video
            ret, frame = cap.read()

            if not ret:
                break
            timestamp = start_timestamp + datetime.timedelta(seconds=frame_count/15.0)
            count = count + 1

            if frame_count % 15 == 0:
                timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")

                # Save the frame as an image
                frame_filename = os.path.join(output_folder, f'{timestamp_str}.jpg')

                print(f"Frames extracted and saved to {output_folder} as {timestamp_str}.jpg")
                cv2.imwrite(frame_filename, frame)

            frame_count += 1
        cap.release()

def Rotate_Frames(Frame_Foler_Path):
    if not os.path.exists(Frame_Foler_Path):
        print(f"Folder '{Frame_Foler_Path}' does not exist.")
        return

    file_list = sorted(os.listdir(Frame_Foler_Path))

    # Iterate through the files in the folder
    for filename in file_list:
        file_path = os.path.join(Frame_Foler_Path, filename)

        # Check if the file is an image (you can add more image extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Read the image
            image = cv2.imread(file_path)

            if image is not None:
                # Rotate the image 90 degrees to the right
                rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                cv2.imwrite(file_path, rotated_image)
                print(f"Rotated and saved: {file_path}")

def Rotate_Picture(picture_path):
    # Read the image
    image = cv2.imread(picture_path)

    if image is not None:
        # Rotate the image 90 degrees to the right
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(picture_path, rotated_image)
        print(f"Rotated and saved: {picture_path}")

if __name__ == '__main__':
    # vid = '/home/user/Videos/libcamera_vid/Result/No1_20230726235205.h264'
    # vid_name = 'No1_20230726235205.h264'
    # output = f'/home/user/Videos/Pictures/{vid_name}'
    # time = datetime.datetime.now()
    # extract_frames(vid, output, time)
    pass

import os
import shutil

def dup_annotation_txt(photo_folder_path, txt_file_path):
    photo_files = [f for f in os.listdir(photo_folder_path) if f.startswith('frame_') and f.endswith('.jpg')]

    for photo_file in photo_files:
        photo_name = os.path.splitext(photo_file)[0]
        new_annotation_txt_path = os.path.join(photo_folder_path, f'{photo_name}.txt')

        shutil.copy2(txt_file_path, new_annotation_txt_path)

        print(f"Dup {txt_file_path} to {new_annotation_txt_path}")
    print("Dup Completed")

# Example usage
photo_folder_path = 'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Elevator_Sample'
annotation_txt_path = 'E:\ML\Elevator Git\Effective-Elevator-Energy-Calculation-for-SejongAI-Center\Images_Sample\Sample_Annotes\\frame_360.txt'
dup_annotation_txt(photo_folder_path, annotation_txt_path)
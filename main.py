import cv2
import os
import random
from RenameMusics import RenameMusics
from GenFolders import SplitPicsToOtherFolders

IMAGE_FOLDER = './images/'
MUSIC_FOLDER = './music/'

# Preprocess
SplitPicsToOtherFolders(IMAGE_FOLDER)
RenameMusics(MUSIC_FOLDER)

random_number = random.randint(0,len(os.listdir('./music/')) - 1)
input_audio_path = os.path.join(MUSIC_FOLDER, os.listdir(MUSIC_FOLDER)[random_number])


def get_last_folder_name(path):
    folders = path.strip('/').split('/')
    return folders[-1]


def GenerateVideo(image_path):
    try:
        input_video_path = './output.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        images = [img for img in os.listdir(image_path) if img.endswith('.png')]

        # Get the first image to use as a reference for the video size
        frame = cv2.imread(os.path.join(image_path, images[0]))
        height, width, channels = frame.shape

        frame_duration = 4  # sec

        # Create a video writer object
        out = cv2.VideoWriter(input_video_path, fourcc, 1.0, (width, height))

        # Loop through the images and add them to the video
        for img in images:
            # Load the image and write it to the video writer for the duration of the frame
            frame = cv2.imread(os.path.join(image_path, img))
            for i in range(frame_duration):
                out.write(frame)

        # Release the video writer and destroy all windows
        out.release()
        output_file = get_last_folder_name(image_path) + '.mp4'
        command = "ffmpeg -i {} -i {} -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 -t 70 {}".format(input_video_path, input_audio_path, output_file)
        os.system(command)
        os.remove('./output.mp4')
        cv2.destroyAllWindows()
    except Exception as e:
        print(image_path, e)

def GenAllVideos(IMAGE_FOLDER):
    folders = os.listdir(IMAGE_FOLDER)
    folders_with_path = [os.path.join(IMAGE_FOLDER, folder) for folder in folders]
    for image_path in folders_with_path:
        GenerateVideo(image_path)


GenAllVideos(IMAGE_FOLDER)
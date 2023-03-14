import os
extension = ".mp3"  # replace with the extension of the files you want to rename


def RenameMusics(folder_path):
    counter = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            new_filename = f"music_{counter}{extension}"
            new_file_path = os.path.join(folder_path, new_filename)
            if not os.path.exists(new_file_path):
                os.rename(os.path.join(folder_path, filename), new_file_path)
                counter += 1

import os


def SplitPicsToOtherFolders(dir_path):
    # Define the number of pictures to include in each subfolder
    batch_size = 17

    folders_list = os.listdir(dir_path)
    for folder in folders_list:
        original_folder = os.path.join(dir_path, folder)
        file_names = os.listdir(original_folder)
        # Create the subfolders and move the pictures into them
        for i in range(0, len(file_names), batch_size):
            # Create a subfolder name based on the batch number
            subfolder_name = f'{folder}_{i // batch_size + 1}'
            os.makedirs(os.path.join(dir_path, subfolder_name), exist_ok=True)  # create folder if not exist

            # Get the batch of file names for this subfolder
            batch_file_names = file_names[i:i + batch_size]

            # Move the batch of files into the subfolder
            for file_name in batch_file_names:
                src_path = os.path.join(dir_path, folder, file_name)
                dst_path = os.path.join(dir_path, subfolder_name, file_name)
                os.rename(src_path, dst_path)
        os.rmdir(os.path.join(dir_path, folder))
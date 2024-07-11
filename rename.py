# import os


# def rename_files(test_folder, groundtruth_folder, start_index=0):
  
#     test_files = sorted([f for f in os.listdir(test_folder) if f.endswith('.png') or f.endswith('.jpg')])
#     groundtruth_files = sorted([f for f in os.listdir(groundtruth_folder) if f.endswith('.png')or f.endswith('.jpg')])
 
#     for i, (test_file, groundtruth_file) in enumerate(zip(test_files, groundtruth_files)):
#         base_name = f"{start_index + i:03d}"
#         new_name = f"{base_name}.png"
        
#         # Rename test files
#         os.rename(os.path.join(test_folder, test_file), os.path.join(test_folder, new_name))
#         new_name = f"{base_name}_mask.png"
        
#         # Rename groundtruth files
#         os.rename(os.path.join(groundtruth_folder, groundtruth_file), os.path.join(groundtruth_folder, new_name))

# def main():
#     test_broken_folder = './tags_seg/test/missing_letter'
#     groundtruth_broken_folder = './tags_seg/ground_truth/missing_letter'

#     # Rename files in both folders ensuring corresponding names
#     rename_files(test_broken_folder, groundtruth_broken_folder)

# if __name__ == "__main__":
#     main()

import os

def rename_files(folder_path, start_index=0):
    files = sorted(os.listdir(folder_path))
    for i, filename in enumerate(files):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            new_name = f"{start_index + i:03d}.png"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

def main():
    train_good_folder = './datasets/MVTec/tags_seg/test/good'
    test_good_folder = './datasets/MVTec/tags_seg/train/good'


    # Rename files in test/broken
    rename_files(train_good_folder)
    rename_files(test_good_folder)


if __name__ == "__main__":
    main()
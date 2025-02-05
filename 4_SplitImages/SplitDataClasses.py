import argparse
import os
import shutil
from random import seed
from random import sample

# Add Parser
parser = argparse.ArgumentParser()

parser.add_argument("--train", type=int, default=80, help="Percentage of train set")
parser.add_argument("--validation", type=int, default=10, help="Percentage of validation set")
parser.add_argument("--test", type=int, default=10, help="Percentage of test set")
parser.add_argument("--folder", type=str, default="img", help="Folder that contain image")
parser.add_argument("--dest", type=str, default="img-dest", help="Destination folder")
parser.add_argument("--random_seed", type=int, default=42, help="Random seed for reproducibility")  # Added argument for random seed

args = parser.parse_args()

# Set the random seed for reproducibility
seed(args.random_seed)

def get_difference_from_2_list(list1, list2):
    set_list1 = set(list1)
    set_list2 = set(list2)

    diff = list(set_list1.difference(set_list2))

    return diff

def get_split_data(list_id):
    # Train Set
    # Count number of training data
    n_train = (count * args.train) / 100
    # Random
    train = sample(list_id, int(n_train))

    list_id = get_difference_from_2_list(list_id, train)

    # Validation Set
    # Count number of validation data
    n_valid = (count * args.validation) / 100

    # Random
    valid = sample(list_id, int(n_valid))

    # Test Set
    test = get_difference_from_2_list(list_id, valid)

    return train, valid, test

def make_folder(class_folder):    
    folders = ["train", "val", "test"]

    if(not os.path.isdir(args.dest)):
        os.mkdir(args.dest)

    for folder in folders:
        path = os.path.join(args.dest, folder)
        # Check existing folder
        if(not os.path.isdir(path)):
            os.mkdir(path)     

        # Folder class            
        class_path = os.path.join(path, class_folder)
        # Check folder
        if(not os.path.isdir(class_path)):
            os.mkdir(class_path)

def copy_image(file, id_folder, class_folder):
    inner_folders = ["train", "val", "test"]    

    # Image
    source = os.path.join(args.folder, class_folder)
    source = os.path.join(source, file)
    
    destination = os.path.join(args.dest, inner_folders[id_folder])   
    destination = os.path.join(destination, class_folder)

    try:
        shutil.copy(source, destination)
        # print("File copied successfully.")

    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")    

# Check train set
if((args.train < args.validation) or (args.train < args.test) ):
    print("Train set must has a biggest Percentage")
    exit()

# Check total percentage
total = args.train + args.validation + args.test
if(total > 100):
    print("Total Percentage must 100%")
    exit()

# Access all folder
for folder in os.listdir(args.folder):
    class_folder = os.path.join(args.folder, folder)
    is_dir = os.path.isdir(class_folder)
    
    if(is_dir):
        # Count number of data
        count = 0
        list_id = []
        for file in os.listdir(class_folder):    
            if ((file.endswith(".jpg")) or (file.endswith(".png"))):                       
                list_id.append(count)
                count += 1

        train, valid, test = get_split_data(list_id)
        make_folder(folder)

        count = 0
        for file in os.listdir(class_folder):
            if ((file.endswith(".jpg")) or (file.endswith(".png"))):
                if(count in train):			
                    copy_image(file, 0, folder)
                elif(count in valid):			
                    copy_image(file, 1, folder)
                else:			
                    copy_image(file, 2, folder)			

                count += 1

import os
import shutil

os.chdir(r"C:\Users\muham\Desktop\YOLOMODEL1")

folders = os.listdir("4_SplitImages/Train")
subfolders = ["buy", "hold", "sell"]

for folder in folders:

    test_folder = folder[0:-5] + "Test"
    
    if not os.path.exists(f"4_SplitImages/Test/{test_folder}"):
        os.makedirs(f"4_SplitImages/Test/{test_folder}")
    
    for subfolder in subfolders:

        files = os.listdir(f"4_SplitImages/Train/{folder}/test/{subfolder}")

        for file in files:

            sourcepath = f"4_SplitImages/Train/{folder}/test/{subfolder}/{file}"
            destinationpath = f"4_SplitImages/Test/{test_folder}/{file}"
            shutil.copy(sourcepath,destinationpath)
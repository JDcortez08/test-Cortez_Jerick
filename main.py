import os
import shutil

folder_path = input("enter folder path")
if os.path.exists():
    print("this files exist")
else:
    print("fail")

os.listdir(folder_path)
images = 0
documents = 0
videos = 0
others = 0

folder_path = os.listdir("image, document, videos, others")
print()




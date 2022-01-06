import os
import shutil
source=input("Enter the source name:")
dst=input("Enter the destination name:")
source=source+"/"
dst=dst+"/"
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),dst)
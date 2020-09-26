#! /usr/bin/env python3
"""
Created by MD Fardeen Ehsan Shawon
https://facebook.com/fardeen.es7
https://github.com/fardeenes7/
fardeen.es7@gmail.com
"""

import os
import subprocess
import time

myDir = ""  # Enter expected directory or leave black for current directory
files = os.listdir(myDir)
# Edit filetypes as your wish.
filetypes = ["Document", "Presentation", "Pictures", "Compressed", "App", "Video", "Folders"]
for filetype in filetypes:
    os.mkdir(filetype)


def ext(filename):
    for i in range(-1, -len(filename), -1):
        if filename[i] == ".":
            extension = filename[i + 1:]
            return extension


# Change the filetypes and keep the return value similar to the filetypes defined at the top.
def filetype(file_name):
    exts = ext(file_name.lower())
    if exts == 'txt' or exts == 'docx' or exts == 'doc' or exts == "pdf" or exts == "xml":
        return "Document"
    elif exts == "ppt" or exts == "pptx":
        return "Presentation"
    elif exts == "jpg" or exts == "jpeg" or exts == "png" or exts == "gif" or exts == "svg":
        return "Pictures"
    elif exts == "zip" or exts == "rar" or exts == "gz" or exts == "bz2" or exts == "xz":
        return "Compressed"
    elif exts == "exe" or exts == "deb" or exts == "apk":
        return "App"
    elif exts == "mkv" or exts == "mp4" or exts == "mpeg":
        return "Video"
    else:
        return None


logfile = open(myDir + "error.log", 'w')
error_count = 0
success = 0
start = time.time()
for file in files:
    print(file)
    if file in filetypes:
        continue
    if os.path.isdir(myDir + file):
        file_type = "Folders"
    else:
        file_type = filetype(file)

    if file_type is None:
        print("FIle type not recognised: could't move")
        logfile.write(file + " couldn't be moved\n")
        error_count += 1
        continue
    try:
        src = myDir + file
        path = myDir + file_type + "/" + file
        subprocess.run(["mv", src, path])
        print("File type: " + file_type)
        print("Moved Successfully")
        success += 1
    except FileNotFoundError:
        print("Error: File Not Found")

logfile.write("Errors: " + str(error_count))
logfile.close()
print(str(success) + " files moved successfully")
print(str(error_count) + " errors. Check <error.log> for details.")
end = time.time()
total_time = end - start
print("Completed in " + str(total_time) + " seconds.")

"""
Remove the logfile and print statements if you wish to make the code faster.
"""

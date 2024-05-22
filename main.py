# Importing the required libraries
import os
import collections
from pprint import pprint

# Defining the file extensions
AUDIO_EXTENSIONS = ["mp3", "wav", "raw", "wma", "mid", "midi", "aac", "flac", "ogg"]
VIDEO_EXTENSIONS = [
    "mp4",
    "mpg",
    "mpeg",
    "avi",
    "mov",
    "flv",
    "mkv",
    "wmv",
    "m4v",
    "h264",
]
IMAGE_EXTENSIONS = [
    "png",
    "jpg",
    "jpeg",
    "gif",
    "svg",
    "bmp",
    "psd",
    "tiff",
    "tif",
    "ico",
    "webp",
]
DOCUMENT_EXTENSIONS = [
    "txt",
    "pdf",
    "csv",
    "xls",
    "xlsx",
    "ods",
    "doc",
    "docx",
    "html",
    "odt",
    "tex",
    "ppt",
    "pptx",
    "log",
    "rtf",
    "md",
]
COMPRESSED_EXTENSIONS = [
    "zip",
    "z",
    "7z",
    "rar",
    "tar",
    "gz",
    "rpm",
    "pkg",
    "deb",
    "xz",
]
INSTALLER_EXTENSIONS = ["dmg", "exe", "iso", "msi"]

# Defining the destination directories
BASE_PATH = os.path.join(os.getenv("USERPROFILE"), "Downloads")
DEST_DIRS = ["Audio", "Video", "Images", "Documents", "Applications", "Others"]

# Creating the destination directories
for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Mapping files from Downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(BASE_PATH)
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    file_path = os.path.join(DOWNLOADS_PATH, file_name)
    if os.path.isfile(file_path) and file_name not in DEST_DIRS:
        file_ext = file_name.split(".")[-1].lower()
        if len(file_name.split(".")) > 1 and file_ext.isalnum():
            files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# Traverse through folders to find applications and move them
for root, dirs, files in os.walk(DOWNLOADS_PATH):
    if any(d in DEST_DIRS for d in root.split(os.path.sep)):
        continue  # Skip processing destination directories
    for file_name in files:
        file_path = os.path.join(root, file_name)
        file_ext = file_name.split(".")[-1].lower()
        if file_ext in INSTALLER_EXTENSIONS:
            # Move the entire top-level folder to Applications
            top_level_folder = os.path.split(root)[-1]
            dest_dir = os.path.join(BASE_PATH, "Applications", top_level_folder)
            os.makedirs(dest_dir, exist_ok=True)
            try:
                os.rename(root, os.path.join(dest_dir, file_name))
            except PermissionError:
                # Close any open file handles before renaming
                os.close(os.open(root, os.O_RDONLY))
                os.rename(root, os.path.join(dest_dir, file_name))
            break  # Move to the next folder
    else:
        # If no application file found, move the folder to Others
        if root != DOWNLOADS_PATH:
            dest_dir = os.path.join(BASE_PATH, "Others")
            try:
                os.rename(root, os.path.join(dest_dir, os.path.split(root)[-1]))
            except PermissionError:
                # Close any open file handles before renaming
                os.close(os.open(root, os.O_RDONLY))
                os.rename(root, os.path.join(dest_dir, os.path.split(root)[-1]))

# Moving files to their respective directories
for f_ext, f_list in files_mapping.items():

    if f_ext in INSTALLER_EXTENSIONS:
        dest_dir = os.path.join(BASE_PATH, "Applications")
    elif f_ext in AUDIO_EXTENSIONS:
        dest_dir = os.path.join(BASE_PATH, "Audio")
    elif f_ext in VIDEO_EXTENSIONS:
        dest_dir = os.path.join(BASE_PATH, "Video")
    elif f_ext in IMAGE_EXTENSIONS:
        dest_dir = os.path.join(BASE_PATH, "Images")
    elif f_ext in DOCUMENT_EXTENSIONS or f_ext in COMPRESSED_EXTENSIONS:
        dest_dir = os.path.join(BASE_PATH, "Documents")
    else:
        dest_dir = os.path.join(BASE_PATH, "Others")

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file in f_list:
        try:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(dest_dir, file))
        except FileNotFoundError as e:
            print(f"Error moving file {file}: {e}")

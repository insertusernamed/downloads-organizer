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
DEST_DIRS = ["Audio", "Video", "Images", "Documents", "Applications", "Other"]

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
    if file_name[0] != ".":
        file_ext = file_name.split(".")[-1]
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

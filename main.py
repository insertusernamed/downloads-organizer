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

# Use to package the project

import os
import zipfile
import re

base_dir = '22125038_22125049_22125077_22125108'

if os.path.exists(base_dir+".zip"):
    os.remove(base_dir+".zip")

with zipfile.ZipFile(base_dir+".zip", 'w') as zipf:
    folders = [
        "Source/problem/",
        "Source/solutions/",
        "Source/strategy/",
        "Source/utils/",
        "Source/visualize/",
    ]
    for folder in folders:
        print(f"Zipping {folder}")
        for root, _, files in os.walk(base_dir+"/"+folder):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), base_dir))
    src_files = [
        "input-.*.txt",
        "output-.*.txt",
        "README.txt",
        "main.py",
        "visualize.py",
        "requirements.txt",
    ]
    for file in os.listdir(base_dir+"/Source"):
        # print(file)
        if re.match("|".join(src_files), file):
            print(f"Zipping {file}")
            zipf.write(base_dir+"/Source/"+file, os.path.relpath(base_dir+"/Source/"+file, base_dir))
    if os.path.exists(base_dir+"/Report.pdf"):
        zipf.write(base_dir+"/Report.pdf", os.path.relpath(base_dir+"/Report.pdf", base_dir))
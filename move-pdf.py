__author__ = 'jacob'
import os
from shutil import copyfile

common_path = os.path.join("")
initial_path = os.path.join("", common_path)

final_path = os.path.join("", common_path)

for file_name in initial_path:
    copyfile(os.path.join(initial_path, file_name), os.path.join(final_path, file_name))

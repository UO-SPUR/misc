__author__ = 'jacob'
import os
from shutil import copyfile

common_path = os.path.join("RC_Data_FMS", "AppsSPUR", "Files", "AppsSPUR", "22FebSPURapps07a", "PDF")
initial_path = os.path.join("Library", "FileMaker Server", "Data", "Databases", "SPUR", common_path)

final_path = os.path.join("Server HD", "Users", "spur", "Documents", "Web", common_path)

for file_name in initial_path:
    copyfile(os.path.join(initial_path, file_name), os.path.join(final_path, file_name))

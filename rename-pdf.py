#!/usr/bin/env python
__author__ = 'Jacob Bieker'
import os
DATA_DIRECTORY = os.path.join("test_file")
DATA = os.listdir(DATA_DIRECTORY)
file_name_dict = {}

for file_name in DATA:
    split_name = file_name.split("_")
    print split_name
    file_name_dict.setdefault(split_name[0], [])
    # Name has the extra _NUM extension
    if len(split_name) > 1:
        file_name_dict[split_name[0]].append(split_name[1])
    else:
        file_name_dict[split_name[0]].append(0)

for key in file_name_dict:
    if len(file_name_dict[key]) == 1:
        continue
    else:
        max = 0
        for value in file_name_dict[key]:
            if int(value) > max:
                max = value
            elif int(value) == 0:
                path = os.path.join(DATA_DIRECTORY, str(key))
                os.remove(path)
            else:
                path = os.path.join(DATA_DIRECTORY, str(key) + "_" + str(value))
                os.remove(path)
        
        # Now rename the extra files to the original name
        for value in file_name_dict[key]:
            if len(value) > 1:
                path = os.path.join(DATA_DIRECTORY, str(key) + "_" + str(value))
                out_path = os.path.join(DATA_DIRECTORY, str(key))
                os.rename(path, out_path)

# https://data.vision.ee.ethz.ch/cvl/aess/dataset/

import re
import os
import pybboxes as pbx


def create_files(indx):
    with open(path_db, 'r') as f:
        for line in f: 
            with open(path_labels + str(indx) + '.txt', 'w') as new_file:
                indx += 1 

def pascal_voc_to_yolo(x1, y1, x2, y2, image_w = 640, image_h = 480):
    yolo_format = [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]
    
    strg = ''
    for i in yolo_format:
        strg += str(i) + ' '
    
    return strg

def rename_files(indx):
    for file_name in os.listdir(folder_images):
        source = folder_images + file_name
        destination = folder_images + str(indx) + '.png'
        os.rename(source, destination)
        indx += 1

folder_images = "D:\\Summer Practice 2022 - Conti\\aess_dataset\\images\\"
path_db = "D:\\Summer Practice 2022 - Conti\\aess_dataset\\eth02.idl"
path_labels = "D:\\Summer Practice 2022 - Conti\\aess_dataset\\labels\\"

pattern_box_bounds = re.compile(r'(\d+, ){3}\d+')

while True:
    answ = int(input('\n1. For new files; \n2. Rename File; \n0. Exit;\nAnsw : '))
    
    
    if answ == 1:
        indx = int(input('Index: '))
        creating_files_indx = indx
        create_files(creating_files_indx )
        with open(path_db, 'r') as f:
            for line in f:
                matches_box = pattern_box_bounds.finditer(line)
                for match in matches_box:
                    pascal_voc_format = []
                    for item in match.group(0).split(', '):     
                        pascal_voc_format.append(int(item))   
                                           
                    with open(path_labels + str(indx) + '.txt', 'a') as new_file:
                        new_file.writelines('0 ' + pascal_voc_to_yolo(pascal_voc_format[0], pascal_voc_format[1], pascal_voc_format[2], pascal_voc_format[3]) + '\n')           
                                   
                indx += 1
                
    elif answ == 2:
        indx = int(input('Index: '))
        renaming_files_indx = indx
        rename_files(renaming_files_indx)
    else:
        break

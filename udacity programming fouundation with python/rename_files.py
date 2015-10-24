from os import *

def rename_files():
    file_list = listdir(r"E:\Youtube Videos\python\programs\prank")
    print file_list
    saved_path = getcwd()
    chdir(r"E:\Youtube Videos\python\programs\prank")
    for file_name in file_list:
        rename(file_name, file_name.translate(None,"0123456789"))
        
    chdir(saved_path)
    
rename_files()

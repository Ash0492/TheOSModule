import os

def create_folders(folders:list) -> None:
    for folder in folders:
        try:
            os.makedirs(folder)
        except FileExistsError:
            continue
        
def find(path:str,dir:str):
    for child in os.listdir(path):
        fullpath = f"{path}/{child}"
        if child == dir:
            print(fullpath)
        else:
            find(fullpath,dir)
            
create_folders(["tree/c/other_courses/cpp",
"tree/c/other_courses/python",
"tree/cpp/other_courses/c",
"tree/cpp/other_courses/python",
"tree/python/other_courses/c",
"tree/python/other_courses/cpp"])

find("tree","python")
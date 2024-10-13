import os 
folders = input("provide folder name").split()
for folder in folders:
    try:
        files = os.listdir(folder)
        print("listing the folder for the files",folder)
        for file in files:
          print(file)
    except FileNotFoundError:
        print("please provide the valid folder name ",folder)      
        break
    except PermissionError:
        print("permission error")
import os
import shutil
import tkinter
def logSearch():
    try:
        for root, dirs, files in os.walk("C:\\"): #This cn be changed to whatever directory
            for file in files:

                    if file.endswith(".log"):
                        print(os.path.join(root, file))
                        shutil.copy2(os.path.join(root, file) , "C:\\Software Log\\Error_Logs\\2018" )
    except RecursionError:
        pass

def txtSearch():

    for root, dirs, files in os.walk("C:\\"):  # This cn be changed to whatever directory
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))
                shutil.copy2(os.path.join(root, file), "C:\\Software Log\\Info_Logs\\2018")





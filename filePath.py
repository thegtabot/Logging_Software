import os

def makePath():
    global current_year
    current_year = 2018
    os.chdir("C:\\")
    os.mkdir("Software Log")
    os.chdir("C:\\Software Log")
    os.mkdir("Error_Logs")
    os.mkdir("Info_Logs")
    os.chdir("C:\\Software Log\\Error_Logs")
    os.mkdir(str(current_year))
    os.chdir("C:\\Software Log\\Info_Logs")
    os.mkdir(str(current_year))
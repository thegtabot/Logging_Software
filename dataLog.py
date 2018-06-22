import logging
import timeKeeping
import datetime
import logFinder
import os
import filePath
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
current_year = 2018
while True:
    try:
        filePath.makePath()
    except FileExistsError:
       # print("File path already exists, continuing...")
        pass
    year1 = str(datetime.date.today())
    def getError():       #This function is for collecting and storing error data into a log file.
            logging.basicConfig(filename="C:\\Software Log\\Error_Logs\\2018\\Error_Log.log", level=logging.ERROR, format=LOG_FORMAT)
            #logger1 = logging.getLogger()
            #logger1.error(error)
            logFinder.logSearch()


    def getInfo():     #This function is for collecting and storing general information about program operations
        logging.basicConfig(filename="C:\\Software Log\\Info_Logs\\2018\\Info_Log.log", level=logging.INFO, format=LOG_FORMAT)
        logFinder.txtSearch()

    def getYear():   #For checking the the year, and if the year changes, the new year gets added as a folder.
        global current_year
        try:
            if timeKeeping.dayCounter >= 365:
                os.chdir("C:\Software Log\Info_Logs")
                os.mkdir(str(current_year+1))
                os.chdir("C:\Software Log\Error_Logs")
                os.mkdir(str(current_year + 1))
        except FileExistsError:
           # print('File path exists, rerunning ')
            pass

            current_year = current_year + 1
    #testing
    getError()
    getInfo()
    getYear()



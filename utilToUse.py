# %%
# import pywhatkit as kit
import webbrowser as wb
import requests
# from pywhatkit.core.exceptions import InternetException
# from bs4 import BeautifulSoup
import pyautogui
import time
# import inspect
import datetime
import os
import shutil

# Use the inspect module to find the module of the open function
# module_name = inspect.getmodule(open).__name__

# print(f"The 'open' function is part of the {module_name} module.")

# %%
# remaining tasks
## organize the files on your computer by creating folder for each subject
###demo: create source paths dict with the key as the id of the group
##take the latest date you have and put it in the .txt file
## download the messages
#### first initialize your computer as local server
#### second create a javascript post request to your local server
#### third organize the important messages as word file


# %%

# modulePath=kit.__file__
# print(modulePath)
# modulePath2=wb.__file__
# print(modulePath2)

# %%

class InternetException(Exception):
    """
    Host machine is not connected to the Internet or the connection Speed is Slow
    """

    pass


def check_connection() -> None:
    """Check the Internet connection of the Host Machine"""

    try:
        requests.get("https://google.com")
    except requests.RequestException:
        raise InternetException(
            "Error while connecting to the Internet. Make sure you are connected to the Internet!"
        )

# %%
def openGroup(groupID):
    wb.open("https://web.whatsapp.com/accept?code=" + groupID)

# %%

def readLatestDate(file_path):
        try:  
                with open(file_path,'r') as file:
                        line=file.readlines()
                        lastdate=str(line[0])
                        # print(lastdate)
                                
                        parts = lastdate.strip().split('-')
                        if len(parts) == 3:
                                month, day, year = map(int, parts)
                                
                                
                                # print(f"Month: {month}, Day: {day}, Year: {year}")
                                return lastdate

        except FileNotFoundError:
                print(f"File not found: {file_path}")

# latest=readLatestDate(file_path)
        


# %%
def getTodaysDate():
    today = datetime.date.today()

    # Print the date in a specific format (optional)
    formatted_date = str(today.strftime("%d-%m-%Y"))  # Example format: YYYY-MM-DD
    # print("Today's date:", formatted_date)
    return formatted_date
# getTodaysDate()

# %%
def dateDifference(lastdate,today):
    date1=datetime.datetime.strptime(lastdate,"%d-%m-%Y")
    
    date2=datetime.datetime.strptime(today,"%d-%m-%Y")
    dateDiff=date1-date2
    # print(dateDiff)
    print("date 1 is: ",date1)
    print("date 2 is: :",date2)
    daysDiff=dateDiff.days
    print("the difference in days is: ", daysDiff)
    return daysDiff
# print(daysDiff)

# %%
def formattedLastDay(daysDiff,file_path):
    # daysDiff=8
    if daysDiff == 0:
        return 'today'
    elif daysDiff==-1:
        return 'Yesterday'
    elif daysDiff < -1 and daysDiff >= -7:
        date_str = readLatestDate(file_path)
        date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        day_of_week = date_obj.strftime("%A")
        return day_of_week
    else:
        return readLatestDate(file_path).replace("-","/")

    

# %%

def openTheConsole()-> None:
    time.sleep(10)
    screen_width, screen_height = pyautogui.size()
    xCoordins=0
    yCoordins=screen_height//2
    pyautogui.moveTo(xCoordins,yCoordins)
    time.sleep(2)
    pyautogui.rightClick()
    time.sleep(2)
    inspectXCoordins=xCoordins+100
    inspectYCoordins=yCoordins+370
    pyautogui.moveTo(inspectXCoordins,inspectYCoordins)
    pyautogui.leftClick()
    #moving to consolve
    pyautogui.move(100,-138)
    time.sleep(2)
    #clicking on the console
    pyautogui.leftClick()

# %%
def writeCommandsToDownloadFiles(formattedDDDate) -> None:
    time.sleep(10)
    code_lines = [
        'var elements = document.getElementsByClassName("_1jHIY _2OvAm focusable-list-item");',
        "for (var i = 0; i < elements.length; i++) {",
        '    console.log(elements[i])',
        '    var spanElement = elements[i].querySelector("div > div > span");',
        f'    date = "{formattedDDDate}";',
        '    console.log(spanElement.textContent)',
        '    if (spanElement.textContent == date) {',
        '        var nextSiblings = [];',
        '        var nextSibling = elements[i].nextElementSibling;',
        '        while (nextSibling) {',
        '            nextSiblings.push(nextSibling);',
        '            nextSibling = nextSibling.nextElementSibling;',
        '        }',
        '        for (var j = 0; j < nextSiblings.length; j++) {',
        '            console.log(nextSiblings[j]);',
        '            var buttonDiv = nextSiblings[j].querySelector(\'div[role="button"]\');',
        '            if (buttonDiv) {',
        '                buttonDiv.click();',
        '                console.log("we clicked element " + j);',
        '            }',
        '        }',
        '    }',
        '}',
    ]

    for line in code_lines:
        pyautogui.typewrite(line + '\n', interval=0.005)

# %%
def moveToDirectory(destinationPathh) ->None:
    toRemoved='desktop.ini'
    downloadsPath='C:\\Users\\dell\\Downloads'
    destinationPathh="E:\\FCSE\\testScript"

    fileList=os.listdir(downloadsPath)
    if toRemoved in fileList:
        fileList.remove(toRemoved)
    print(len(fileList))
    print(fileList)
    time.sleep(10)
    for fileToMove in fileList:
        sourcePath=os.path.join(downloadsPath,fileToMove)
        distinationPath=os.path.join(destinationPathh,fileToMove)
        try:
            shutil.move(sourcePath,distinationPath)
            print(f"Successfully moved {fileToMove} to {destinationPathh}")
        except FileNotFoundError:
            print(f"File not found: {sourcePath}")
        except Exception as e:
            print(f"An error occurred: {e}")

# %%
if __name__=="__main__":
    file_path = 'E:\projects\lectures downloader\lastDate.txt'  
    destPath="E:\\FCSE\\testScript"
    latestdate=readLatestDate(file_path)

    print(f"the latests date is: {latestdate}, and it's type is {type(latestdate)}")

    todaysDate=getTodaysDate()

    print(f"the today date is: {todaysDate}, and it's type is {type(todaysDate)}")

    difference=dateDifference(latestdate,todaysDate)

    print(f"the difference date is: {difference}, and it's type is {type(difference)}")

    formattedDDate=formattedLastDay(difference,file_path)

    print(f"the formattedDDate date is: {formattedDDate}, and it's type is {type(formattedDDate)}")



    # %%
    openGroup('LWLZdL20Z11B0zI5SPUndn')
    openTheConsole()
    writeCommandsToDownloadFiles(formattedDDate)
    time.sleep(10)
    moveToDirectory(destPath)

# %%


# %%




# %%



# %%
# time.sleep(3)
# code_lines = [
#     # 'var elements = document.getElementsByClassName("_1jHIY _2OvAm focusable-list-item");',
#     # '',
#     # 'for (var i = 0; i < elements.length; i++) {',
#     # '    console.log(elements[i]);',
#     # '}',
#     'var elements = document.getElementsByClassName("_1jHIY _2OvAm focusable-list-item");',
#         "for (var i = 0; i < elements.length; i++) {",
#            ' var spanElement = elements[i].querySelector("div > div > span");',
#             f'date="{formattedDDate}"',
#             """if (spanElement.textContent ==date)
#                 {
#                     var nextSiblings = [];
#                     var nextSibling = elements[i].nextElementSibling;
#                     while (nextSibling) {
#                         nextSiblings.push(nextSibling);
#                         nextSibling = nextSibling.nextElementSibling;
#                     }
#                     for (var j=0;j<nextSiblings.length;j++){
#                         console.log(nextSiblings[j])
#                         var buttonDiv = nextSiblings[j].querySelector('div[role="button"]');
#                         if(buttonDiv){

#                         buttonDiv.click()
#                         console.log("we clicked element " + j )
#                         }

#                     }
#                 }
#             }
#             """
# ]

# for line in code_lines:
#     pyautogui.typewrite(line + '\n', interval=0.005)

# %%
######javascript scripts##############
"""
################spand elements selector##########################
var elements = document.getElementsByClassName("_1jHIY _2OvAm focusable-list-item");
for (var i = 0; i < elements.length; i++) {
    var spanElement = elements[i].querySelector("div > div > span");
    date="10/05/2023"
    if (spanElement.textContent ==date)
    {
        var nextSiblings = [];
        var nextSibling = elements[i].nextElementSibling;
        while (nextSibling) {
            nextSiblings.push(nextSibling);
            nextSibling = nextSibling.nextElementSibling;
        }
        for (var j=0;j<nextSiblings.length;j++){
            console.log(nextSiblings[j])
            var buttonDiv = nextSiblings[j].querySelector('div[role="button"]');
            if(buttonDiv){

            buttonDiv.click()
            console.log("we clicked element " + j )
            }

        }
    # }


}

    console.log(spanElement)



"""
10

# %%




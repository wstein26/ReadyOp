import os, pyautogui, time, datetime, json

# subprocess.Popen([r"C:\Program Files (x86)\AgencyAp\SIMMS v10.4.0\simms.exe"])

CurrentPath = os.getcwd()
#print(CurrentPath)

import webbrowser

url = 'https://i5.readyop.com/fs/4cim/9fb7'

try:
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    Mac = True
except:
    Mac = False
print(Mac)
try:
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    Windows = True
except:
    Windows = False
print(Windows)
try:
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)
    Linux = True
except:
    Linux = FalseWRS
print(Linux)

os.chdir(CurrentPath)
WFile = 'PersonalInfomration.JSON'
W_File_Open = open(WFile)
WDict_ST = W_File_Open.read()
WDict = json.loads(WDict_ST)
print(WDict)

LName = WDict['LName']
FName = WDict['FName']
EmployeeID = WDict['EmployeeID']
OrgCode = WDict['OrgCode']


TMC = False
Remote = True
NWR = True
enter = [LName, FName, EmployeeID, OrgCode]
print(enter)
time.sleep(6)
k = 0
while k < len(enter):
        pyautogui.write('\t')
        time.sleep(.05)
        PN = enter[k]
        WAns = str(PN)
        WAns = WAns.capitalize()
        print(WAns)
        if k < 2:
            pyautogui.keyDown('shift')
            pyautogui.typewrite(WAns[0], interval=0.005)
            pyautogui.keyUp('shift')
            pyautogui.typewrite(WAns[1:], interval=0.005)
        else:
            pyautogui.typewrite(WAns, interval=0.005)
        time.sleep(.05)
        k = k + 1
print('Complete')

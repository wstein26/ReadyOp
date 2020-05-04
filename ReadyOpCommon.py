import os, pyautogui, time, datetime, json

# subprocess.Popen([r"C:\Program Files (x86)\AgencyAp\SIMMS v10.4.0\simms.exe"])

CurrentPath = os.getcwd()
#print(CurrentPath)

import webbrowser

url = 'https://i5.readyop.com/fs/4cim/9fb7'
while True:
    os.chdir(CurrentPath)
    WFile = 'UserInfo.JSON'
    W_File_Open = open(WFile)
    WDict_ST = W_File_Open.read()
    WUsers = json.loads(WDict_ST)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('Please Enter your UserID: Eg: SteinbW:')
    UserID = input("UserID: ")
    UserID = UserID.upper()
    if UserID in WUsers:
        WData = WUsers[UserID]
        print('Hello ' + WData['FName'] + '!  Please confirm the information below:')
        print('First Name: ' + WData['FName'])
        print('Last Name: ' + WData['LName'])
        print('Employe ID: ' + WData['EmployeeID'])
        print('Org Code: ' + WData['OrgCode'])
        print("UserID: " + UserID)
        print('If this information is correct, please press enter. Else, type "EDIT"')
        edittest = input('Press Enter or type EDIT: ')
        edit = False
        if edittest == 'EDIT':
            edit = True
        if edittest == 'Edit':
            edit = True
        if edittest == 'edit':
            edit = True
    else:
        print('UserID not found.  Please enter your information.  '
              'If you made a typo in the UserID, please type "Cancel" below.  To coninue with editing, press enter'
              'The currently stored User ID is: ' + UserID)
        edittest = input('Press Enter or type CANCEL: ')
        edit = True
        if edittest == 'CANCEL':
            edit = False
        if edittest == 'Cancel':
            edit = False
        if edittest == 'cancel':
            edit = False
    if edit == True:
        while True:
            print('The terminal will ask you some quick questions. Please answer them with appropriate capitals and no spacing, then press enter')
            FName = input('First Name: ') #eg: William
            LName = input('Last Name: ') #eg: Steinberg
            EmployeeID = input('Employee ID: ') #eg: 1862459
            print("Leave the following blank if the correct Org Code is 414127")
            OrgCode = input('Org Code: ')#eg:"414127"
            print(OrgCode)
            if len(OrgCode) == 0:
                OrgCode = '414127'
            print('Confirm the Following Infomration')
            print('First Name: ' + FName)
            print('Last Name: ' + LName)
            print('Employe ID: ' + EmployeeID)
            print('Org Code: ' + OrgCode)
            clear = input('To Confirm this information is correct, type "True": ')
            if clear == 'TRUE':
                clear = 'True'
            if clear == 'true':
                clear = 'True'
            if clear == 'tRUE':
                clear = 'True'
            if clear == 'T':
                clear = 'True'
            if clear == 't':
                clear = 'True'
            if clear == 'True':
                break
            print("Information Stored")
        jsonconverted = {}
        jsonconverted['LName'] = LName
        jsonconverted['FName'] = FName
        jsonconverted['EmployeeID'] = EmployeeID
        jsonconverted['OrgCode'] = OrgCode
        WUsers[UserID] = jsonconverted
        with open('UserInfo.JSON', 'w') as f:
            json.dump(WUsers, f)
    WData = WUsers[UserID]
    FName = WData['FName']
    LName = WData['LName']
    EmployeeID = WData['EmployeeID']
    OrgCode = WData['OrgCode']
    enter = [LName, FName, EmployeeID, OrgCode]
    print(enter)
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

    TMC = False
    Remote = True
    NWR = True

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

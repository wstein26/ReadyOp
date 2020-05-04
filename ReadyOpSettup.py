import os,json
CurrentPath = os.getcwd()

if 1 == 1:
    while True:
        print('The terminal will ask you some quick questions. Please answer them with appropriate capitals and no spacing, then press enter')
        LName = input('Last Name: ') #eg: Steinberg
        FName = input('First Name: ') #eg: William
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
with open('PersonalInfomration.JSON', 'w') as f:
        json.dump(jsonconverted, f)

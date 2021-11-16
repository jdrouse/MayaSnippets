#Execute Latest file in a folder, even if it isnt python :)
#Might not even work with complex dates and times? .... def iffy.
#John Rouse 11-15-21
#Sourced from:
#https://forums.autodesk.com/t5/motionbuilder-forum/how-to-launch-a-script-from-another-script/td-p/4018492
#https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder

#Modify this line:      ...also should be using raw strings like the example ExecuteCode(r"C:\PythonFolder\PythonScript.py")
folderPath = 'C:\temp\\mat\\'


latestFile = findLatestFile(folderPath)

ExecuteCode(latestFile)


def findLatestFile(folderPath):
        
    import glob
    import os
    
    
    list_of_files = glob.glob(folderPath + '*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file
    
def ExecuteCode(filename):
    codefile = open(filename)
    import imp
    module = imp.new_module("child")
    exec codefile in module.__dict__
    del(codefile,imp)
 
import os, shutil
import subprocess as sp
import re
import time

try:
    taskKill = sp.run(["taskkill", "/IM", "Communicator.exe", "/F"], stdout=sp.PIPE)
    time.sleep(2)
except FileNotFoundError:
    pass

regCommand1 = sp.run(["reg", "delete", "HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{24D4336D-415E-4175-933F-BB9F3986484D}", "/f"], stdout=sp.PIPE)
time.sleep(2)

regCommand3 = sp.run(["reg", "delete", "HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Nextiva App", "/f"], stdout=sp.PIPE)
time.sleep(2)

directory1 = 'C:/Program Files (x86)/Nextiva, Inc'
for filename1 in os.listdir(directory1):
    file_path1 = os.path.join(directory1, filename1)
    try:
        if os.path.isfile(file_path1) or os.path.islink(file_path1):
            os.unlink(file_path1)
        elif os.path.isdir(file_path1):
            shutil.rmtree(file_path1)
    except Exception as e:
        print()

directory2 = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Nextiva, Inc/Nextiva App'
for filename2 in os.listdir(directory2):
    file_path2 = os.path.join(directory2, filename2)
    try:
        if os.path.isfile(file_path2) or os.path.islink(file_path2):
            os.unlink(file_path2)
        elif os.path.isdir(file_path2):
            shutil.rmtree(file_path2)
    except Exception as e:
        print()

try:
    os.remove(r'C:/Users/Public/Public Desktop/Nextiva App.lnk')
except FileNotFoundError:
    pass

#this is running the command and then is converting it into string
output = sp.run(["findstr", "/R", "/S", "[a-z]*Nextiva", "C:\Windows\Installer\*.msi"], stdout=sp.PIPE)
strOutput = output.stdout.decode('utf-8', 'ignore')
#this finds all the msi files, Problem.. I get duplicates.
temp = re.compile('.+msi')
strOutputTrim = temp.findall(strOutput)
strStripped = set(strOutputTrim) # this is going to remove duplicates
for i in strStripped:   # for loop to iterate through all items in set and have them display the path needed seperate.
    neededPath = i
    os.remove(neededPath) # delete not uninstall msi.
    time.sleep(5)

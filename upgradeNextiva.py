import subprocess

path = '"C:\Users\gbeltran\Downloads\NextivaApp.bc-uc.win-22.9.31.119.msi"'
command = "msiexec /i "+ path + " /qn"
subprocess.Popen(command, shell=True)
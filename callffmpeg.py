import sys
import os
import subprocess
'''
for i in range(20):
    try:
        print(sys.argv[i])
    except:
        print("error")
'''
if sys.argv[3] == "-vn":
    #print("VNNNNNNNNNNNNNNNNNNNN")
    cmd = ["C:/ffmpeg/bin/ffmpeg.exe", "-ss", sys.argv[5], "-t", sys.argv[7], "-i", sys.argv[2], "-vn", "-acodec", "aac", "-ab", "192k", os.getcwd() + "/" + sys.argv[10]]
    #print(cmd)
    subprocess.call(cmd, shell=True)
else:
    cmd = ["C:/ffmpeg/bin/ffmpeg.exe", "-i", os.getcwd() + "/" + sys.argv[2], "-i", os.getcwd() + "/" + sys.argv[4], "-vcodec", "copy", "-acodec", "copy", os.getcwd() + "/" + sys.argv[9]]
    #print(cmd)
    subprocess.call(cmd, shell=True)
#input("Press Enter to continue...")
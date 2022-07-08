# please move downloadfirebase.py file at folder *.md files(exported from Roam research) are located at .
# downloadfirebase.py을 Roam에서 추출하 *.md 파일이 있는 폴더에 넣어주세요.

# cmd/terminal에서 ">python3 downloadfirebase.py" 입력 

#-*-coding:utf-8 -*-
import re
import glob
import os
import requests
import calendar
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.'+directory)


createFolder('./target')
createFolder('./target/assets')

vaultDir = os.path.dirname(os.path.realpath(__file__))
NewvaultDir = './target'
firebaseShort = 'none'
fullRead = 'none'
fileFullPath = ''
fullTempFilePath = ''
i = 0
ext = ''


# Walk through all files in all directories within the specified vault directory
for subdir, dirs, files in os.walk(vaultDir):
    for file in files:
        if file != 'downloadfirebase.py':
            # Open file in directory
            fileFullPath = os.path.join(subdir,file)
            fhand = open(fileFullPath, errors='ignore')
            for line in fhand:
                # Download the Firebase file and save it in the assets folder
                if 'firebasestorage' in line:
                    try:
                        # If it's a PDF, it will be in the format {{pdf: link}}
                        if '{{pdf:' in line:
                            link = re.search(r'https://firebasestorage(.*)\?alt(.*)\}', line)
                        else:
                            link = re.search(r'https://firebasestorage(.*)\?alt(.*)\)', line)
                        firebaseShort = 'https://firebasestorage' + link.group(1) # https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FDownloadMyBrain%2FLy4Wel-rjk.png
                        firebaseUrl = link.group(0)[:-1] # https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FDownloadMyBrain%2FLy4Wel-rjk.png?alt=media&token=0fbafc8f-0a47-4720-9e68-88f70803ced6
                        # Download the file locally
                        r = requests.get(firebaseUrl)
                        timestamp = calendar.timegm(time.gmtime())
                        # Get file extension of file. Ex: .png; .jpeg
                        reg = re.search(r'(.*)\.(.+)', firebaseShort[-5:]) # a.png / .jpeg
                        ext = '.' + reg.group(2) # .jpe
                        # Create assets folder if it doesn't exist
                        if not os.path.exists(NewvaultDir + '/assets'):
                            os.makedirs(NewvaultDir + '/assets')
                        # Create new local file out of downloaded firebase file
                        newFilePath = 'assets/' + str(timestamp) + '_' + str(i) + ext
                        # print(firebaseUrl + '>>>' + newFilePath)
                        with open(NewvaultDir + '/' + newFilePath,'wb') as output_file:
                            output_file.write(r.content)
                    except AttributeError: # This is to prevent the AttributeError exception when no matches are returned
                        continue
                    # Save Markdown file with new local file link as a temp file
                    # If there is already a temp version of a file, open that.
                    fullTempFilePath = NewvaultDir + '/' + file
                    NewFilePath = NewvaultDir + file
                    if os.path.exists(fullTempFilePath):
                        fullRead = open(fullTempFilePath, errors='ignore',encoding='utf-8')
                    else:
                        fullRead = open(fileFullPath, errors='ignore',encoding='utf-8')
                    data = fullRead.read()
                    data = data.replace(firebaseUrl,newFilePath)
                    with open(fullTempFilePath,'wt',encoding='utf-8') as temp_file:
                        temp_file.write(data)
                        i = i + 1
                    
                    #if os.path.exists(fullTempFilePath):
                    #    path = os.replace(fullTempFilePath,fileFullPath)
                    fullRead.close()
            # Close file
            fhand.close()

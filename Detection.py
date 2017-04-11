
import os
import re
path=input("Give the path to the Place where Chrome extension you want to check is present:-\n")
#print(path)
a=os.listdir(path) #a stores all the file name in the given directory
# print(a)
files=[] #file names and their path for analysing there javascript files.
textfiles=[] # file names and their path for analysing if they contain email content
# here we are checking if there is some email content stored on your harddisk
email_content=input("Give the content of one of your email:-\n") #takes the content of your email
counter=0;
# following for loop checks for email content in the files of extension
for i in a:
    if i.find('.txt')>0 or i.find('.csv')>=0 or i.find('html')>=0:
        textfiles.append(path+ '\\'+ i) #textfiles now contain full file names
        myfile=open(textfiles[counter],'r') #opens file in read mode
        counter=counter+1
        mytext=myfile.read()#mytext varaible of type string stores whole of the text file
        if mytext.find(email_content)>=0:
            print('Extension is malicious for sure.Do not use it.')
            break
    
#following for loop stores file names of javascript in files list
for i in a:
    if i.find("manifest.json")==-1 and i.find(".js")!=-1:
        files.append(path+ '\\'+ i) #javascript file directory are appended in files list
        #print(path+i)




'''
for i in files:
    print(i);
'''
htmlcount=0
updatecount=0
for i in files:
    fileobj=open(i,'r')
    text=fileobj.read()
    #print(text)
    #print("\n \n")
    if (text.find('document.body.innerHTML')>=0 or text.find('document.body.outerHTML')>=0) and (text.find("@gmail.com")>=0 or text.find("mailed-by:")>=0 or text.find("subject:")>=0):
        htmlcount+=1
    if(text.find("chrome.tabs.update")>=0 and text.find("https://mail.google.com")):
        updatecount+=1
        print(text)
if htmlcount>0:
    print(str(htmlcount) + " Files can read your email through content script.They are suspicious")
if updatecount>0:
    print(str(updatecount) + " Files check your tabs for gmail url.They are suspicious")

if htmlcount==0 and updatecount==0:
    print("Extension may not be doing email spying")

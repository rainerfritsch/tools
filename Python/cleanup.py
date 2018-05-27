import os

# config
baseDirectory = "/home/rainer/"
downloadDirectory = baseDirectory + "Downloads/"
documentDirectory = baseDirectory + "Downloads/Documents/"
pictureDirectory = baseDirectory + "Downloads/Pictures/"
installationDirectory= baseDirectory + "Downloads/Installationfiles/"
musicDirectory = baseDirectory + "Downloads/Music/"
videoDirectory = baseDirectory + "Downloads/Videos/"

# files ending with this ending fall into that category
txtfiles=".txt,.doc,.pdf,.xlsx"
musicfiles=".mp3"
installationfiles=".zip,.dmg,.tar.gz,.tar.bz2,.iso,.exe"
videofiles=".mp4"

# decide if file ends with given fileending
def kindOf(filename, endings):
    isKindOf=0
    aendings=endings.split(",")
    for ending in aendings:
        if filename.endswith(ending):
            isKindOf=isKindOf+1
    #if filename ends with certain filending return true
    return (isKindOf>0)

# create needed directories
#def init()



for filename in os.listdir(downloadDirectory):
    if (kindOf(filename,txtfiles)):
        print ("*Textfile found * "+filename)
        os.rename(downloadDirectory+filename,documentDirectory+filename)
    if (kindOf(filename,musicfiles)):
        print ("*Music found * "+filename)
        os.rename(downloadDirectory+filename,musicDirectory+filename)
    if (kindOf(filename,installationfiles)):
        print ("*Installation file found * "+filename)
        os.rename(downloadDirectory+filename,installationDirectory+filename)
    if (kindOf(filename,videofiles)):
        print ("*Video file found * "+filename)
        os.rename(downloadDirectory+filename,videoDirectory+filename)

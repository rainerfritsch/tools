import os
from pathlib import Path


# config
baseDirectory = str(Path.home())+"/"
downloadDirectory = baseDirectory + "Downloads/"
documentDirectory = downloadDirectory + "_Documents/"
pictureDirectory = downloadDirectory + "_Pictures/"
installationDirectory= downloadDirectory + "_Installationfiles/"
musicDirectory = downloadDirectory + "_Music/"
videoDirectory = downloadDirectory + "_Videos/"
archiveDirectory = downloadDirectory + "_Archive/"

# files ending with this ending fall into that category
txtfiles=".txt,.doc,.pdf,.xlsx"
musicfiles=".mp3,.wav"
installationfiles=".dmg,.iso,.exe"
videofiles=".mp4"
picturefiles=".jpg,.jpeg,.png"
archivefiles=".zip,.tar,.gz,.bz2"

# decide if file ends with given fileending
def kindOf(filename, endings):
    isKindOf=0
    aendings=endings.split(",")
    for ending in aendings:
        if filename.endswith(ending):
            isKindOf=isKindOf+1
    #if filename ends with certain filending return true
    return (isKindOf>0)

# create folders if nessesary
def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
                os.makedirs(dir)

def check():
    assure_path_exists(documentDirectory)
    assure_path_exists(pictureDirectory)
    assure_path_exists(installationDirectory)
    assure_path_exists(musicDirectory)
    assure_path_exists(videoDirectory)
    assure_path_exists(archiveDirectory)

# let´s go
def main():
    check()
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
        if (kindOf(filename,picturefiles)):
            print ("*Picture file found * "+filename)
            os.rename(downloadDirectory+filename,pictureDirectory+filename)
        if (kindOf(filename,archivefiles)):
            print ("*Picture file found * "+filename)
            os.rename(downloadDirectory+filename,archiveDirectory+filename)

if __name__ == "__main__":
    main()

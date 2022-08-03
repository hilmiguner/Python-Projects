import os

result = dir(os)
print(result)

print(50*"*")

# "os.name" gives name of the operator system which are you using.
print("Operator System:", os.name)

print(50*"*")

# "os.getcwd()" returns current work directory of the .py file.
print("Current Directory:", os.getcwd())

print(50*"*")

# "os.mkdir(String folderName)" creates a new folder in the current directory which is "os.getcwd()".
# If folder already exists, compiler gives error so we call this function in try-catch.
try:
    os.mkdir("newFolder")
    print("File is successfully created")
except FileExistsError:
    print("The folder which you want to create is already exists.")

print(50 * "*")

# "os.chdir(String path)" gets a path and changes the current work directory into the that path.
os.chdir("newFolder")
print("Current Directory:", os.getcwd())
try:
    os.mkdir("newFolder1")
    print("File is successfully created")
except FileExistsError:
    print("The folder which you want to create is already exists.")

print(50*"*")

# Parameter of ".." means in "os.chdir("..")" go to upper directory.
# You can use ".." few times in one function.
print("Current Directory:", os.getcwd())
os.chdir("..")
print('New Directory after "..":', os.getcwd())
os.chdir("../..")
print('New Directory after "../..":', os.getcwd())

os.chdir("Python/Module OS")

print(50*"*")

# With "os.makedirs(String path)" we can create intertwined folders.
try:
    os.makedirs("newFolder1/newFolderInNewFolder")
    print("Files are successfully created")
except FileExistsError:
    print("The folders which you want to create are already exists.")

print(50*"*")

# "os.listdir()" lists the current directory folders and files.
# Function's default parameter is current directory, but it can take any path.
currentDirList = os.listdir()
print("Current Directory List:", currentDirList)

dirList = os.listdir("C:/Users/Casper/Desktop")
print('List of "C:\\Users\\Casper\\Desktop":', dirList)

print(50*"*")

# How to filter the list ?
# Let's say we want .py files:
for file in currentDirList:
    if file.endswith(".py"):
        print(".py file:", file)

print(50*"*")

# "os.stat(String file)" gives information about the file which is parameter as a string.
info = os.stat("main.py")
print("Information about main.py:", info)

sizeOfFile = os.stat("main.py").st_size  # .st_size is a size value as bytes.
print("Size of the file as BYTES:", sizeOfFile)
print("Size of the file as KILOBYTES:", sizeOfFile/1024)

print(50*"*")

# Let's import datetime.
from datetime import datetime
timePassedSinceCreated = os.stat("main.py").st_ctime  # .st_ctime is time that passed since file is created.
print("Time passed since file is created:", timePassedSinceCreated)
createdDate = datetime.fromtimestamp(timePassedSinceCreated)
print("Date that when file is created:", createdDate)

print(50*"*")

timePassedSinceLastAccess = os.stat("main.py").st_atime  # .st_atime is time that passed since last access.
print("Time passed since file is last accessed:", timePassedSinceLastAccess)
lastAccessedDate = datetime.fromtimestamp(timePassedSinceLastAccess)
print("Date that when file is last accessed:", lastAccessedDate)

print(50*"*")

timePassedSinceModified = os.stat("main.py").st_mtime  # .st_mtime is time that passed since last modify.
print("Time passed since file is modified:", timePassedSinceModified)
modifiedDate = datetime.fromtimestamp(timePassedSinceModified)
print("Date that when file is modified:", modifiedDate)

print(50*"*")

# With "os.system(String command)", we can execute any command in a subshell.
# os.system("notepad.exe")

# "os.rename(String currentName, String newName)" changes a file or folder name.
try:
    os.rename("newFolder", "changedName")
    print("Name is successfully changed.")
except FileExistsError:
    print("There is already desired name of a folder.")

print(50*"*")

# "os.rmdir(String path)" and "os.removedirs(String path)" are for removing folder or files.
# "os.rmdir(String path)" only removes the path.
# "os.removedirs(String path)" removes all the way to the path.
os.mkdir("forRemoving")
print("Before removing:", os.listdir())
os.rmdir("forRemoving")
print("After removing:", os.listdir())

os.removedirs("newFolder1/newFolderInNewFolder")  # Removes "newFolderInNewFolder" and "newFolder1".

print(50*"*")

# "os.path.abspath(String fileName)" gives the full path of the file from hdd's or ssd's.
fullPath = os.path.abspath("main.py")
print('Full Path of "main.py":', fullPath)

print(50*"*")

# "os.path.dirname(String pathfOfFile)" gives the directory of a file from a full path.
dirOfFile = os.path.dirname(fullPath)
print('Directory of "main.py":', dirOfFile)

# If you want to know a directory of a file without knowing the full path of the file,
# you can use two functions in the same time.

print(50*"*")

dirOfFile = os.path.dirname(os.path.abspath("main.py"))
print('Directory of "main.py":', dirOfFile)

print(50*"*")

# "os.path.exists(String fileOrFolder)" checks if there is a file or folder which you want to know.
isFileExists = os.path.exists("main.py")  # Returns true.
print('Is "main.py" exists ?', isFileExists)
isFileExists = os.path.exists("main123.py")
print('Is "main123.py" exists ?', isFileExists)  # Returns false.

isFolderExists = os.path.exists("newFolder")  # Returns true.
print('Is "newFolder" exists ?', isFolderExists)
isFolderExists = os.path.exists("newFolder1")  # Returns false.
print('Is "newFolder1" exists ?', isFolderExists)

print(50*"*")

# "os.path.join(...)" takes strings and make a path with them but does NOT create the path.
pathMade = os.path.join("C:\\", "newFolder", "newFolder1")
print("The path that is made:", pathMade)

print(50*"*")

# "os.path.split(String path)" takes a path and returns a list which has pieces of the path.
list1 = os.path.split(pathMade)
print("Pieces of the path:", list1)

print(50*"*")

# "os.path.splitext(String fileName)" splits the name and extension of the file.
piecesOfFile = os.path.splitext("main.py")
print('Pieces of "main.py":', piecesOfFile)

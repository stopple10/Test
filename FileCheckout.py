# Create Executable File with pyinstaller --onefile Filename.py

import os
import datetime
import csv
from shutil import copyfile
import tkinter as Tk
from tkinter.filedialog import askopenfilename

def get_user_input():
    user[0] = (name.get())
    dialogbox.destroy()

ext = '.csv'
user = ['']
dialogbox = Tk.Tk()
Tk.Label(dialogbox, text="Name").grid(row=0)

name = Tk.Entry(dialogbox)
name.grid(row=0, column=1)

Tk.Button(dialogbox, text='Quit', 
          command=dialogbox.quit).grid(row=3, column=0, sticky=Tk.W, pady=4)
Tk.Button(dialogbox, text='Enter', 
          command=get_user_input).grid(row=3, column=1, sticky=Tk.W, pady=4)

Tk.mainloop()
if user[0] != '':
    # Go through entire directory and make all files visible 
    rootdir = 'S:/Machine Version Library/VersionControlLibrary'
    filenames = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filenames.append(os.path.join(subdir, file))
            p = os.popen('attrib -h ' + os.path.join(subdir, file))
            p.close()
    #print(filenames)
    
    Tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(initialdir=rootdir,
                               filetypes=[("Logix Designer Project", ".ACD")])
    
    # Copy file to root directory and add log entry
    splitpath = os.path.split(filename)
    subfolder = os.path.split(splitpath[0])[1]
    mainpath = os.path.split(rootdir)
    print(splitpath, subfolder, mainpath)
    if subfolder == mainpath[1] or os.path.split(splitpath[0])[0] != (mainpath[0] + '/' + mainpath[1]):
        subfolder == ''
        print("Incorrect File and/or Folder")
    else:
        # Add log entry to that specific folder
        user.append(splitpath[1].strip(ext))
        now = datetime.datetime.now()
        currentDate = now.strftime("%m/%d/%y")
        currentTime = now.strftime("%I:%M %p")
        user.append(currentDate)
        user.append(currentTime)
        with open(splitpath[0] + '/' 'Log.csv', 'a', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(user)
            print(user)
        #Copy File For User
        print(subfolder, splitpath)
        copyfile(filename, splitpath[1])
    
    # Hide all important files again
    for file in filenames:
        if file.rfind(ext) == -1:
            p = os.popen('attrib +h ' + file)
            p.close()
else:
    print("Operation Quit")
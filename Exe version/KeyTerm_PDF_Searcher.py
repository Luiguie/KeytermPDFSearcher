# import packages
from email import message
import PyPDF2
import re
import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

chosenFile = ""
def BrowseFile():
    global chosenFile 
    chosenFile = filedialog.askdirectory()
    #label_file_explorer.configure(text="Chosen File: " + chosenFile)

def aa(cf):
    # returns all file paths that has .pdf as extension in the specified directory
    print(cf)
    pdf_search = Path("%s" %(cf)).glob("*.pdf")
    # convert the glob generator out put to list
    # skip this if you are comfortable with generators and pathlib
    pdf_files = [str(file.absolute()) for file in pdf_search]
    message = "Your files:", pdf_files
    tx.insert('end', message)
    #print("Seus arquivos sao:", pdf_files)
    #define keyterms
    #key_term = input("Please insert keyterm (Be specific)\n")
    global eDir
    key_term = eDir.get()
    for pdf in pdf_files:    
        # open the pdf file
        object = PyPDF2.PdfFileReader("%s" %(pdf))
            
        print(pdf)
        slen = len(pdf)
        print(slen)
        for i in range((slen-1),0, -1):
            if pdf[i] == "\\":
                message = "\n" + pdf[i:slen] +"\n"
                tx.insert('end', message)
                break
        # get number of pages
        NumPages = object.getNumPages()
        tx.insert('end', message)
        # extract text and do the search
        for i in range(0, NumPages):
            PageObj = object.getPage(i)
            message = "Current Page: " + str(i+1) +"\n"
            tx.insert('end', message)
                #print("Current Page: " + str(i+1) ) 
            pdfText = PageObj.extractText() 
            ResSearch = re.search(key_term, pdfText)
                # Displays whether or not the keyterm was found
            if ResSearch == None:
                message = "Not Found\n"
                tx.insert('end', message)                    
            else:
                message = "Keyterm Found\n"
                tx.insert('end', message)

# window instance and config
wd = Tk()
wd.title("KeyTerm PDF Searcher by Luiguie")
wd.geometry("800x450")
tx = Text(wd, height=40, width=50)
tx.pack(expand=True)
tx.pack(padx=0, pady=0, side=tk.LEFT)
scrollbar = ttk.Scrollbar(
    wd,
    orient='vertical',
    command=tx.yview
)
scrollbar.pack(padx=0, pady=0, side=tk.LEFT)
bOpen = Button(wd, text = "Select Folder", command = BrowseFile)
#bOpen.grid(column = 10, row = 20)
bOpen.pack(padx=5, pady=200, side=tk.RIGHT)
bSearch = Button(wd, text = "➢", command= lambda:aa(chosenFile))
bSearch.pack(padx=5, pady=200, side=tk.RIGHT)
eDir = Entry(wd, bd=5)
eDir.pack(padx=5, pady=200, side=tk.RIGHT)

tk.mainloop()







        

    

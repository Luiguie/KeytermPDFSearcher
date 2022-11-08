# import packages
import PyPDF2
import re
import webbrowser
import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

chosenFile = ""
foundPDFList = []
def openPDFs():
    for pdf in foundPDFList:
        webbrowser.open_new(pdf)
    
def MyGithub():
    webbrowser.open("https://github.com/Luiguie", new=1)

def BrowseFile():
    tx.config(state=NORMAL)
    tx.delete(1.0, "end")
    global chosenFile 
    chosenFile = filedialog.askdirectory()
    tx.insert("end", "Sua pasta é: \n" + chosenFile + "\n")
    tx.config(state=DISABLED)

def aa(cf):
    tx.config(state=NORMAL)
    tx.delete(1.0, "end")
    tx.insert("end", "Sua pasta é: \n" + chosenFile + "\n")
    # returns all file paths that has .pdf as extension in the specified directory
    pdf_search = Path("%s" %(cf)).glob("*.pdf")
    # convert the glob generator output to list
    pdf_files = [str(file.absolute()) for file in pdf_search]
    global KT
    key_term = KT.get()
    emptyPDF_Results = True
    logs = ""
    for pdf in pdf_files:    
        # open the pdf file
        object = PyPDF2.PdfFileReader("%s" %(pdf))
        slen = len(pdf)
        for i in range((slen-1),0, -1):
            if pdf[i] == "\\":
                mInfo = "\n" + pdf[(i+1):slen] +"\n"
                break
        # get number of pages
        NumPages = object.getNumPages()
        mPage = " "
        
        # extract text and do the search
        for i in range(0, NumPages):
            PageObj = object.getPage(i)      
            pdfText = PageObj.extractText() 
            pdfText = pdfText.lower()
            key_term = key_term.lower()
            ResSearch = re.search(key_term, pdfText)
                # Displays whether or not the keyterm was found
            pdfCheck = False
            if ResSearch != None:
                pdfCheck = True
                if i == 0:
                    mPage += str(i+1)
                elif i<(NumPages-1):
                    mPage += ", " + str(i+1)
                else:
                    if mPage == " ":
                        mPage += str(i+1)    
                    else:
                        mPage += " e " + str(i+1)  
                        
        if pdfCheck == True:
            emptyPDF_Results = False
            message = mInfo + "Palavra chave encontrada na(s) pagina(s):" + mPage + "\n"
            logs += message
            tx.insert('end', message)
            foundPDFList.append(pdf)
            print(foundPDFList)
            pdfOpen.config(state=NORMAL)
        else:
            logs += mInfo + "Palavra chave não encontrada no PDF" + "\n"
    if emptyPDF_Results == True:
        tx.insert("end", "\nPalavra chave não encontrada na pasta escolhida")
        pdfOpen.config(state=DISABLED)
    
    tx.insert("end", "\n\n\n\n#######################\nHistorico completo:\n" + logs)
    tx.config(state=DISABLED)



# window instance and config
wd = Tk()
wd.title("KeyTerm PDF Searcher by Luiguie")
wd.geometry("800x450")
#wd.resizable(0,0)
bOpen = Button(wd, text = "Selecionar pasta", command = BrowseFile)
bOpen.grid(row=12,column=0, sticky="sw")

KT = Entry(wd, bd=5)
KT.grid(row=13,column=0, sticky="n")
bSearch = Button(wd, text = "➢", command= lambda:aa(chosenFile))
bSearch.grid(row=13,column=1, sticky="n")
credits = Button(wd, text = "Made By Luiguie", command= MyGithub)
credits.grid(row=20,column=0, sticky="sw")

tx = Text(wd, height=25, width=48)
tx.grid(row=2, column=2, padx=(200,0), rowspan=20, columnspan=10)
tx.config(state=DISABLED)
scrollbar = ttk.Scrollbar(
    wd,
    orient='vertical',
    command=tx.yview, 
)
scrollbar.grid(row=2, column=25, rowspan=20 ,sticky="ns")

pdfOpen = Button(wd, text = "Abrir PDFs encontrados", command= openPDFs, state=DISABLED)
pdfOpen.grid(row=25,column=9)


tk.mainloop()
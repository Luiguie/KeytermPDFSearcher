# import packages
import PyPDF2
import re
from pathlib import Path

p = input("Please insert the folder directory \n")

# returns all file paths that has .pdf as extension in the specified directory
pdf_search = Path("%s" %(p)).glob("*.pdf")
# convert the glob generator out put to list
# skip this if you are comfortable with generators and pathlib
pdf_files = [str(file.absolute()) for file in pdf_search]
print("Seus arquivos sao:", pdf_files)

# define keyterms
key_term = input("Please insert keyterm (Be specific)\n")

for pdf in pdf_files:    
    # open the pdf file
    object = PyPDF2.PdfFileReader("%s" %(pdf))
    
    print(pdf)

    # get number of pages
    NumPages = object.getNumPages()

    # extract text and do the search
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        print("Current Page: " + str(i+1) ) 
        pdfText = PageObj.extractText() 
        ResSearch = re.search(key_term, pdfText)
        # Displays whether or not the keyterm was found
        if ResSearch == None:
            print("Not Found")
            
        else:
            print("Keyterm Found")
        
    
    

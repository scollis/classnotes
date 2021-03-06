import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk pde*/*.pdf output ~/Dropbox/Public/skfiles/pde.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("pde*")):
        os.chdir(a)
        os.system("pdflatex -shell-escape pde*.tex")    
        os.chdir("..")
    
    

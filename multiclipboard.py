#! python3
# Saves and loads pieces of text to the clipboard
"""
Instructions:
1- Save this file as a pyw (No console python)
2- Create a bat file containing @pyw.exe C:\Python34\mcb.pyw %*
3- add the folder containing the pyw, the bat file and the shelve files to Path variables
2- Verify the default py version has installed the pyperclip module

"""
# Usage: 
# py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip
import shelve
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv)
elif len(sys.argv) == 2:

# List of Keywords and load contents
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv)
else:
    print(sys.argv)
    print(sys.version)
mcbShelf.close()




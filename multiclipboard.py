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
# py.exe mcb.pyw delete <keyword> - delete the keyword and its content
# py.exe mcb.pyw deleteall - deletes all keywords.


import pyperclip
import shelve
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete only the selected keyword
    elif sys.argv[1].lower == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
# List of Keywords and load contents
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
# Delete all Keywords saved
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.keys().delete()
# Save clipboard to keyword
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv)
mcbShelf.close()




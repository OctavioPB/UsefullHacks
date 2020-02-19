#! python3
# mapit.py - Launches a map in the browser using an address from the command line
# bat file = @py.exe C:\Users\user\Documents\Experiments\mapit.py %*

#USAGE:
# 1- From run call mapit
# 2- Either:
    # a- write the address in the run window
    # b- copy the address and mapit will take it from clipboard
    
import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])
    # TODO Get address from the clipboard
else:
    # Get address from the clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

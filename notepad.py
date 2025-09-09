from tkinter.filedialog import *
import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox


canvas = tk.Tk()
canvas.geometry("400x600") # window size
canvas.title("Notepad") # window title
canvas.config(bg = "#f0f4f9") # background color

top = tk.Frame(canvas) # create container
top.pack(padx = 10, pady = 5, anchor = "nw") # give padding and set it to topleft

# Functions
def saveFile():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")]) # sets deafult filetype to .txt
    if not file_path:
        return
    text = str(entry.get(1.0, "end")) # get text from notepad
    with open(file_path, "w") as file:
        file.write(text) # write text from notepad to new file

def openFile():
    file = askopenfile(mode = "r", filetypes = [("Text Files", "*.txt")]) # mode = read, sets default file type to *.txt
    if file != None:
        content = file.read() # reads file content
    entry.delete("1.0", "end")  # clear current text before inserting
    entry.insert("insert", content) # adds text from file to notepad

def clearFile():
    confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all text?")
    if confirm:
        entry.delete(1.0, "end") # deletes text from start to end from notepad

def searchWord():
    entry.tag_remove("highlight", "1.0", "end")  # clear old highlights
    word = searchEntry.get() # get word from search entry
    if word: # if word is not empty
        start_pos = "1.0" # start from the beginning of the text
        while True: # loop to find all occurrences
            start_pos = entry.search(word, start_pos, stopindex="end", nocase=1) # search for word, nocase=1 makes it case insensitive
            if not start_pos: 
                break  # if no more occurrences, break loop
            end_pos = f"{start_pos}+{len(word)}c"  # calculate end position of the found word
            entry.tag_add("highlight", start_pos, end_pos) # highlight the found word
            start_pos = end_pos # move to the end of the found word for next search
        entry.tag_config("highlight", background="yellow", foreground="black") # configure highlight tag with background and foreground color

def clearSearch():
    entry.tag_remove("highlight", "1.0", "end")
    searchEntry.delete(0, "end")

# Buttons
openButton = tk.Button(canvas, text="Open", bg="White", command= openFile) # Button with text Open and background color white
openButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

saveButton = tk.Button(canvas, text="Save", bg="White", command= saveFile) # Button with text Save and background color white
saveButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

clearButton = tk.Button(canvas, text="Clear", bg="White", command= clearFile) # Button with text Clear and background color white
clearButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

exitButton = tk.Button(canvas, text="Exit", bg="White", command= exit) # Button with text Exit and background color white
exitButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

searchEntry = tk.Entry(top, width=15)  # Entry widget for search input with width of 15 characters
searchEntry.pack(side="left", padx=5)   # moves entry to the left, adds padding and adds it to "top" container

searchButton = tk.Button(top, text="Search", bg="White", command=searchWord) # Button with text Search and background color white
searchButton.pack(side="left") # moves button to the left and adds it to "top" container

clearSearchButton = tk.Button(top, text="✕", bg="White", command=clearSearch) # Button with text Clear and background color white
clearSearchButton.pack(side="left") # moves button to the left and adds it to "top" container

# Text Area
entry = tk.Text(canvas, wrap = "word", bg = "White", font = ("Arial", 15)) # text area, wraps word when on edge, background color, font and fontsize
entry.pack(padx = 10, pady = 5, expand="true", fill="both") # pack with padding, expands with window, fills both x and y

# Main
canvas.mainloop() # runs canvas
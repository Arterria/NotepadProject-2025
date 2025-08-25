from tkinter.filedialog import *
import tkinter as tk

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
    entry.delete(1.0, "end") # deletes text from start to end from notepad

# Buttons
openButton = tk.Button(canvas, text="Open", bg="White", command= openFile) # Button with text Open and background color white
openButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

saveButton = tk.Button(canvas, text="Save", bg="White", command= saveFile) # Button with text Save and background color white
saveButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

clearButton = tk.Button(canvas, text="Clear", bg="White", command= clearFile) # Button with text Clear and background color white
clearButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

exitButton = tk.Button(canvas, text="Exit", bg="White", command= exit) # Button with text Save and background color white
exitButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

# Text Area
entry = tk.Text(canvas, wrap = "word", bg = "White", font = ("Arial", 15)) # text area, wraps word when on edge, background color, font and fontsize
entry.pack(padx = 10, pady = 5, expand="true", fill="both") # pack with padding, expands with window, fills both x and y

# Main
canvas.mainloop() # runs canvas
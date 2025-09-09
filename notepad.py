from tkinter.filedialog import *
import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import tkinter.font as tkFont
import tkinter.colorchooser as colorchooser


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

def openSearchWindow():
    search_win = tk.Toplevel(canvas)
    search_win.title("Search")
    search_win.geometry("300x120")
    search_win.config(bg="#f0f4f9")
    search_win.transient(canvas)

    tk.Label(search_win, text="Enter word to search:", bg="#f0f4f9").pack(pady=(10, 0))
    search_var = tk.StringVar()
    searchEntry = tk.Entry(search_win, textvariable=search_var, width=30)
    searchEntry.pack(pady=5)

    def search():
        word = search_var.get()
        entry.tag_remove("highlight", "1.0", "end")
        if word:
            start_pos = "1.0"
            while True:
                start_pos = entry.search(word, start_pos, stopindex="end", nocase=1)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                entry.tag_add("highlight", start_pos, end_pos)
                start_pos = end_pos
            entry.tag_config("highlight", background="yellow", foreground="black")

    def clear():
        entry.tag_remove("highlight", "1.0", "end")
        search_var.set("")

    button_frame = tk.Frame(search_win, bg="#f0f4f9")
    button_frame.pack(pady=10)

    search_btn = tk.Button(button_frame, text="Search", command=search, bg="white")
    search_btn.pack(side="left", padx=5)

    clear_btn = tk.Button(button_frame, text="Clear", command=clear, bg="white")
    clear_btn.pack(side="left", padx=5)

def openSettings():
    settings_win = tk.Toplevel(canvas) # create window
    settings_win.title("Settings") # window title
    settings_win.geometry("300x250") # window size
    settings_win.config(bg="#f0f4f9") # background color set to #f0f4f9
    settings_win.transient(canvas) # keeps setting window above main notepad
    settings_win.grab_set() # makes it so you can't use notepad unless you close settings window

    # Current font settings
    current_font = tkFont.Font(font=entry["font"])
    current_family = current_font.actual("family")
    current_size = current_font.actual("size")

    # Font Family Dropdown
    tk.Label(settings_win, text="Font Family:", bg="#f0f4f9").pack(pady=(10, 0))
    font_family_var = tk.StringVar(value=current_family)
    font_families = list(tkFont.families())
    font_family_menu = tk.OptionMenu(settings_win, font_family_var, *sorted(font_families))
    font_family_menu.pack()

    # Font Size Spinbox
    tk.Label(settings_win, text="Font Size:", bg="#f0f4f9").pack(pady=(10, 0))
    font_size_var = tk.IntVar(value=current_size)
    font_size_spin = tk.Spinbox(settings_win, from_=8, to=72, textvariable=font_size_var)
    font_size_spin.pack()

    # Background Color Picker
    tk.Label(settings_win, text="Background Color:", bg="#f0f4f9").pack(pady=(10, 0))
    bg_color_var = tk.StringVar(value=entry["bg"])

    color_frame = tk.Frame(settings_win, bg="#f0f4f9")
    color_frame.pack(pady=5)

    bg_color_preview = tk.Label(color_frame, bg=bg_color_var.get(), width=3, height=1, relief="sunken", bd=1)
    bg_color_preview.pack(side="right", padx=(10, 0))

    def chooseColorWrapper():
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            bg_color_var.set(color)
            bg_color_preview.config(bg=color)

    bg_color_button = tk.Button(color_frame, text="Choose Color", command=chooseColorWrapper)
    bg_color_button.pack(side="left")

    # Apply Button
    apply_button = tk.Button(settings_win, text="Apply", bg="#f0f4f9", command=lambda: applySettings(font_family_var.get(), font_size_var.get(), bg_color_var.get(), settings_win))
    apply_button.pack(pady=10)

def chooseColor(bg_color_var):
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        bg_color_var.set(color)

def applySettings(font_family, font_size, bg_color, settings_win):
    try:
        entry.config(font=(font_family, int(font_size)), bg=bg_color)
        settings_win.destroy()  # Close the settings window after applying
    except Exception as e:
        messagebox.showerror("Error", f"Failed to apply settings:\n{e}")

# Buttons
openButton = tk.Button(canvas, text="Open", bg="White", command= openFile) # Button with text Open and background color white
openButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

saveButton = tk.Button(canvas, text="Save", bg="White", command= saveFile) # Button with text Save and background color white
saveButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

clearButton = tk.Button(canvas, text="Clear", bg="White", command= clearFile) # Button with text Clear and background color white
clearButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

settingsButton = tk.Button(canvas, text="Settings", bg="White", command= openSettings) # Button with text Settings and background color white
settingsButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container

searchWindowButton = tk.Button(canvas, text="Search", bg="White", command= openSearchWindow) # Button with text Search and background color white
searchWindowButton.pack(in_=top, side="left") # moves button to the left and adds it to "top" container

exitButton = tk.Button(canvas, text="Exit", bg="White", command= exit) # Button with text Exit and background color white
exitButton.pack(in_ = top, side="left") # moves button to the left and adds it to "top" container



# Text Area
entry = tk.Text(canvas, wrap = "word", bg = "White", font = ("Arial", 15)) # text area, wraps word when on edge, background color, font and fontsize
entry.pack(padx = 10, pady = 5, expand="true", fill="both") # pack with padding, expands with window, fills both x and y

# Main
canvas.mainloop() # runs canvas
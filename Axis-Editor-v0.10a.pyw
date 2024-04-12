# Axis-Editor - v0.10a
# Designed and Coded by: WevOppy


# ===== Imports ============ #
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# ===== Variables ========== #



# ===== Functions ========== #
# File
def newFile():
    txtEdit.delete("1.0", tk.END)
    
def openFile():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txtEdit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txtEdit.insert(tk.END, text)
    root.title(f"Text-Editor: {filepath}")
    
def saveFile():
    x = 0
    
def saveAs():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txtEdit.get("1.0", tk.END)
        output_file.write(text)
    root.title(f"Text-Editor: {filepath}")
    

# Settings
def preferences():
    x = 0
    
def styleConfig():
    x = 0


# ===== Main =============== #
# ----- Setup -------------- #
root = tk.Tk()
root.title('Axis-Editor - v0.10a')
root.iconbitmap("Axis-Editor-Icon.ico")

# ----- Menu-Bar ----------- #
menubar = tk.Menu(root)
fileMenu = tk.Menu(menubar, tearoff=0)
settingsMenu = tk.Menu(menubar, tearoff=0)

# File
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=newFile)
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_command(label='Save As...', command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.destroy)

# Settings
menubar.add_cascade(label='Settings', menu=settingsMenu)
settingsMenu.add_command(label='Preferences...', command=preferences)
settingsMenu.add_command(label='Style Config...', command=styleConfig)


root.config(menu=menubar)



# Configure Rows and Columns
root.rowconfigure(0, minsize=350, weight=1)
root.columnconfigure(0, minsize=750, weight=1)

# Box
txtEdit = tk.Text(root)

# Put box into grid
txtEdit.grid(row=0, column=0, sticky="nsew")


root.mainloop()
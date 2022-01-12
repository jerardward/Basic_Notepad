from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


class MainWindow:
    def __init__(self):

        self.menuBar = Menu(root)
        root.config(menu=self.menuBar)

        self.filemenu_layout()
        self.editmenu_layout()
        self.helpmenu_layout()
        self.text_box()

    def filemenu_layout(self):
        # File menu
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New", command=self.newFile)
        self.fileMenu.add_command(label="Open", command=self.openFile)
        self.fileMenu.add_command(label="Save", command=self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.quitApp)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

    def editmenu_layout(self):
        # Edit menu
        self.editMenu = Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="Cut", command=self.cut)
        self.editMenu.add_command(label="Copy", command=self.copy)
        self.editMenu.add_command(label="Paste", command=self.paste)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

    def helpmenu_layout(self):
        # Help menu
        self.HelpMenu = Menu(self.menuBar, tearoff=0)
        self.HelpMenu.add_command(label="About Notepad", command=self.about)
        self.menuBar.add_cascade(label="Help", menu=self.HelpMenu)

    def do_popup(self, event):
        # Popup on right click
        self.editMenu.tk_popup(event.x_root, event.y_root)
        self.editMenu.grab_release()

    def text_box(self):
        # Text field
        self.TextArea = Text(root, font="lucida 14")
        self.file = None
        self.TextArea.pack(expand=True, fill=BOTH)
        self.TextArea.bind("<Button-2>", self.do_popup)

        self.Scroll = Scrollbar(self.TextArea)
        self.Scroll.pack(side=RIGHT, fill=Y)
        self.Scroll.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scroll.set)

    def newFile(self):
        # Create a new file
        root.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0, END)

    def openFile(self):
        # Open a file
        self.file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            root.title(os.path.basename(self.file) + " - Notepad")
            self.TextArea.delete(1.0, END)
            f = open(self.file, "r")
            self.TextArea.insert(1.0, f.read())
            f.close()

    def saveFile(self):
        # Save a file
        if self.file == None:
            self.file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                # Save as a new file
                f = open(self.file, 'w')
                f.write(self.TextArea.get(1.0, END))
                f.close()
                root.title(os.path.basename(self.file) + " - Notepad")
                print("File Saved")
        else:
            # Save the file
            f = open(self.file, "w")
            f.write(self.TextArea.get(1.0, END))
            f.close()

    def quitApp(self):
        # Exit program
        root.destroy()

    def cut(self):
        self.TextArea.event_generate(("<Cut>"))

    def copy(self):
        self.TextArea.event_generate(("<Copy>"))

    def paste(self):
        self.TextArea.event_generate(("<Paste>"))

    def about(self):
        showinfo("Notepad", "Code By Jerard Ward")


if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")
    MainWindow()
    root.mainloop()

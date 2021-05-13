import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class plantInformation(tk.Frame):
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        label = tk.Label(self, text="Plant information page")
        label.grid(row=1, column=1)

        self.plant_text = tk.Text(self, width=30, height=10)
        self.plant_text.grid(row = 2, column = 1)

        self.select_plant = tk.Button(self, text="Open plant file", command = self.open_txt)
        self.select_plant.grid(row=3, column = 0)

        self.save_btn = tk.Button(self, text="Save changes", command = self.save_txt)
        self.save_btn.grid(row=3, column = 2)

        self.home_btn = tk.Button(self, text="Return to home page", command=lambda: controller.show_frame(0))
        self.home_btn.grid(row=3, column=1)

    def open_txt(self):
        text_file = filedialog.askopenfilename(initialdir= "C:\IA_GardenHub" , title="Open File", filetypes=(("text files", "*.txt"), ))
        textfile = open(text_file, 'r')
        stuff = textfile.read()

        self.plant_text.insert(tk.END, stuff)
        textfile.close()

    def save_txt(self):
        savemsg = messagebox.showinfo("update", "All changes have been saved", icon="info")
        text_file = open('sample.txt', 'w')
        text_file.write(self.plant_text.get(1.0, tk.END))
        if savemsg == 'ok':
            text_file.close()
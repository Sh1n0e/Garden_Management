import tkinter as tk
import sqlite3
import PlantFrame as pf

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)


class Gardenhub(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(row=0, column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, pf.Plants):
            frame = F(self, container)

            self.frames[F] = frame

            self.frames[F].grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to the garden", font=MEDIUM_FONT)
        label.grid(row=1, column=1)

        button1 = tk.Button(self, text="Visit Equipment Page",
                            command=lambda: parent.show_frame(PageOne))
        button1.grid(row=3, column=1)

        button2 = tk.Button(self, text="Test page",
                            command=lambda: controller.show_frame(pf.Plants))
        button2.grid(row=4, column=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Equipment Page!!!", font=MEDIUM_FONT)
        label.grid(row=1, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=2, column=1)

        button2 = tk.Button(self, text="Visit plant page",
                            command=lambda: controller.show_frame(PageOne))
        button2.grid(row=3, column=2)


app = Gardenhub()
app.mainloop()

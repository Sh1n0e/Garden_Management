import tkinter as tk
import sqlite3

LARGE_FONT = ("Verdana", 12)
MEDUIM_FONT = ("Verdana", 10)


class Gardenhub(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to the garden", font=MEDUIM_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Plant Page",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Equipment Page",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Plant page!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Equipment Page",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        L1 = tk.Label(self, text="Plant ID")
        L1.pack()
        T1 = tk.Entry(self, width=30, bd=5)
        T1.pack()

        L2 = tk.Label(self, text="Plant Name")
        L2.pack()
        T2 = tk.Entry(self, width=30, bd=5)
        T2.pack()

        L3 = tk.Label(self, text="Harvestable?")
        L3.pack()
        T3 = tk.Entry(self, width=30, bd=5)
        T3.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Equipment Page!!!", font=MEDUIM_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = Gardenhub()
app.mainloop()

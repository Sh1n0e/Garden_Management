import tkinter as tk
import PlantFrame as pf
import EquipFrame as eq
import CalendarFrame as ca

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

        for F in (StartPage, pf.Plants, eq.Equipment, ca.Calendar):
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
                            command=lambda: parent.show_frame(eq.Equipment))
        button1.grid(row=3, column=1)

        button2 = tk.Button(self, text="Plant page",
                            command=lambda: parent.show_frame(pf.Plants))
        button2.grid(row=4, column=1)

        button3 = tk.Button(self, text="Calendar page",
                            command=lambda: parent.show_frame(ca.Calendar))
        button3.grid(row=5, column=1)

app = Gardenhub()
app.mainloop()

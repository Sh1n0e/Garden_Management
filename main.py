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

        myStartPage = StartPage(container, self)
        myPlantFrame = pf.Plants(container, self)
        myEquipmentFrame = eq.Equipment(container, self)
        myCalendarFrame = ca.Calendar(container, self)

        self.frames = [myStartPage, myPlantFrame, myEquipmentFrame, myCalendarFrame]

        for F in self.frames:
            F.grid(row=0, column=0, sticky="nsew")

        self.frames[0].tkraise()

    def show_frame(self, frameIndex):
        frame = self.frames[frameIndex]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        label = tk.Label(self, text="Welcome to the garden", font=MEDIUM_FONT)
        label.grid(row=1, column=1)

        button1 = tk.Button(self, text="Visit Equipment Page",
                            command=lambda: controller.show_frame(2))
        button1.grid(row=3, column=1)

        button2 = tk.Button(self, text="Plant page",
                            command=lambda: controller.show_frame(1))
        button2.grid(row=4, column=1)

        button3 = tk.Button(self, text="Calendar page",
                            command=lambda: controller.show_frame(3))
        button3.grid(row=5, column=1)



app = Gardenhub()
app.mainloop()

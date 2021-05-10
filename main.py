import tkinter as tk
import sqlite3
import PlantFrame as pf

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)



class Gardenhub(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, pf.Plants):
            frame = F(self, container)

            self.frames[F] = frame

        self.frames[StartPage].grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to the garden", font=MEDIUM_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Plant Page",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Equipment Page",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = tk.Button(self, text="Test page",
                            command=lambda: controller.show_frame(pf.Plants))
        button3.pack()




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

        plant_id = tk.Label(self, text="Plant ID")
        plant_id.pack()
        plant_id_entry = tk.Entry(self, width=30, bd=5)
        plant_id_entry.pack()

        plant_name = tk.Label(self, text="Plant Name")
        plant_name.pack()
        plant_name_entry = tk.Entry(self, width=30, bd=5)
        plant_name_entry.pack()

        harvestable = tk.Label(self, text="Harvestable?")
        harvestable.pack()
        harvestable_entry = tk.Entry(self, width=30, bd=5)
        harvestable_entry.pack()

        next_plant = tk.Button(self, text=">")
        next_plant.pack()

        prev_plant = tk.Button(self, text="<")
        prev_plant.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Equipment Page!!!", font=MEDIUM_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit plant page",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        equipment_id = tk.Label(self, text="Equipment ID")
        equipment_id.pack()
        equipment_id_entry = tk.Entry(self, width=30, bd=5)
        equipment_id_entry.pack()

        equipment_name = tk.Label(self, text="Equipment Name")
        equipment_name.pack()
        equipment_name_entry = tk.Entry(self, width=30, bd=5)
        equipment_name_entry.pack()

        quantity = tk.Label(self, text="Quantity")
        quantity.pack()
        quantity_entry = tk.Entry(self, width=30, bd=5)
        quantity_entry.pack()

app = Gardenhub()
app.mainloop()

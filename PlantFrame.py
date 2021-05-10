import sqlite3
import tkinter as tk

class Plants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Plant_window_label = tk.Label(self, text="Garden system: Plants")
        self.Plant_window_label.grid(row=0, column=1 )

        self.var_plant_index = tk.IntVar()
        self.var_plant_index.set(0)

        self.var_plant_id = tk.StringVar(self)
        self.var_plant_name = tk.StringVar(self)
        self.var_harvest = tk.StringVar(self)

        self.plant_id = tk.Label(self, text="Plant ID:")
        self.plant_id.grid()
        self.plant_id_entry = tk.Entry(self)
        self.entry_plant_id = tk.Entry(self, textvariable=self.var_plant_id)
        self.entry_plant_id.grid(row=1, column=0)

        self.plant_name = tk.Label(self, text="Plant name:")
        self.plant_name.grid(row=2, column=-0)
        self.plant_name_entry = tk.Entry(self)
        self.entry_plant_name = tk.Entry(self, textvariable=self.var_plant_name)
        self.entry_plant_name.grid(row=2, column=1)

        self.Harvest = tk.Label(self, text="Harvestable?:")
        self.Harvest.grid(row=3, column=0)
        self.Harvest_entry = tk.Entry(self)
        self.entry_Harvest = tk.Entry(self, textvariable=self.var_harvest)
        self.entry_Harvest.grid(row=3, column=1)

        self.load_plants_btn = tk.Button(self, text="Load", command=self.load_plants)
        self.load_plants_btn.grid(row=5, column=2)

        self.next_plant_btn = tk.Button(self, text=">", command=self.next_plant)
        self.next_plant_btn.grid(row=6, column=1)

        self.prev_plant_btn = tk.Button(self, text="<", command=self.prev_plant)
        self.prev_plant_btn.grid(row=6, column=3)

        self.new_plant_btn = tk.Button(self, text="New data", command=self.new_plant)
        self.new_plant_btn.grid(row=5, column=3)

        self.delete_plant_btn = tk.Button(self, text="Delete entry", command=self.delete_plant)
        self.delete_plant_btn.grid(row=3, column=3)

        self.update_plant_btn = tk.Button(self, text="Update entry", command=self.update_plant, state="disabled")
        self.update_plant_btn.grid(row=4, column=3)

        self.set_plant_data()

    def load_plants(self):
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        c.execute("SELECT * FROM plant")
        data = c.fetchall()
        row = data[0]
        print(row[1])
        return data

    def set_plant_data(self):
        data = self.load_plants()
        row = data[self.var_plant_index.get()]
        self.var_plant_id.set(row[0])
        self.var_harvest.set(row[2])
        self.var_plant_name.set(row[1])


    def next_plant(self):
        print("Here is the next item")
        self.var_plant_index.set(self.var_plant_index.get() + 1)
        self.set_plant_data()


    def prev_plant(self):
        print("Here is the previous item")
        self.var_plant_index.set(self.var_plant_index.get() - 1)
        self.set_plant_data()


    def new_plant(self):
        self.var_plant_id.set("")
        self.var_plant_name.set("")
        self.var_harvest.set("")
        self.update_plant_btn["state"] = "active"
        print("INSERT")
        equipment = [self.var_plant_name.get(), self.var_harvest.get()]
        insert_query = "INSERT INTO plant VALUES (null,?,?)"
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        c.execute(insert_query, equipment)
        conn.commit()


    def delete_plant(self):
        tk.MsgBox = tk.messagebox.askquestion('DELETE RECORD',
                                        'Are you sure you want to delete the current record? This cannot be undone.',
                                        icon='warning')
        if tk.MsgBox == 'yes':
            conn = sqlite3.connect('Plants.db')
            c = conn.cursor()
            delete_query = "DELETE FROM plant WHERE plant_id=" + str(self.var_plant_id.get())
            print(delete_query)
            c.execute(delete_query)
            conn.commit()
            self.set_plant_data()
            print("DELETED")


    def update_plant(self):
        print("UPDATE")
        plant = [self.var_plant_name.get(), self.var_harvest.get(), self.var_plant_id.get()]
        update_query = "UPDATE plant SET species=? , harvestable=? WHERE plant_id=?"
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        c.execute(update_query, plant)
        conn.commit()
        self.set_plant_data()


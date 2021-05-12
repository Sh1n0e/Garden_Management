from tkinter import messagebox
import sqlite3
import tkinter as tk


class Equipment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.var_recordset_index = tk.IntVar()
        self.var_recordset_index.set(0)

        self.var_recordset_index = tk.IntVar()
        self.var_recordset_index.set(0)

        self.Equipment_window_label = tk.Label(self, text="Garden system: Equipment")
        self.Equipment_window_label.grid(row =0 ,column =1 )

        self.var_equipment_id = tk.StringVar(self)
        self.var_name = tk.StringVar(self)
        self.var_quantity = tk.StringVar(self)

        self.equipment_id = tk.Label(self, text="Equipment ID:")
        self.equipment_id.grid(row=1, column =0)
        self.equipment_id_entry = tk.Entry(self)
        self.entry_equipment_id = tk.Entry(self, textvariable = self.var_equipment_id)
        self.entry_equipment_id.grid(row=1, column=1)

        self.name = tk.Label(self, text="Name:")
        self.name.grid(row=2, column =0 )
        self.name_entry = tk.Entry(self)
        self.entry_name = tk.Entry(self, textvariable = self.var_name)
        self.entry_name.grid(row=2, column=1)

        self.quantity = tk.Label(self, text="Quantity:")
        self.quantity.grid(row=3, column=0)
        self.quantity_entry = tk.Entry(self)
        self.entry_quantity = tk.Entry(self, textvariable = self.var_quantity)
        self.entry_quantity.grid(row=3, column=1)

        self.load_equipment_btn = tk.Button(self, text = "Load", command = self.load_equipment)
        self.load_equipment_btn.grid(row=6, column=1)

        self.next_btn = tk.Button(self, text=">", command = self.next)
        self.next_btn.grid(row=5, column=2)

        self.prev_btn = tk.Button(self, text="<", command = self.prev)
        self.prev_btn.grid(row=5, column=0)

        self.new_btn = tk.Button(self, text="New data", command = self.new)
        self.new_btn.grid(row=2, column=2)

        self.delete_btn = tk.Button(self, text = "Delete entry", command = self.delete)
        self.delete_btn.grid(row=6, column=2)

        self.update_btn = tk.Button(self, text = "Update entry", command = self.update, state = "disabled")
        self.update_btn.grid(row=6,column=0)

        self.home_btn = tk.Button(self, text="Return to home page", command=lambda: controller.show_frame(0))
        self.home_btn.grid(row=5, column=1)

        self.set_data()

    def load_equipment(self):
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Equipment")
        data = c.fetchall()
        row = data[0]
        print(row[1])
        return data

    def set_data(self):
        data = self.load_equipment()
        row = data[self.var_recordset_index.get()]
        self.var_equipment_id.set(row[0])
        self.var_quantity.set(row[2])
        self.var_name.set(row[1])

    def next(self):
        print("Here is the next item")
        self.var_recordset_index.set(self.var_recordset_index.get() + 1)
        self.set_data()

    def prev(self):
        print("Here is the previous item")
        self.var_recordset_index.set(self.var_recordset_index.get() - 1)
        self.set_data()

    def new(self):
        self.var_equipment_id.set("")
        self.var_name.set("")
        self.var_quantity.set("")
        self.update_btn["state"] = "active"
        print("INSERT")
        equipment = [self.var_name.get(), self.var_quantity.get()]
        insert_query = "INSERT INTO equipment VALUES (null,?,?)"
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        c.execute(insert_query, equipment)
        conn.commit()

    def delete(self):
        MsgBox = messagebox.askquestion('DELETE RECORD',
                                        'Are you sure you want to delete the current record? This cannot be undone.',
                                        icon='warning')
        if MsgBox == 'yes':
            conn = sqlite3.connect('Plants.db')
            c = conn.cursor()
            delete_query = "DELETE FROM equipment WHERE equipment_id=" + str(self.var_equipment_id.get())
            print(delete_query)
            c.execute(delete_query)
            conn.commit()
            self.set_data()
            print("DELETED")

    def update(self):
        messagebox.showinfo("update", "All changes have been saved", icon="info")
        print("UPDATE")
        equipment = [self.var_name.get(), self.var_quantity.get(), self.var_equipment_id.get()]
        update_query = "UPDATE equipment SET type=? , quantity=? WHERE equipment_id=?"
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        c.execute(update_query, equipment)
        conn.commit()
        self.set_data()


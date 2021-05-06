from tkinter import messagebox
import sqlite3
from tkinter import *

def load_plants():
    conn = sqlite3.connect('Plants.db')
    c = conn.cursor()
    c.execute("SELECT * FROM plant")
    data = c.fetchall()
    row = data[0]
    print(row[1])
    return data

def set_plant_data():
    data = load_plants()
    row = data[var_plant_index.get()]
    var_plant_id.set(row[0])
    var_harvest.set(row[2])
    var_plant_name.set(row[1])


def next_plant():
    print("Here is the next item")
    var_plant_index.set(var_plant_index.get() + 1)
    set_plant_data()


def prev_plant():
    print("Here is the previous item")
    var_plant_index.set(var_plant_index.get() - 1)
    set_plant_data()


def new_plant():
    var_plant_id.set("")
    var_plant_name.set("")
    var_harvest.set("")
    update_plant_btn["state"] = "active"
    print("INSERT")
    equipment = [var_plant_name.get(), var_harvest.get()]
    insert_query = "INSERT INTO plant VALUES (null,?,?)"
    conn = sqlite3.connect('Plants.db')
    c = conn.cursor()
    c.execute(insert_query, equipment)
    conn.commit()


def delete_plant():
    MsgBox = messagebox.askquestion('DELETE RECORD',
                                    'Are you sure you want to delete the current record? This cannot be undone.',
                                    icon='warning')
    if MsgBox == 'yes':
        conn = sqlite3.connect('Plants.db')
        c = conn.cursor()
        delete_query = "DELETE FROM plant WHERE plant_id=" + str(var_plant_id.get())
        print(delete_query)
        c.execute(delete_query)
        conn.commit()
        set_plant_data()
        print("DELETED")


def update_plant():
    print("UPDATE")
    plant = [var_plant_name.get(), var_harvest.get(), var_plant_id.get()]
    update_query = "UPDATE plant SET species=? , harvestable=? WHERE plant_id=?"
    conn = sqlite3.connect('Plants.db')
    c = conn.cursor()
    c.execute(update_query, plant)
    conn.commit()
    set_plant_data()

plant_window = Tk()
plant_window.geometry("800x800")
Plant_window_label = Label(plant_window, text="Garden system: Plants")
Plant_window_label.place(relx=0.3, rely=0.2, anchor=CENTER)

var_plant_index = IntVar()
var_plant_index.set(0)

var_plant_id = StringVar(plant_window)
var_plant_name = StringVar(plant_window)
var_harvest = StringVar(plant_window)

plant_id = Label(plant_window, text="Plant ID:")
plant_id.place(relx=0.1, rely=0.3, anchor=CENTER)
plant_id_entry = Entry(plant_window)
entry_plant_id = Entry(plant_window, textvariable=var_plant_id)
entry_plant_id.place(relx=0.3, rely=0.3, anchor=CENTER)


plant_name = Label(plant_window, text="Plant name:")
plant_name.place(relx=0.1, rely=0.4, anchor=CENTER)
plant_name_entry = Entry(plant_window)
entry_plant_name = Entry(plant_window, textvariable=var_plant_name)
entry_plant_name.place(relx=0.3, rely=0.4, anchor=CENTER)


Harvest = Label(plant_window, text="Harvestable?:")
Harvest.place(relx=0.1, rely=0.5, anchor=CENTER)
Harvest_entry = Entry(plant_window)
entry_Harvest = Entry(plant_window, textvariable=var_harvest)
entry_Harvest.place(relx=0.3, rely=0.5, anchor=CENTER)


load_plants_btn = Button(plant_window, text="Load", command=load_plants)
load_plants_btn.place(relx=0.3, rely=0.6, anchor=CENTER)


next_plant_btn = Button(plant_window, text=">", command=next_plant)
next_plant_btn.place(relx=0.4, rely=0.6, anchor=CENTER)


prev_plant_btn = Button(plant_window, text="<", command=prev_plant)
prev_plant_btn.place(relx=0.2, rely=0.6, anchor=CENTER)


new_plant_btn = Button(plant_window, text="New data", command=new_plant)
new_plant_btn.place(relx=0.5, rely=0.5, anchor=CENTER)


delete_plant_btn = Button(plant_window, text="Delete entry", command=delete_plant)
delete_plant_btn.place(relx=0.5, rely=0.4, anchor=CENTER)


update_plant_btn = Button(plant_window, text="Update entry", command=update_plant, state="disabled")
update_plant_btn.place(relx=0.5, rely=0.3, anchor=CENTER)


set_plant_data()
plant_window.mainloop()
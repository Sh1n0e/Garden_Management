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
    row = data[var_recordset_index.get()]
    var_plant_id.set(row[0])
    var_harvest.set(row[2])
    var_name.set(row[1])

def next():
    print("Here is the next item")
    var_recordset_index.set(var_recordset_index.get()+1)
    set_plant_data()

def prev():
    print("Here is the previous item")
    var_recordset_index.set(var_recordset_index.get() - 1)
    set_plant_data()

def new():
    var_plant_id.set("")
    var_name.set("")
    var_harvest.set("")
    update_btn["state"] = "active"
    print("INSERT")
    equipment = [var_name.get(), var_harvest.get()]
    insert_query = "INSERT INTO plant VALUES (null,?,?)"
    conn = sqlite3.connect('Plants.db')
    c = conn.cursor()
    c.execute(insert_query, equipment)
    conn.commit()

def delete():
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

def update():
	print("UPDATE")
	equipment = [var_name.get(), var_harvest.get(), var_plant_id.get()]
	update_query = "UPDATE plant SET species=? , harvestable=? WHERE plant_id=?"
	conn = sqlite3.connect('Plants.db')
	c = conn.cursor()
	c.execute(update_query, equipment)
	conn.commit()
	set_plant_data()

var_recordset_index = IntVar()
var_recordset_index.set(0)

var_recordset_index = IntVar()
var_recordset_index.set(0)

Equipment_window_label = Label(root, text="Garden system: Plants")
Equipment_window_label.grid(row =0 ,column =1 )

var_plant_id = StringVar(root)
var_name = StringVar(root)
var_harvest = StringVar(root)

plant_id = Label(root, text="Plant ID:")
plant_id.grid(row=1, column =0)
plant_id_entry = Entry(root)
entry_plant_id = Entry(root, textvariable = var_plant_id)
entry_plant_id.grid(row=1, column=1)

name = Label(root, text="Plant name:")
name.grid(row=2, column =0 )
name_entry = Entry(root)
entry_name = Entry(root, textvariable = var_name)
entry_name.grid(row=2, column=1)

quantity = Label(root, text="Harvestable?:")
quantity.grid(row=3, column=0)
quantity_entry = Entry(root)
entry_quantity = Entry(root, textvariable = var_harvest)
entry_quantity.grid(row=3, column=1)

load_plants_btn = Button(root, text = "Load", command = load_plants)
load_plants_btn.grid(row=6, column=1)

next_btn = Button(root, text=">", command = next)
next_btn.grid(row=5, column=2)

prev_btn = Button(root, text="<", command = prev)
prev_btn.grid(row=5, column=0)

new_btn = Button(root, text="New data", command = new)
new_btn.grid(row=2, column=2)

delete_btn = Button(root, text = "Delete entry", command = delete)
delete_btn.grid(row=6, column=2)

update_btn = Button(root, text = "Update entry", command = update, state = "disabled")
update_btn.grid(row=6,column=0)

set_plant_data()
root.mainloop()
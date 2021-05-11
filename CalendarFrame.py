# Import Required Library
import tkinter as tk
from datetime import date
import tkcalendar as cal


class Calendar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add Calender
        self.cal = cal.Calendar(self, selectmode='day',
                            year=2020, month=5,
                            day=22)
        self.cal.grid(row=0, column=0)

        # Add Button and Label
        Get_date=tk.Button(self, text="Get Date",
                  command=self.grad_date)
        Get_date.grid(row=1, column=1)

        C_date = tk.Label(self, text="")
        C_date.grid(row=2, column=0)

    def grad_date(self):
        date.config(text="Selected Date is: " + self.cal.get_date())



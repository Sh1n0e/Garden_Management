# Import Required Library
import tkinter as tk
import tkcalendar as cal


class Calendar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add Calender
        self.cal = cal.Calendar(self, selectmode='day',
                            year=2020, month=5,
                            day=22)
        self.cal.grid(row=0, column=0)



        self.home_btn = tk.Button(self, text="Return to home page", command=lambda: controller.show_frame(0))
        self.home_btn.grid(row=1, column=0)







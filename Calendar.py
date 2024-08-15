import tkinter as tk

class Calendar:
    def __init__(self):
        # Main window
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.configure(bg="lightpink")

        # Month entry
        self.month_label = tk.Label(self.root, text=" Month ", borderwidth=10, relief="flat", bg="lightPink", fg="black", font=("Arial", 18))
        self.month_label.grid(row=1, column=1, padx=5, pady=20)

        self.month_entry = tk.Entry(self.root, borderwidth=0, relief="flat", bg="White", fg="black")
        self.month_entry.grid(row=1, column=3, padx=0, pady=20)

        self.month = self.month_entry.get()

        # Button to generate the calendar
        self.generate_button = tk.Button(self.root, text="Generate Calendar", command=self.generate_calendar)
        self.generate_button.grid(row=1, column=5, columnspan=3, pady=2, padx=20)

        self.root.mainloop()

    def generate_calendar(self):
        month = self.month_entry.get()
        year = 2023  # you can set year dynamically as well
        self.create_date(month, year)

    def create_date(self, month, year):
        total_days = self.totalday(month, year)
        num = 1
        row = 3
        column = 0

        while num <= total_days:
            day = tk.Button(self.root, text=num, width=5, height=3, relief="flat")
            day.grid(row=row, column=column, padx=5,pady=10)
            num += 1
            column += 1
            if column == 7:  # move to next row after 7 columns
                row += 1
                column = 0

    def totalday(self, month, year):
        if month in ["January", "March", "May", "July", "August", "October", "December"]:
            return 31
        elif month in ["April", "June", "September", "November"]:
            return 30
        elif month == "February":
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 0  # In case of invalid month
        
        
    
        


import tkinter as tk
class Calendar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("745x500")
        self.root.configure(bg="lightpink")
        self.total_dates = 35  # Total number of dates to display
        self.create_dates(self.total_dates)
        self.root.mainloop()
    
    def create_date(self, row, column, day_number):
        box = tk.Label(self.root, text=str(day_number), width=10, height=2, bg="white")
        box.grid(row=row, column=column, padx=5, pady=10)

    def create_dates(self, total_dates):
        num = 0
        row = 0
        column = 0
        while num < total_dates:
            self.create_date(row, column, num + 1)
            num += 1
            column += 1
            # Move to the next row if we exceed the column limit (e.g., 7 days in a week)
            if column >= 7:
                column = 0
                row += 1


import tkinter as tk
from tkinter import ttk

from stats import stats_columns

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Data View")
        self.L1 = tk.Label(self.master, text="File Name")
        self.L2 = tk.Label(self.master, text="X Label")
        self.L3 = tk.Label(self.master, text="Y Label")

        self.L1.grid(row=0, column=0)
        self.L2.grid(row=1, column=0)
        self.L3.grid(row=2, column=0)

        self.eFname = tk.Entry(self.master, width=40)
        self.eX = tk.Entry(self.master, width=40)
        self.eY = tk.Entry(self.master, width=40)

        self.eFname.grid(row=0, column=1)
        self.eX.grid(row=1, column=1)
        self.eY.grid(row=2, column=1)

        self.txtX = tk.Text(self.master, width=30)
        self.txtY = tk.Text(self.master, width=30)

        self.txtX.grid(row=3, column=0, columnspan=2, sticky='w')
        self.txtY.grid(row=4, column=0, columnspan=2, sticky='w')

        self.style = ttk.Style()
        self.style.map('TButton',
                       foreground=[('pressed', 'red'), ('active', 'green')],
                       background=[('pressed', 'black'), ('active', 'white')])

        self.btn = ttk.Button(self.master, text="Show Regression Graph", style="TButton")
        self.btn.grid(row=5, column=0, columnspan=2, sticky='w')

        self.stats = ttk.Button(self.master, text="Show Stats")
        self.stats["command"] = self.show_stats
        self.stats.grid(row=6, column=0, columnspan=2, sticky='w')

    def show_stats(self):
        # Add your code here to show the stats
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

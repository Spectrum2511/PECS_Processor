import tkinter as tk
from tkinter import filedialog


window = tk.Tk()
window.title("PECS Processor")
prompt_frame = tk.Frame(master=window)
prompt_frame.pack(side=tk.TOP)

prompt_label = tk.Label(master=prompt_frame, text="Select output CSV file:")
prompt_label.pack(side=tk.LEFT)

choose_file_cont = tk.Frame(master=window, width=300, height=200)
choose_file_cont.pack()


window.mainloop()

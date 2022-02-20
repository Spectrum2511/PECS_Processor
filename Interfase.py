import tkinter as tk
from tkinter import filedialog as fd
# used for displaying message once file is selected, used for test purposes
from tkinter.messagebox import showinfo


def select_file():
    filename = fd.askopenfilename(
        title='Select file:',
        initialdir='/'
    )
    path.insert(0, filename)
    # bottom code can be deleted in final build
    showinfo(
        title='Selected Files',
        message=filename
    )


window = tk.Tk()
window.resizable(False, False)

window.title("PECS Processor")
prompt_frame = tk.Frame(master=window)
prompt_frame.pack(side=tk.TOP)

prompt_label = tk.Label(master=prompt_frame, text="Select output CSV file:")
prompt_label.pack(side=tk.LEFT)

choose_file_cont = tk.Frame(master=window, width=300, height=200)
choose_file_cont.pack()

choose_btn = tk.Button(master=choose_file_cont, text='Choose File:', command=select_file)
choose_btn.pack(side=tk.LEFT)

path = tk.Entry(master=choose_file_cont)
path.pack(side=tk.RIGHT)

window.mainloop()

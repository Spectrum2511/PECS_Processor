import tkinter as tk
from tkinter import filedialog as fd
# used for displaying message once file is selected, used for test purposes
from tkinter.messagebox import showinfo


def select_file():
    filename = fd.askopenfilename(title='Select file:', initialdir='/')
    path.insert(0, filename)
    # bottom code can be deleted in final build
    showinfo(title='Selected Files', message=filename)


window = tk.Tk()
window.resizable(True, False)

window.title("PECS Processor")
prompt_frame = tk.Frame(master=window)
prompt_frame.pack(side=tk.TOP)

prompt_label = tk.Label(master=prompt_frame, text="Select output CSV file and save location:")
prompt_label.pack(side=tk.LEFT)

choose_file_cont = tk.Frame(master=window, width=300, height=200)
choose_file_cont.pack()

choose_btn = tk.Button(master=choose_file_cont, width=13, text='Choose File:', command=select_file)
choose_btn.pack(side=tk.LEFT, padx=5)

path = tk.Entry(master=choose_file_cont)
path.pack(side=tk.RIGHT, padx=5)

save_loc_cont = tk.Frame(master=window, width=300, height=200)
save_loc_cont.pack()

save_btn = tk.Button(master=save_loc_cont, width=13, text='Save Output To:')
save_btn.pack(side=tk.LEFT, padx=5)

save_path = tk.Entry(master=save_loc_cont)
save_path.pack(side=tk.RIGHT, padx=5)
# TODO: Add functionality to save path button
# TODO: Set scaling for entry widgets to auto scale as the window is enlarged, buttons should stay the same size and
#  in the same place when window is resized
process_cont = tk.Frame(master=window, width=300, height=200)
process_cont.pack()

process_btn = tk.Button(master=process_cont, text='Process File')
process_btn.pack(pady=5)
# TODO: add functionality to process button
window.mainloop()

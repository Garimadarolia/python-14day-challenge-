import tkinter as tk
from tkinter import messagebox
import csv


def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    try:
        Englishmarks = float(Englishmarks_entry.get())
        Hindimarks = float(Hindimarks_entry.get())
        Mathsmarks = float(Mathsmarks_entry.get())

    except ValueError:
        messagebox.showerror("Error", "Please enter a number.")
        return
    average = float((Englishmarks + Mathsmarks + Hindimarks) / 3)
    grade = get_grade(average)
    output = (f"{name} (Roll No. {roll}) - \n"
              f"English Marks: {Englishmarks}\n"
              f"Maths Marks: {Mathsmarks}\n"
              f"Hindi Marks: {Hindimarks}\n"
              f" Average:{average:.2f}\n"
              f" grade: {grade}\n")
    output_list.insert(tk.END, output + "\n\n")





def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


def save_to_file():
    rows = []
    for i in range(output_list.size()):
        rows.append([output_list.get(i)])  # Store everything in a list first

    # Now write to the file in one go
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)  # Write all rows together

    # Show message AFTER file is safely closed
    messagebox.showinfo("Success", "Successfully saved to file students.csv")

root = tk.Tk()
root.geometry("500x500")
root.title("Student Grade Tracker")
root.resizable(True,   True)
root.configure(bg="lightblue")
#root.grid_rowconfigure(6, weight=1)       # Row 6 can grow vertically
#root.grid_columnconfigure(1, weight=1)    # Column 1 can grow horizontally



#labels and entry fields
tk.Label(root, text="Name",width= 10).grid(row=0,column=0,pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
name_entry.grid(row=0,column=1)

tk.Label(root, text="Roll No.",width= 10).grid(row=1,column=0,pady=5)
roll_entry = tk.Entry(root)
roll_entry.grid(row=1,column=1)

tk.Label(root, text="English Marks",width= 10).grid(row=2,column=0,pady=5)
Englishmarks_entry = tk.Entry(root)
Englishmarks_entry.grid(row=2,column=1)

tk.Label(root, text="Hindi Marks",width= 10).grid(row=3,column=0,pady=5)
Hindimarks_entry = tk.Entry(root)
Hindimarks_entry.grid(row=3,column=1)

tk.Label(root, text="Maths Marks",width= 10).grid(row=4,column=0,pady=5)
Mathsmarks_entry = tk.Entry(root)
Mathsmarks_entry.grid(row=4,column=1)




tk.Button(root, text="Save to CSV", command=save_to_file).grid(row=7,column=0,columnspan=2,pady=10)


tk.Button(root, text="Add Student", command=add_student).grid(row=5,column=0, columnspan=2,pady=10)

output_list = tk.Text(root, width=45 , height=17)
output_list.grid(row=6,column=0, columnspan=2,pady=10, padx=50, sticky="nsew")

root.mainloop()
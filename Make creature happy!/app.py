import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image,ImageTk

#define creature data
creatures = {
    "Cat": {
        "question": "How many lives do cats have?",
        "answer": "9",
        "happy": "Purrfect! The cat is purring happily.",
        "angry": "The cat knocks your cup off the table. Typical.",
        "image": "cat.png"
    },
    "Dog": {
        "question": "Spell 'woof' backwards.",
        "answer": "foow",
        "happy": "Tail wags! You're now officially best friends.",
        "angry": "Dog stares in betrayal and walks away slowly...",
        "image": "dog.png"
    },
    "Robot": {
        "question": "What is 101 in binary (decimal form)?",
        "answer": "5",
        "happy": "BEEP BOOP. You are certified non-bot.",
        "angry": "ACCESS DENIED. Robot spins in disappointment.",
        "image": "robot.png"
    }
}

# Pick a random creature
creature_name = random.choice(list(creatures.keys()))
creature = creatures[creature_name]

# GUI setup
root = tk.Tk()
root.title("Make the Creature Happy!")
root.geometry("500x500")
root.configure(bg="orange")

# Load creature image
image = Image.open(creature["image"])
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)

img_label = tk.Label(root, image=photo, bg="lightblue")
img_label.pack(pady=20)

# Question
question_label = tk.Label(root, text=creature["question"], font=("Arial", 14), bg="lightblue")
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=10)

def check_answer():
    user_answer = answer_entry.get().strip().lower()
    if user_answer == creature["answer"]:
        messagebox.showinfo("You got it bro!", creature["happy"])
    else:
        messagebox.showwarning("Pathetic bro!", creature["angry"])

submit_btn = tk.Button(root, text="Make Happy!", command=check_answer, font=("Arial", 12), bg="green", fg="white")
submit_btn.pack(pady=20)

root.mainloop()


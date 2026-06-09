from tkinter import ttk
import tkinter as tk
import pyttsx3
from deep_translator import GoogleTranslator

def show_text():
    text = entry.get()

    if text.strip() == "":
        result_label.config(text= "Please enter text")
        return
    
    source_code = language_codes[source_combo.get()]
    target_code = language_codes[target_combo.get()]

    translated = GoogleTranslator(source = source_code, target = target_code).translate(text)

    result_label.config(text = translated)

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

def listen_text():
    text = result_label.cget("text")

    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

root = tk.Tk()


root.title("Translator")
root.geometry("600x600")
root.configure(bg="#3e76ae")

label = tk.Label(root,  text = "Language Translator", font = ("Arial",18) )
label.pack(pady = 20)


tk.Label(root, text = "Select languages").pack()

languages = ["English", "Hindi", "French", "Spanish"]

source_combo = ttk.Combobox(root, values = languages)
source_combo.pack(pady = 5)
source_combo.set("English")

source_language = source_combo.get()
print(source_language)

target_combo = ttk.Combobox(root, values = languages)
target_combo.pack(pady = 5)
target_combo.set("Hindi")

target_language = target_combo.get()
print(target_language)

language_codes= { "English": "en", "Hindi": "hi", "Spanish": "es", "French": "fr" }

input_label = tk.Label(root, text = "Enter your input: ")
input_label.pack(pady = 5)

entry = tk.Entry(root, width = "30")
entry.pack(pady = 10)

button = tk.Button(root, text = "Translate", command = show_text)
button.pack(pady = 20)


result_label = tk.Label(root, text = "", font = ("Arial", 14 ), bg = "white", fg = "black", width = 20, height = 2)
result_label.pack(pady = 5)


copy_button = tk.Button(root, text = "copy", command = copy_text)
copy_button.pack(pady = 5)

listen_button = tk.Button(root, text ="Listen", command = listen_text)
listen_button.pack(pady = 5)


root.mainloop()

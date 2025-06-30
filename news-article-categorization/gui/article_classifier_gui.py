import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load and train the model using the BBC News Train.csv file
train_df = pd.read_csv(r"C:\Users\nvcse\OneDrive\Desktop\BBC News Train.csv")
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train_df["Text"], train_df["Category"])

# Function to classify the article content using the trained model
def classify_article(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    return model.predict([text])[0]

# GUI logic
def load_and_classify():
    filepath = filedialog.askopenfilename()
    if filepath:
        category = classify_article(filepath)
        result_label.config(text=f"The article is classified as: {category}")
        result_window.deiconify()

def ok_action():
    result_window.withdraw()

# Main window setup
root = tk.Tk()
root.title("Article Classifier")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Fonts
title_font = ("Arial", 24, "bold")
button_font = ("Arial", 12)

# Title label
title_label = tk.Label(root, text="Article Classifier", font=title_font, bg="#f0f0f0")
title_label.pack(pady=(30, 20))

# Subtitle label
subtitle_label = tk.Label(root, text="Upload an article to classify", font=("Arial", 12), bg="#f0f0f0")
subtitle_label.pack()

# Classify button
classify_button = tk.Button(
    root,
    text="Classify",
    command=load_and_classify,
    font=button_font,
    bg="#4CAF50",
    fg="white",
    width=10,
    relief=tk.GROOVE
)
classify_button.pack(pady=30)

# Result window
result_window = tk.Toplevel(root)
result_window.title("Result")
result_window.geometry("300x150")
result_window.resizable(False, False)
result_window.protocol("WM_DELETE_WINDOW", ok_action)
result_window.withdraw()

# Result label
result_label = tk.Label(result_window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# OK button
ok_button = tk.Button(
    result_window,
    text="OK",
    command=ok_action,
    font=button_font,
    bg="#4CAF50",
    fg="white",
    width=10,
    relief=tk.GROOVE
)
ok_button.pack()

# Run the GUI
root.mainloop()

import cv2
import pytesseract
import requests
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


class AnswerChecker():
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Answer Checker")
        self.root.geometry("350x550")

        self.First_page()

    def First_page(self):

        tk.text_label = Label(self.root, text="Automatic Answer\n Checker", font=("Rockwell", 30, 'bold'), fg="#03A9F4")
        tk.text_label.pack()

        tk.Label(self.root, text='''Check Your Answer :''', font=("Helvetica", 20)).pack(anchor="w", pady=50)

        tk.Label(self.root, text="Set Model Answer", font=("Helvetica", 20)).pack()

        model_frame = tk.Frame(self.root)
        model_frame.pack()
        tk.Button(model_frame, text="Browse", command=self.load_image1).pack(side=tk.LEFT, padx=5)


    def Second_page(self):

        tk.Label(self.root, text="Upload Your Answer", font=("Helvetica", 20)).pack()

        ans_frame = tk.Frame(self.root)
        ans_frame.pack()
        tk.Button(ans_frame, text="Browse", command=self.load_image2).pack(side=tk.LEFT)
        
        self.check_button = tk.Button(self.root, text="Check Answer", font=("Helvetica", 17), command=self.Check_similarity, bg='white')
        self.check_button.pack(pady=20)

        self.result_label = tk.Label(self.root, text="", wraplength=400)
        self.result_label.pack(pady=10)

    def load_image1(self):
        self.image1_path = filedialog.askopenfilename()
        if self.image1_path:
            messagebox.showinfo("Image Selected", f"Model Answer: {self.image1_path}")
            self.Second_page()
        else :
            messagebox.showinfo("Image Not Selected", f"You did not select any image! please retry")

    def load_image2(self):
        self.image2_path = filedialog.askopenfilename()
        if self.image2_path:
            messagebox.showinfo("Image Selected", f"Check Answer : {self.image2_path}")
        else :
            messagebox.showinfo("Image Not Selected", f"You did not select any image! please retry")

    def extract_text(self, image_path):
        
        img = cv2.imread(image_path)
        gray_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(threshold_img)
        return text.strip()

    def show_marks(self, ratio):
        marks = 0
        if ratio > 0.8:
            marks = 8
        elif 0.7 < ratio < 0.8:
            marks = 7
        elif 0.6 < ratio < 0.7:
            marks = 6
        elif 0.5 < ratio < 0.6:
            marks = 5
        elif 0.4 < ratio < 0.5:
            marks = 4
        elif 0.3 < ratio < 0.4:
            marks = 3
        elif 0.2 < ratio < 0.3:
            marks = 2
        elif 0.1 < ratio < 0.2:
            marks = 1
        elif ratio > 0.1:
            marks = 0
        return marks
    
    def Check_similarity(self):
        if not self.image1_path or not self.image2_path:
            messagebox.showwarning("Warning", "Please select both images.")
            return

        text1 = self.extract_text(self.image1_path)
        text2 = self.extract_text(self.image2_path)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([text1, text2])
        similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        
        marks = self.show_marks(similarity_score)
        messagebox.showinfo("Your got", f"{marks} marks")


def main():
    root = tk.Tk()
    root.iconbitmap("icon/question.png")
    check = AnswerChecker(root)
    root.mainloop()


if __name__ == "__main__":
    main()

    
import os
import time
import logging
import multiprocessing as mp
import pandas as pd
from pdf2docx import parse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import tkinter as tk
from tkinter import filedialog

# Set up logging configuration
logging.basicConfig(filename='pdf2docx.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

def convert_pdf_to_docx(file):
    input_file = file + ".pdf"
    output_file = file + ".docx"
    try:
        # Convert PDF to DOCX using pdf2docx
        parse(input_file, output_file)
    except Exception as e:
        # Handle errors and log them
        logging.error(f"Error: {e} - {input_file}")
        print(f"Error: {e} - {input_file}")
    else:
        # Handle successful conversion and log it
        logging.info(f"{input_file} successfully converted to {output_file}")
        print(f"{input_file} successfully converted to {output_file}")

def train_classifier(data, labels):
    # Vectorize the input data using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data)
    
    # Train a Naive Bayes classifier on the vectorized data
    clf = MultinomialNB()
    clf.fit(X, labels)
    return clf, vectorizer

def predict_language(input_text, clf, vectorizer):
    # Vectorize the input text using the fitted vectorizer
    X = vectorizer.transform([input_text])
    
    # Use the trained classifier to predict the language of the input text
    language = clf.predict(X)[0]
    return language

def select_file():
    # Open file dialog to select PDF file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def select_folder():
    # Open file dialog to select folder to save converted files
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

if __name__ == '__main__':
    # Use GUI to select PDF file and folder to save converted files
    pdf_file = select_file()
    output_folder = select_folder()
    file_name = os.path.splitext(os.path.basename(pdf_file))[0]

    # Convert selected PDF file to DOCX
    convert_pdf_to_docx(file_name)
    
    # Load the converted DOCX file into memory
    input_file = os.path.join(output_folder, file_name + ".docx")
    if os.path.exists(input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
            data = [text]
            labels = [file_name]
    
    # Train a language classifier on the converted text
    clf, vectorizer = train_classifier(data, labels)
    
    # Use GUI to prompt the user to enter some text to predict the language
    root = tk.Tk()
    root.withdraw()
    input_text = tk.simpledialog.askstring("Input", "Enter some text:")
    
    # Use the trained classifier to predict the language of the input text
    language = predict_language(input_text, clf, vectorizer)
    print(f"The language of the input text is {language}")


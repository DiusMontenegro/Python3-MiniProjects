import os
import time
import logging
import multiprocessing as mp
import pandas as pd
from pdf2docx import parse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

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

if __name__ == '__main__':
    # List of PDF files to convert
    pdf_files = ["sample1", "sample2", "sample3"]
    
    # Use multiprocessing to convert PDF files in parallel
    with mp.Pool() as p:
        p.map(convert_pdf_to_docx, pdf_files)
    
    # Load the converted DOCX files into memory
    data = []
    labels = []
    for file in pdf_files:
        input_file = file + ".docx"
        if os.path.exists(input_file):
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
                data.append(text)
                labels.append(file)
    
    # Train a language classifier on the converted text
    clf, vectorizer = train_classifier(data, labels)
    
    # Prompt the user to enter some text to predict the language
    input_text = input("Enter some text: ")
    
    # Use the trained classifier to predict the language of the input text
    language = predict_language(input_text, clf, vectorizer)
    print(f"The language of the input text is {language}")

# automatic-answer-checker
# Automatic-Answer-Checker

## Overview

The Automatic Answer Checker is a software application designed to evaluate handwritten answers against a given set of correct answers. It utilizes OCR (Optical Character Recognition) and natural language processing (NLP) technologies to recognize text from handwritten submissions and assess them based on predefined criteria.

## Table of Contents

- [Features](#Features)
- [Requirements](#Requirements)
- [Usage](#Usage)
- [Acknowledgments](#Acknowledgments)
- [How to Contribute](#How-to-Contribute)


## Features

Handwriting Recognition: Extracts text from handwritten images using OCR.
Answer Evaluation: Compares recognized text with reference answers and grades responses.
Similarity Analysis: Uses NLP techniques to analyze semantic similarity between student answers and the correct ones.
Customizable Criteria: Allows for scoring based on keywords, sentence structure, and overall relevance.
Error Reporting: Highlights discrepancies between the handwritten response and the expected answer.

## Requirements

### Software
- [Python 3.x](https://www.python.org/)
- [OCR Engine](https://pypi.org/project/pytesseract/)
- [NLP Library (e.g., SpaCy, NLTK, or Hugging Face Transformers)](https://www.nltk.org/book/))


### Modules 
opencv-python
- [pytesseract](https://pypi.org/project/pytesseract/)
- [PIL](https://pypi.org/project/pillow/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [nltk](https://www.nltk.org/book/)
- [os](https://docs.python.org/3/library/os.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)




## Usage

### Prepare Input Files:
Save handwritten answer sheets as images (e.g., JPEG, PNG).
Store reference answers in a text or CSV file.

### Run the Checker:
- [python answer_checker.py --input <path_to_images> --answers <path_to_reference_answers>]

### View Results:
Graded results will be saved in the output/ directory as a CSV or JSON file.
Detailed reports (optional) include detected handwriting and marked discrepancies.

## How to Contribute

We encourage you to contribute to the projects by following these steps:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/YourFeatureName`)
3. **Commit your changes** (`git commit -m 'Add some feature'`)
4. **Push to the branch** (`git push origin feature/YourFeatureName`)
5. **Create a Pull Request**

## Acknowledgments

1. **Tesseract OCR**
2. **Scikit-learn**
3. **NLTK**
4. **OpenAI for NLP inspiration**

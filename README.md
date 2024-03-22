---
title: Image To Text
emoji: 💩
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: 1.32.2
app_file: app.py
pinned: false
---


## Streamlit OCR Web Application

### Context
This project aims to demonstrate Optical Character Recognition (OCR) using the `easyocr` library and deploying it as a web application with Streamlit. The application allows users to upload images containing text, and it extracts the text from the images using the OCR model.

### Problem Statement
The goal is to provide users with a convenient tool for extracting text from images, which can be useful in various scenarios such as digitizing printed documents, extracting information from images, etc.

### Data
The application does not rely on any specific dataset as it performs text extraction directly from user-uploaded images. However, it leverages the pre-trained models provided by the `easyocr` library.

### Functionality
- Users can upload images containing text.
- The application processes the uploaded image using the OCR model.
- Extracted text is displayed to the user.

### Usage
1. **Upload Image**: Users can upload an image containing text by clicking on the "Upload your image here" button.
2. **Text Extraction**: The application processes the uploaded image and extracts the text from it.
3. **Display Results**: Extracted text is displayed to the user below the uploaded image.

### Deployment
The Streamlit OCR Web Application is deployed on Hugging Face Spaces, providing a seamless user experience for accessing the OCR functionality directly from the web browser.

**Link to the deployed application:** [Streamlit OCR Web App](https://huggingface.co/spaces/canoris/image_to_text)

### Testing Methodology

This project incorporates robust testing methodologies to ensure the accuracy and reliability of the OCR functionality. The testing process involves the following steps:

1. **Dictionary Check with Levenshtein Distance**:
   - Before deploying the OCR functionality, we conducted extensive testing using a dictionary to ensure the accuracy of extracted text.
   - The Levenshtein distance algorithm was employed to compare the extracted words with the words in the English dictionary.
   - This helped in identifying and correcting any discrepancies or inaccuracies in the extracted text.

2. **Spell Checking**:
   - We integrated a spell-checking mechanism using the `enchant` library to further enhance the accuracy of the extracted text.
   - Each word extracted from the images undergoes spell checking to detect and correct any misspellings.

### Deployment

The Streamlit OCR Web Application is deployed on Hugging Face Spaces, offering a seamless user experience for text extraction from images. The rigorous testing process ensures that users receive accurate and reliable results.

**Link to the deployed application:** [Streamlit OCR Web App](https://huggingface.co/spaces/canoris/image_to_text)

### Future Improvements
- Continuous Integration (CI) and Continuous Deployment (CD) pipelines to automate the testing and deployment process.
- Integration of additional language models for multilingual support.
- Implementation of feedback mechanisms to gather user suggestions and improve the OCR functionality further.

### Acknowledgments
- The project leverages the `easyocr` library for Optical Character Recognition.
- Streamlit is utilized for creating the interactive web application.
- Hugging Face Spaces facilitates the deployment of the web application.

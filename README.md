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

To answer the question in your README on GitHub regarding your Streamlit app deployed on Hugging Face:

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

### Future Improvements
- Implementing additional features such as language selection for OCR.
- Improving the user interface for better usability.
- Optimizing the OCR model for better performance.

### Acknowledgments
- The project utilizes the `easyocr` library for Optical Character Recognition.
- Streamlit is used for creating the interactive web application.
- Hugging Face Spaces is utilized for deploying the web application.

---

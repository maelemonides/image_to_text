import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np
import re
import enchant  # For spell checking
import Levenshtein

# Title
st.title("Easy OCR - Extract Text from Images")

# Subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit` - hosted on 🤗 Spaces")

# Image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

# Load English dictionary for spell checking
english_dict = enchant.Dict("en_US")

# Function for text preprocessing
def preprocess_text(text):
    # Remove non-alphanumeric characters and extra whitespaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    # Convert text to lowercase
    text = text.lower()
    # Optionally, perform spell checking
    words = text.split()
    corrected_words = []
    for word in words:
        closest_word = find_closest_word(word)
        corrected_words.append(closest_word)
    return ' '.join(corrected_words)

# Function to find closest word in English dictionary
def find_closest_word(word):
    closest_word = word
    min_distance = np.inf
    for dict_word in english_dict.suggest(word):
        distance = Levenshtein.distance(word, dict_word)
        if distance < min_distance:
            min_distance = distance
            closest_word = dict_word
    return closest_word



# Function to load OCR model
@st.cache
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader

reader = load_model()  # Load model

if image is not None:
    input_image = Image.open(image)  # Read image
    st.image(input_image)  # Display image

    with st.spinner("🤖 AI is at Work!"):
        result = reader.readtext(np.array(input_image))
        result_text = []  # Empty list for results

        for text in result:
            result_text.append(text[1])

        # Text preprocessing
        preprocessed_text = [preprocess_text(text) for text in result_text]

        st.write(preprocessed_text)
        st.balloons()
else:
    st.write("Upload an Image")

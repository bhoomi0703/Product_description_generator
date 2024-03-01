# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:52:45 2024

@author: bhoom
"""

import streamlit as st
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Streamlit UI
st.title("E-commerce Product Description Generator")

# Input for product details
product_name = st.text_input("Product Name:")
product_features = st.text_area("Product Features:")

# Function to generate product description
def generate_description(product_name, product_features):
    # Tokenize and remove stop words
    stop_words = set(stopwords.words("english"))

    words = word_tokenize(product_features)
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Get the most frequent words
    freq_dist = FreqDist(filtered_words)
    most_common_words = freq_dist.most_common(5)

    # Generate a description using the most common words
    description = f"Introducing {product_name}, a {', '.join([word for word, _ in most_common_words])} {product_name.lower()} that {product_features.lower()}."

    return description

# Button to generate description
if st.button("Generate Description"):
    if not product_name or not product_features:
        st.warning("Please enter product name and features.")
    else:
        # Call the generate_description function
        description = generate_description(product_name, product_features)
        st.success("Generated Description:")
        st.write(description)

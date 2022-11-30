import streamlit as st
import pandas as pd
import cv2 
from PIL import Image


with st.sidebar: 
    st.image("https://editor.analyticsvidhya.com/uploads/59954intro%20to%20CNN.JPG")
    st.title("Skin Cancer Classification using Deep Learning")
    choice = st.radio("Navigation", ["Upload","Details"])
    st.info("This project application helps you detect Skin Cancer.")

if choice == "Upload":
    st.title("Upload The Photo You Want To Predict")
    file = st.file_uploader("Upload The Photo")
    if file:
        img = Image.open(file)#cv2.imread('file')
        #cv2.imshow(img)
        st.image(img,width=400)
        st.write(img.format,img.size,img.mode)
        
    
    

if choice == "Details":
    pass
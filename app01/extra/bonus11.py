# convert photos to grayscale

import streamlit as st
from PIL import Image # pillow

st.subheader("Color to Graysale Converter")

# let the user upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

def convert_to_grayscale(color_img):
    # create a pillow image instance
    img = Image.open(color_img)
    # convert image to grayscale
    gray_img = img.convert("L")
    return gray_img

if camera_image:
    # render the grayscale image on the webpage
    st.image(convert_to_grayscale(camera_image))

if uploaded_image:
    st.image(convert_to_grayscale(uploaded_image))
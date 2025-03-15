import streamlit as st
from PIL import Image

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)
    gray_img = img.convert('L')
    st.image(gray_img)
    
with st.expander("Start Camera"):

    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert('L')
    st.image(gray_img)
import streamlit as st
import os 
import PIL

def load_image():
    uploaded_file = st.sidebar.file_uploader(label='Pick an image to test')
    if uploaded_file and st.sidebar.button('Load'):
        img=PIL.Image.open(uploaded_file)
        exifdata=img._getexif()
        print (exifdata)
        with st.expander('Selected Image', expanded = True):
            st.image(img, use_column_width = True)
        st.subheader('Image Exchange Information')
        st.markdown(f'{exifdata}') 

def main():
    st.title('Digital Forensics Tool')
    st.sidebar.title("Upload an Image")
    load_image()

if __name__ == '__main__':
    main()
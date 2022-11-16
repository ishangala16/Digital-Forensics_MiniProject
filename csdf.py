#cmd to run this: C:\Users\hp\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\streamlit run CSDF\Digital-Forensics_MiniProject\csdf.py
import pandas as pd
import streamlit as st
import os 
import PIL
from PIL import Image
from PIL.ExifTags import TAGS


def load_image():
    uploaded_file = st.sidebar.file_uploader(label='Pick an image to test')
    if uploaded_file and st.sidebar.button('Load'):
        image=PIL.Image.open(uploaded_file)
        exifdata=image._getexif()
        print (exifdata)
        with st.expander('Selected Image', expanded = True):
            st.image(image, use_column_width = True)
        st.subheader('Image Exchange Information')
        #st.markdown(f'{exifdata}')

        info_dict = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }
        # df = pd.DataFrame(info_dict)
        # st.table(df)
        for label, value in info_dict.items():
            st.markdown(f"{label:25}: {value}")
        if exifdata != None:
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()
                st.markdown(f"{tag:25}: {data}")
        else:
            st.markdown('This image does not have metadata!!')


def main():
    st.title('Digital Forensics Tool')
    st.sidebar.title("Upload an Image")
    load_image()


if __name__ == '__main__':
    main()
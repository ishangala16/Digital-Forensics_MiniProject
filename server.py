import json
from flask import Flask, request, send_file
from PIL import Image
import PIL
from PIL.ExifTags import TAGS

app = Flask(__name__)
import pandas as pd
import numpy as np


@app.route("/metadata/<filename>", methods=["POST"])
def metadata(filename):
    image = Image.open(filename)
    exifdata=image._getexif()
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
    df = [info_dict]
    if exifdata != None:
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes
                if isinstance(data, bytes):
                    data = data.decode()
                df.append(f"{tag}: {data}")
    print((info_dict))

    # return jsonify({'msg': 'success', 'info': [info_dict]})
    return df
    

if __name__ == "__main__":
    app.run(debug=True)
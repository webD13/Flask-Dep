# import webbrowser
from flask import Flask, request, jsonify
from PIL import Image
# import os
# import boto3
# from pdf2image import convert_from_path
# from paddleocr import PaddleOCR

app = Flask(__name__)

# ocr_ar = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False, use_mkl=True, enable_mkldnn=False,  ocr_version='PP-OCRv4')

@app.route("/ocr_image", methods=["POST"])
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)
    img.save("temp.jpg") 
    result = ocr_ar.ocr("temp.jpg", cls=True)
    text, prop = getOCRtext(result)
    return jsonify({'msg': 'success', 'ocr': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=False)




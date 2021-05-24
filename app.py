import flask
from flask import Flask, render_template, request
import joblib
import os

import cv2
from cv2 import imread, resize

app = Flask(__name__)

#image_folder = os.path.join('images')
#app.config["UPLOAD_FOLDER"] = image_folder

#model = joblib.load('finalized_model.sav')

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')
'''
@app.route('/', methods=['POST'])
def predict():
  imagefile = request.files['imagefile']
  image_path = './images/' + imagefile.filename
  #imagefile.save(image_path)

  img = imread(image_path)
  img = resize(img, (100, 100)).flatten()
  image = img.reshape(-1, 1)
  pred = model.predict(image.T)

  #pic = os.path.join(app.config['UPLOAD_FOLDER'], imagefile.filename)

  if pred == 0:
    return render_template('index.html', prediction_text='{} is the image of Horse'.format(imagefile.filename))
  else:
    return render_template('index.html', prediction_text='{} is the image of Human'.format(imagefile.filename))
'''
app.run()

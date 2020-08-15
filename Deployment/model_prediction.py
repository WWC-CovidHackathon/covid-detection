from tensorflow.keras.models import model_from_json
import numpy as np
import cv2
from PIL import Image
import streamlit as st

@st.cache(show_spinner=False)
def load_model(model_json_file,model_weights_file):
  with open(model_json_file,"r") as json_file:
    model_json=json_file.read()
    model=model_from_json(model_json)
  model.load_weights(model_weights_file)
  return model

def preprocess(xray_file):
  xray_file=np.array(Image.open(xray_file).convert("RGB"))
  xray_file=cv2.resize(xray_file,(256,256))
  return xray_file

def predict_pathology(xray_file,model):
  xray_file=np.expand_dims(xray_file,axis=0)/255.
  pathology_prediction=model.predict(xray_file)[0]
  return pathology_prediction

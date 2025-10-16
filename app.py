import streamlit as st
import joblib
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Rossmann ", page_icon="⭕️", layout="centered")

st.logo(icon_image="Rossmann_Logo.svg")
st.title("Predict sales rate for Rossmann drugstore")
st.image('rossmann.jpeg')

st.header("Input here:")

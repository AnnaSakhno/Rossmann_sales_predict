import streamlit as st
import joblib
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Rossmann ", page_icon="⭕️", layout="centered")

st.title("Predict sales rate for Rossmann drugstore")
st.image('Rossmann_Logo.svg')

st.header("Input here:")

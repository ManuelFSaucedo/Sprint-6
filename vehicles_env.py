import pandas as pd
import plotly
import plotly_express as px
import streamlit as st
import numpy as np

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# crear un gráfico de dispersión
fig = px.scatter(car_data, x="odometer", y="price")
fig.show()  # crear gráfico de dispersión

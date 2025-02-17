import streamlit as st
import pandas as pd

st.title('🤖 Data Science Junior')

st.write('Hello Bro!')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expander("Data"):
  st.write("X")
  X_raw = df.drop('species', axis=1)
  st.dataFrame(X_raw)

  st.write("y")
  y_raw = df.species
  st.dataFrame(y_raw)

import streamlit as st
import matplotlib.pyplot as plt

st.title("GPS & LiDAR Attack Detection")

st.write("Visualization of anomaly detection")

x = [0, 20, 40, 60, 80, 100]
y = [1, 2, 4, 4, 4, 7]

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
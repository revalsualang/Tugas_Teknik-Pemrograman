import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualisasi Data Seismik")

# Data seismik contoh
np.random.seed(0)
n_time = 500
n_trace = 60
seismic = np.random.normal(0, 1, (n_time, n_trace))

# Sidebar
st.sidebar.header("Kontrol")

cmap = st.sidebar.selectbox(
    "Colormap",
    ["gray", "seismic", "viridis", "plasma", "inferno"]
)

scale_mode = st.sidebar.radio(
    "Scaling Mode",
    ["Auto", "Manual"]
)

if scale_mode == "Manual":
    vmin = st.sidebar.slider("vmin", -3.0, 0.0, -1.0)
    vmax = st.sidebar.slider("vmax", 0.0, 3.0, 1.0)
else:
    vmin = None
    vmax = None

flip_time = st.sidebar.checkbox("Balik sumbu waktu")

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
im = ax.imshow(
    seismic,
    aspect="auto",
    cmap=cmap,
    vmin=vmin,
    vmax=vmax
)

ax.set_xlabel("Trace")
ax.set_ylabel("Time Sample")

if flip_time:
    ax.invert_yaxis()

plt.colorbar(im, ax=ax, label="Amplitude")
st.pyplot(fig)

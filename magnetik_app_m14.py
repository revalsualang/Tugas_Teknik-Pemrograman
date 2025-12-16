import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Minggu 14 - Magnetik", layout="wide")
st.title("Visualisasi Anomali Magnetik – Minggu 14")

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y) * 100

st.sidebar.header("Pengaturan")

cmap = st.sidebar.selectbox(
    "Pilih Colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis"]
)

scale_mode = st.sidebar.radio(
    "Mode Skala",
    ["Auto", "Manual"]
)

vmin = st.sidebar.slider("vmin", -100.0, 0.0, -50.0)
vmax = st.sidebar.slider("vmax", 0.0, 100.0, 50.0)


if scale_mode == "Manual":
    vmin = st.sidebar.slider(
        "vmin",
        float(Z.min()),
        float(Z.max()),
        float(Z.min())
    )
    vmax = st.sidebar.slider(
        "vmax",
        float(Z.min()),
        float(Z.max()),
        float(Z.max())
    )
else:
    vmin = None
    vmax = None

fig, ax = plt.subplots()

if scale_mode == "Auto":
    im = ax.imshow(Z, cmap=cmap)
else:
    im = ax.imshow(Z, cmap=cmap, vmin=vmin, vmax=vmax)

plt.colorbar(im, ax=ax, label="nT")
ax.set_title("Peta Anomali Magnetik")

st.pyplot(fig)

if st.button("Simpan Gambar"):
    fig.savefig("peta_anomali_minggu14.png")
    st.success("Gambar berhasil disimpan!")

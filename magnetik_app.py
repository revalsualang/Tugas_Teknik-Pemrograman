import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Peta Anomali Magnetik")

# -----------------------------
# DATA CONTOH
# -----------------------------
np.random.seed(1)
nx, ny = 60, 60

anom_obs = np.random.normal(0, 50, (nx, ny))
anom_reg = np.random.normal(0, 20, (nx, ny))
anom_res = anom_obs - anom_reg

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("Kontrol Peta")

cmap = st.sidebar.selectbox(
    "Colormap",
    ["seismic", "viridis", "plasma", "inferno", "coolwarm"]
)

scale_mode = st.sidebar.radio(
    "Mode Scaling",
    ["Auto", "Manual"]
)

if scale_mode == "Manual":
    vmin = st.sidebar.slider("vmin (nT)", -150.0, 0.0, -50.0)
    vmax = st.sidebar.slider("vmax (nT)", 0.0, 150.0, 50.0)
else:
    vmin = None
    vmax = None

save_plot = st.sidebar.checkbox("Simpan plot sebagai gambar")

# -----------------------------
# PLOTTING
# -----------------------------
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

maps = [anom_obs, anom_reg, anom_res]
titles = ["Anomali Observasi", "Anomali Regional", "Anomali Residual"]

for ax, data, title in zip(axes, maps, titles):
    im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])

fig.colorbar(im, ax=axes.ravel().tolist(), label="nT")
st.pyplot(fig)

# -----------------------------
# SIMPAN GAMBAR
# -----------------------------
if save_plot:
    fig.savefig("anomali_magnetik.png", dpi=300, bbox_inches="tight")
    st.success("Plot disimpan sebagai anomali_magnetik.png")

# Tugas Teknik Pemrograman

**Nama** : Reval LD Sualang  
**NIM** : 124120022  
**Mata Kuliah** : Teknik Pemrograman  
**Dosen** : Nugroho Prasetyo  

---

## Deskripsi
Repository ini berisi tugas mata kuliah Teknik Pemrograman yang dikerjakan secara bertahap.
Aplikasi dibuat menggunakan Streamlit untuk visualisasi data geofisika, meliputi data seismik dan anomali magnetik.
Tugas mencakup implementasi visualisasi dasar (Minggu 13) serta pengembangan fitur interaktif (Minggu 14).

---

## Daftar Program
- **Minggu 13**
  - `seismic_app.py`  
    Visualisasi data seismik dengan pengaturan colormap, scaling, dan orientasi sumbu waktu.
  - `magnetik_app.py`  
    Visualisasi anomali magnetik dengan tiga komponen: observasi, regional, dan residual.

- **Minggu 14**
  - `magnetik_app_m14.py`  
    Pengembangan aplikasi magnetik berbasis Streamlit dengan fitur interaktif:
    - Dropdown pemilihan colormap
    - Pengaturan skala warna (vmin dan vmax)
    - Mode auto dan manual scaling
    - Fitur menyimpan hasil visualisasi sebagai gambar (PNG)

---

## Prasyarat
- Python 3.7+
- Streamlit
- NumPy
- Matplotlib
- Pandas

---

## Instalasi
```bash
pip install streamlit numpy matplotlib pandas

---
## Cara Menjalankan Program

### Minggu 13 – Aplikasi Seismik
```bash
python -m streamlit run seismic_app_m13.py
python -m streamlit run magnetik_app_m13.py
python -m streamlit run magnetik_app_m14.py

## Struktur Proyek
```text
Tugas_Teknik-Pemrograman/
├── README.md
├── seismic_app_m13.py          # Tugas Minggu 13
├── magnetik_app_m13.py         # Tugas Minggu 13
└── magnetik_app_m14.py     # Tugas Minggu 14
Berikut contoh **README.md** untuk proyek Python MVC pengolahan citra (grayscale → Sobel → threshold) lengkap dengan panduan penggunaan **virtual environment (venv)**.

Aplikasi Python sederhana dengan arsitektur **Model–View–Controller (MVC)** untuk:

* Input citra
* Konversi grayscale
* Deteksi tepi dengan operator Sobel
* Thresholding biner
* Tampilan GUI (Tkinter)

Menggunakan:

* OpenCV
* Tkinter
* Pillow

---

# 📁 Struktur Proyek

```
mvc-image-processing/
│
├── main.py
├── model.py
├── view.py
├── controller.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Persiapan Environment (venv)

## 1️⃣ Buat Virtual Environment

### Linux / Mac

```bash
python3 -m venv venv
```

### Windows

```bash
python -m venv venv
```

---

## 2️⃣ Aktifkan Virtual Environment

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

Jika berhasil aktif, prompt akan berubah:

```
(venv) your-folder$
```

---

# 📦 Install Dependency

Buat file **requirements.txt**

```
opencv-python
pillow
numpy
```

Install:

```bash
pip install -r requirements.txt
```

---

# ▶️ Menjalankan Program

```bash
python main.py
```

---

# 🖱️ Cara Pakai Aplikasi

1. Klik tombol **Load Image**
2. Pilih file gambar
3. Klik **Process Sobel**
4. Program akan memproses:

   * grayscale
   * sobel edge detection
   * threshold
5. Hasil ditampilkan di jendela

---

# 🧠 Arsitektur MVC

## Model

Berisi logika pemrosesan citra:

* load image
* grayscale
* sobel
* threshold
* source venv/bin/activate

## View

Berisi GUI Tkinter:

* tombol
* panel tampilan gambar

## Controller

Penghubung:

* tombol → model proses → view tampilkan

---

# 🧪 Versi Python

Disarankan:

```
Python 3.9+
```

Cek versi:

```bash
python --version
python -m unittest discover tests
python -m unittest tests/test_model.py

```

---

# 🧹 Keluar dari Virtual Environment

```bash
deactivate
```

---

# 🚀 Pengembangan Lanjutan (Opsional)

Bisa ditambahkan:

* slider threshold interaktif
* simpan hasil otomatis
* histogram citra
* perbandingan sebelum/sesudah
* versi web (Flask / Streamlit)
* batch processing folder gambar
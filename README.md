# 🧠 UTS Citra Digital - Noise Reduction pada Foto Pribadi (Grayscale)

Proyek ini merupakan tugas **UTS mata kuliah Citra Digital**, yang berfokus pada **pengurangan noise (noise reduction)** pada citra menggunakan beberapa teknik filter spasial di Python.  
Pada proyek ini, digunakan **foto pribadi** yang dikonversi ke **grayscale**, kemudian ditambahkan **salt & pepper noise**, dan dilakukan proses perbaikan citra menggunakan berbagai jenis filter.

---

## 📂 Struktur Proyek

```
📁 UTS_Citra_Digital
│
├── main.py              # Program utama (menggunakan foto pribadi grayscale)
├── foto_saya.jpg        # Foto pribadi yang digunakan
└── README.md            # Dokumentasi proyek
```

---

## ⚙️ Langkah-Langkah Program

### 1. Membaca Foto Pribadi
- Program membaca file gambar (`foto_saya.jpg`) dari folder lokal.
- Jika gambar berwarna, otomatis dikonversi ke **grayscale** menggunakan `rgb2gray()` dari `skimage.color`.

### 2. Menambahkan Noise
- Jenis noise yang digunakan: **Salt & Pepper**.
- Fungsi: `random_noise(image, mode='s&p', amount=0.1)`.

### 3. Penerapan Filter
Empat jenis filter digunakan untuk memperbaiki citra:
- **Mean Filter** → Rata-rata lokal
- **Min Filter** → Menghilangkan noise terang
- **Median Filter** → Efektif untuk Salt & Pepper noise
- **Max Filter** → Menghilangkan noise gelap

### 4. Evaluasi Hasil
Setiap hasil dibandingkan dengan citra asli menggunakan dua metrik:
- **PSNR (Peak Signal-to-Noise Ratio)** → Mengukur tingkat kebisingan.
- **SSIM (Structural Similarity Index)** → Mengukur kesamaan struktur antara dua citra.

---

## 📈 Hasil yang Ditampilkan

Program akan menampilkan 6 citra:
1. Citra asli (grayscale)  
2. Citra dengan noise  
3. Hasil Mean Filter  
4. Hasil Min Filter  
5. Hasil Median Filter  
6. Hasil Max Filter  

Selain itu, hasil evaluasi berupa nilai **PSNR** dan **SSIM** juga ditampilkan di terminal.

---

## 🧩 Contoh Output

```
=== Evaluasi Hasil ===
Noisy            -> PSNR: 20.48, SSIM: 0.7213
Mean Filtered    -> PSNR: 25.12, SSIM: 0.8427
Min Filtered     -> PSNR: 24.05, SSIM: 0.8169
Median Filtered  -> PSNR: 27.88, SSIM: 0.8902
Max Filtered     -> PSNR: 23.65, SSIM: 0.8103
```

> Berdasarkan hasil evaluasi, **Median Filter** biasanya memberikan hasil terbaik untuk mengurangi **salt & pepper noise**.

---

## 🧰 Library yang Digunakan

- `matplotlib` → Visualisasi hasil
- `numpy` → Operasi numerik
- `scikit-image (skimage)` → Proses citra (membaca gambar, menambah noise, filter, evaluasi)

---

## 🚀 Cara Menjalankan

1. Pastikan kamu sudah menginstal library berikut:
   ```bash
   pip install matplotlib numpy scikit-image
   ```
2. Simpan file **foto pribadi** (misalnya `foto_saya.jpg`) di folder yang sama.
3. Jalankan program:
   ```bash
   python main.py
   ```

---

## 🖼️ Contoh Tampilan Program

![Hasil Output](cake.png)

---

## ✍️ Penulis
**Nama:** Raihan Fathir  
**Mata Kuliah:** Citra Digital  
**Tugas:** Ujian Tengah Semester (UTS)  
**Topik:** Noise Reduction menggunakan Filter Spasial  

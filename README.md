# foto_kita_blurr

## Kamera Auto-Blur dengan Gesture ✌️✌️ (Peace Sign x2)

Script Python yang menggunakan OpenCV dan MediaPipe untuk mendeteksi gesture
peace sign (✌️) di dua tangan sekaligus. Jika kedua tangan membentuk peace
sign secara bersamaan, kamera akan otomatis memberikan efek blur pada frame.

## 🧰 Requirements

- Windows 10/11
- Python **3.11** (disarankan, karena MediaPipe versi stabil belum sepenuhnya
  kompatibel dengan Python 3.13)
- Webcam

## 🚀 Instalasi

### 1. Aktifkan Long Path Support (Windows)

Buka **PowerShell sebagai Administrator**, lalu jalankan:

```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled"
```

Jika diminta konfirmasi update setting saat instalasi Python, pilih `y`:

```
Update setting now? [y/N] y
```

> ⚠️ **Restart komputer** setelah mengaktifkan setting ini.

### 2. Install Python 3.11

1. Download installer dari halaman resmi:
   [https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)
2. Pilih **Windows installer (64-bit)**.
3. Klik kanan file installer → **Run as administrator**.
4. Centang ✅ **Add python.exe to PATH**.
5. Klik **Install Now**, tunggu sampai muncul **"Setup was successful"**.

### 3. Verifikasi instalasi Python 3.11

Buka terminal baru, lalu jalankan:

```powershell
py --list
```

Pastikan ada baris seperti:

```
-V:3.11
```

### 4. Install dependencies

```powershell
py -3.11 -m pip install opencv-python
py -3.11 -m pip install mediapipe==0.10.14
```

> ⚠️ **Wajib gunakan mediapipe versi `0.10.14`.** Versi lebih baru (0.10.30
> ke atas) memiliki bug yang menyebabkan `mediapipe.solutions` tidak bisa
> diakses (`AttributeError: module 'mediapipe' has no attribute 'solutions'`).

### 5. Tes instalasi MediaPipe

```powershell
py -3.11 -c "import mediapipe as mp; print(mp.solutions.hands)"
```

Output yang benar akan terlihat seperti ini (tanpa error):

```
<module 'mediapipe.python.solutions.hands' from '...\Lib\site-packages\mediapipe\python\solutions\hands.py'>
```

## ▶️ Menjalankan Program

```powershell
py -3.11 path/ke/peace_blur_camera.py
```

Contoh:

```powershell
py -3.11 c:/Users/ASUS/Downloads/peace_blur_camera.py
```

## 🎮 Cara Pakai

| Aksi | Hasil |
|------|-------|
| Tunjukkan **1 tangan** ✌️ | Teks hijau: `Tangan dengan peace sign terdeteksi: 1/2` |
| Tunjukkan **2 tangan** ✌️✌️ bersamaan | Frame ter-blur + teks merah `BLUR AKTIF` |
| Tekan `q` | Keluar dari program |

## 🛠️ Troubleshooting

| Error | Solusi |
|-------|--------|
| `pip is not recognized` | Gunakan `python -m pip ...` atau `py -3.11 -m pip ...` |
| `Python was not found` (padahal sudah install) | Matikan App Execution Alias: Settings → Apps → Advanced app settings → App execution aliases → matikan toggle untuk `python.exe` |
| `ModuleNotFoundError: No module named 'cv2'` | Install ulang: `py -3.11 -m pip install opencv-python` |
| `AttributeError: module 'mediapipe' has no attribute 'solutions'` | Uninstall mediapipe lalu install versi `0.10.14`: <br> `py -3.11 -m pip uninstall mediapipe -y` <br> `py -3.11 -m pip install mediapipe==0.10.14` |
| `No suitable Python runtime found` saat `py -3.11` | Python 3.11 belum terinstall dengan benar — install ulang sesuai langkah 2 |

## ⚙️ Kustomisasi

- **Tingkat blur**: ubah angka `(55, 55)` pada `cv2.GaussianBlur(frame, (55, 55), 0)` di dalam script (harus angka ganjil, makin besar makin blur).
- **Sensitivitas jempol**: saat ini jempol diabaikan dalam deteksi peace sign agar gesture lebih mudah dikenali.
- **Jumlah tangan**: ubah `max_num_hands=2` di `mp_hands.Hands(...)` jika ingin mendeteksi lebih banyak tangan.

## 📄 Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan pribadi maupun pembelajaran.

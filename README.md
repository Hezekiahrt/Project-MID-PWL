# 📱 Gadget Repair Monitoring API
**Proyek Ujian Tengah Semester (UTS) - Pemrograman Web Lanjutan**

Sistem RESTful API ini dirancang untuk mengotomatisasi pemantauan perbaikan perangkat digital pada sebuah toko servis. Aplikasi ini memfasilitasi teknisi dalam mengelola data pelanggan serta melacak detail pengerjaan perbaikan, status unit, dan biaya secara terintegrasi.

---

## 🚀 Fitur Utama
- **Autentikasi & Otorisasi JWT**: Mengamankan akses API menggunakan *JSON Web Token*. Pengguna harus login untuk melakukan perubahan data.
- **Manajemen Pelanggan**: Operasi CRUD untuk mendata identitas pelanggan tetap.
- **Monitoring Perbaikan**: Pelacakan status perbaikan perangkat secara *real-time* (Pending, In Progress, Completed).
- **Relasi Database (ORM)**: Implementasi relasi *One-to-Many* antara Pelanggan (Customer) dan Pekerjaan Perbaikan (Repair Job).
- **Validasi Skema**: Penggunaan Pydantic untuk memastikan data yang masuk sesuai dengan tipe dan batasan yang ditentukan.
- **Dokumentasi Otomatis**: Swagger UI interaktif yang dapat diakses langsung melalui endpoint `/docs`.

---

## 🛠️ Stack Teknologi
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Bahasa Pemrograman**: Python 3.12
- **Database**: SQLite (SQLAlchemy ORM)
- **Keamanan**: JWT (Python-Jose), Passlib (Bcrypt 3.2.2)
- **Web Server**: Uvicorn

---

## 📂 Struktur Proyek Modular
Proyek disusun mengikuti pola arsitektur modular untuk memisahkan tanggung jawab setiap komponen:

```text
.
├── auth/               # Logika enkripsi, hashing, dan pembuatan token JWT
│   └── security.py
├── models/             # Definisi tabel database menggunakan SQLAlchemy
│   ├── repair.py
│   └── user.py
├── routers/            # Definisi endpoint API (Routing) per domain
│   ├── auth.py
│   └── repair.py
├── schemas/            # Skema validasi data menggunakan Pydantic
│   ├── repair.py
│   └── user.py
├── database.py         # Konfigurasi koneksi & pembuatan session database
├── main.py             # Entry point utama aplikasi & registrasi router
├── requirements.txt    # Daftar dependensi library Python
└── README.md           # Dokumentasi proyek
```

---

## ⚙️ Panduan Instalasi & Penggunaan

### 1. Persiapan Lingkungan
Pastikan Anda sudah menginstal Python (disarankan versi 3.12).

### 2. Instalasi Library
Buka terminal di folder proyek dan jalankan perintah:
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi
Jalankan server menggunakan uvicorn:
```bash
uvicorn main:app --reload
```

### 4. Akses API
Buka browser dan kunjungi:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 📌 Dokumentasi Endpoint

### 🔑 Authentication (Publik)
- `POST /auth/register` — Mendaftarkan akun teknisi/admin baru.
- `POST /auth/login` — Masuk ke sistem untuk mendapatkan Access Token (Bearer).

### 👥 Customer Management
- `GET /customers/` — Menampilkan semua daftar pelanggan (Publik).
- `POST /customers/` — Menambah pelanggan baru (Membutuhkan Login).

### 🛠️ Repair Management
- `GET /jobs/` — Menampilkan semua daftar pekerjaan perbaikan (Publik).
- `POST /jobs/` — Menambah antrean perbaikan baru (Membutuhkan Login).
- `DELETE /jobs/{id}` — Menghapus data perbaikan dari sistem (Membutuhkan Login).

---

## 👤 Penulis

| Field | Detail |
|---|---|
| **Nama** | Hezekiah Reynard Tikupadang |
| **NIM** | H071241051 |
| **Program Studi** | Sistem Informasi |
| **Fakultas** | Fakultas MIPA |
| **Instansi** | Universitas Hasanuddin (UNHAS) |
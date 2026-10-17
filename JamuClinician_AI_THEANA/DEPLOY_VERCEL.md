# Panduan Deployment JamuClinician AI ke Vercel

Aplikasi **JamuClinician AI** telah disiapkan secara penuh untuk dideploy ke **Vercel** menggunakan arsitektur *Python WSGI Serverless Function* berbasis Flask dan static asset routing.

---

## 📁 Struktur File Khusus Vercel yang Telah Disiapkan

1. **`api/index.py`**
   * Entry point Serverless Function untuk Vercel.
   * Mengimpor instance Flask `app` dari `app.py`.
2. **`vercel.json`**
   * Mengatur routing dan *rewrites* URL.
   * File statis (`/static/...`) disajikan langsung melalui Vercel Edge CDN dengan latensi rendah.
   * Endpoint API (`/api/...`) dan halaman utama (`/`) diarahkan ke Python Serverless runtime (`api/index.py`).
3. **`requirements.txt`**
   * Berisi `Flask>=2.2.5` dan `Werkzeug>=2.2.3` yang akan diinstal otomatis oleh Vercel saat proses *build*.
4. **`.vercelignore`**
   * Mengabaikan file yang tidak dibutuhkan saat deployment (seperti `.env`, `.git`, `tests/`, cache Python).
5. **`package.json`**
   * Memuat skrip `"build"` agar Vercel mendeteksi proses build tanpa kendala.

---

## 🚀 Cara 1: Deploy via GitHub (Paling Direkomendasikan)

1. **Push Proyek ke Repository GitHub:**
   ```bash
   git init
   git add .
   git commit -m "feat: Siap deploy ke Vercel"
   git branch -M main
   git remote add origin https://github.com/USERNAME-ANDA/jamuclinician-ai.git
   git push -u origin main
   ```

2. **Buka Dashboard Vercel:**
   * Kunjungi [https://vercel.com/dashboard](https://vercel.com/dashboard) dan login.
   * Klik tombol **"Add New..."** $\rightarrow$ **"Project"**.
   * Pilih repository GitHub Anda (`jamuclinician-ai`), lalu klik **"Import"**.

3. **Konfigurasi Environment Variable (Gemini API Key):**
   * Pada halaman konfigurasi sebelum deploy, buka bagian **"Environment Variables"**:
     * **Key:** `GEMINI_API_KEY`
     * **Value:** *(Tempelkan Kunci API Gemini Anda di sini)*
   * Klik **"Add"**.

4. **Klik "Deploy":**
   * Vercel akan menginstal dependensi Python dan mengaktifkan Serverless Function secara otomatis.
   * Dalam hitungan detik, aplikasi Anda sudah live dengan URL publik (contoh: `https://jamuclinician-ai.vercel.app`).

---

## 💻 Cara 2: Deploy Cepat via Vercel CLI (Terminal)

Jika Anda sudah menginstal Node.js dan Vercel CLI di komputer Anda:

1. **Login ke Vercel:**
   ```bash
   npx vercel login
   ```

2. **Deploy Aplikasi:**
   ```bash
   npx vercel
   ```
   * Ikuti petunjuk interaktif (tekan Enter untuk opsi default).

3. **Deploy ke Production:**
   ```bash
   npx vercel --prod
   ```

4. **Tambahkan Gemini API Key via CLI:**
   ```bash
   npx vercel env add GEMINI_API_KEY
   ```
   * Masukkan nilai API Key Anda dan pilih environment `Production, Preview, Development`.

---

## 🔒 Catatan Keamanan & Fleksibilitas API Key
* Jika Anda tidak menyetel `GEMINI_API_KEY` di Vercel Dashboard, aplikasi tetap **100% berfungsi normal**:
  1. Pengguna dapat memasukkan Gemini API Key secara mandiri melalui modal integrasi di pojok kiri bawah UI (tersimpan aman di `localStorage` browser pengguna).
  2. Jika API Key tidak diisi sama sekali atau koneksi internet offline, sistem secara otomatis mengaktifkan **Dynamic EBM (Evidence-Based Medicine) Fallback Engine** lokal dengan akurasi klinis tinggi.

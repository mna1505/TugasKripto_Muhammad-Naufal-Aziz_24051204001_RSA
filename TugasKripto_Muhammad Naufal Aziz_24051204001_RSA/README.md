# Implementasi Algoritma RSA From Scratch (Python)

Repository ini berisi implementasi algoritma kriptografi **RSA (Rivest–Shamir–Adleman)** menggunakan Python tanpa library kriptografi eksternal.
Program dibuat untuk memahami proses **pembangkitan kunci, enkripsi, dan dekripsi** secara manual.

---

# Deskripsi Singkat

RSA merupakan algoritma kriptografi **kunci publik (asymmetric cryptography)** yang dikembangkan oleh:

- Ron Rivest
- Adi Shamir
- Leonard Adleman

pada tahun 1977.

Algoritma ini menggunakan dua kunci:

Public Key → digunakan untuk enkripsi
Private Key → digunakan untuk dekripsi

Keamanan RSA bergantung pada **kesulitan memfaktorkan bilangan besar**.

---

# Fitur Program

Program ini mengimplementasikan:

- Perhitungan **GCD (Greatest Common Divisor)**
- **Extended Euclidean Algorithm**
- Perhitungan **modular inverse**
- **Manual modular exponentiation**
- Enkripsi angka
- Enkripsi string
- Dekripsi ciphertext

---

# Cara Menjalankan Program

## 1. Clone Repository

```
git clone https://github.com/USERNAME/rsa-from-scratch.git
```

## 2. Masuk ke Folder Project

```
cd rsa-from-scratch
```

## 3. Jalankan Program

Pastikan Python sudah terinstall.

```
python rsa.py
```

atau

```
python3 rsa.py
```

---

# Contoh Output Program

```
=== PEMBANGKITAN KUNCI RSA ===
Nilai p = 61
Nilai q = 53

Nilai n (p * q) = 3233
Nilai totient (φ(n)) = 3120

Public Key  (e, n) = (19, 3233)
Private Key (d, n) = (2299, 3233)

=== ENKRIPSI ANGKA ===
Plaintext  = 123
Ciphertext = 855
Hasil Dekripsi = 123

=== ENKRIPSI STRING ===
Plaintext  = NAUFAL
Ciphertext = [...]
Hasil Dekripsi = NAUFAL
```

---

# Struktur Algoritma RSA

### Key Generation

1. Pilih dua bilangan prima `p` dan `q`
2. Hitung `n = p × q`
3. Hitung `φ(n) = (p−1)(q−1)`
4. Pilih `e` sehingga `gcd(e, φ(n)) = 1`
5. Hitung `d` dengan modular inverse

### Enkripsi

```
C = M^e mod n
```

### Dekripsi

```
M = C^d mod n
```

---

# Tujuan Proyek

Tujuan utama project ini adalah untuk memahami:

- konsep dasar **kriptografi kunci publik**
- cara kerja **RSA secara matematis**
- implementasi algoritma kriptografi tanpa library eksternal

---

# Catatan

Implementasi ini hanya untuk **tujuan pembelajaran**.
RSA yang digunakan pada sistem keamanan nyata menggunakan:

- bilangan prima sangat besar (2048 bit atau lebih)
- teknik padding seperti OAEP
- optimasi algoritma tambahan

---

# Author

Muhammad Naufal Aziz
Tugas Mata Kuliah Kriptografi

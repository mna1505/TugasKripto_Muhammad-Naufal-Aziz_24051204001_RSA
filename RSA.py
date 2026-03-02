# =====================================
# RSA FROM SCRATCH - FULL IMPLEMENTATION
# ANGKA + STRING (MANUAL)
# =====================================

# ==============================
# LANGKAH 1: Pilih bilangan prima
# ==============================

p = 61
q = 53

print("=== PEMBANGKITAN KUNCI RSA ===")
print("Nilai p =", p)
print("Nilai q =", q)


# ==============================
# LANGKAH 2: Hitung n
# ==============================

n = p * q
print("Nilai n (p * q) =", n)


# ==============================
# LANGKAH 3: Hitung totient
# ==============================

totient_n = (p - 1) * (q - 1)
print("Nilai totient (φ(n)) =", totient_n)


# ==============================
# LANGKAH 4: Pilih e
# ==============================

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

e = 19

print("Nilai e =", e)
print("gcd(e, totient_n) =", gcd(e, totient_n))


# ==============================
# LANGKAH 5: Cari d
# ==============================

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd_value, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_value, x, y


def modular_inverse(e, totient):
    gcd_value, x, y = extended_gcd(e, totient)

    if gcd_value != 1:
        return None
    else:
        return x % totient


d = modular_inverse(e, totient_n)

print("Nilai d =", d)

print("\nPublic Key  (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))


# =====================================
# MODULAR EXPONENTIATION (MANUAL)
# =====================================

def mod_exp(base, exponent, modulus):

    result = 1
    base = base % modulus

    while exponent > 0:

        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent // 2
        base = (base * base) % modulus

    return result


# =====================================
# ENKRIPSI ANGKA
# =====================================

def encrypt_number(message, e, n):
    return mod_exp(message, e, n)


# =====================================
# DEKRIPSI ANGKA
# =====================================

def decrypt_number(ciphertext, d, n):
    return mod_exp(ciphertext, d, n)


print("\n=== ENKRIPSI & DEKRIPSI ANGKA ===")

message_number = 123
print("Plaintext  =", message_number)

cipher_number = encrypt_number(message_number, e, n)
print("Ciphertext =", cipher_number)

decrypt_number_result = decrypt_number(cipher_number, d, n)
print("Hasil Dekripsi =", decrypt_number_result)


# =====================================
# ENKRIPSI STRING
# =====================================

def encrypt_string(plaintext, e, n):

    ciphertext_list = []

    for char in plaintext:

        ascii_value = ord(char)

        encrypted_char = mod_exp(ascii_value, e, n)

        ciphertext_list.append(encrypted_char)

    return ciphertext_list


# =====================================
# DEKRIPSI STRING
# =====================================

def decrypt_string(cipher_list, d, n):

    plaintext = ""

    for encrypted_char in cipher_list:

        decrypted_ascii = mod_exp(encrypted_char, d, n)

        plaintext += chr(decrypted_ascii)

    return plaintext


print("\n=== ENKRIPSI & DEKRIPSI STRING ===")

message_text = "NAUFAL"
print("Plaintext  =", message_text)

cipher_text = encrypt_string(message_text, e, n)
print("Ciphertext =", cipher_text)

decrypt_text = decrypt_string(cipher_text, d, n)
print("Hasil Dekripsi =", decrypt_text)
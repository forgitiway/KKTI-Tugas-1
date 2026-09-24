ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

NOTCH = {
    "I": "Q",
    "II": "E",
    "III": "V"
}

ROTOR = {
    "I": ROTOR_I,
    "II": ROTOR_II,
    "III": ROTOR_III
}

def inverse_wiring(wiring):
    hasil = ""
    for huruf in ALFABET:
        posisi = wiring.index(huruf)
        hasil += ALFABET[posisi]
    return hasil

def plugboard(huruf):
    pasangan = {
        "J": "Z",
        "Z": "J",
        "T": "A",
        "A": "T"
    }
    if huruf in pasangan:
        return pasangan[huruf]
    return huruf

def lewat_rotor(huruf, nama_rotor, posisi, ring):
    wiring = ROTOR[nama_rotor]
    nilai = ALFABET.index(huruf)
    nilai = (nilai + posisi - ring) % 26
    huruf = wiring[nilai]
    nilai = (ALFABET.index(huruf) - posisi + ring) % 26
    return ALFABET[nilai]

def lewat_rotor_balik(huruf, nama_rotor, posisi, ring):
    wiring = inverse_wiring(ROTOR[nama_rotor])
    nilai = ALFABET.index(huruf)
    nilai = (nilai + posisi - ring) % 26
    huruf = wiring[nilai]
    nilai = (ALFABET.index(huruf) - posisi + ring) % 26
    return ALFABET[nilai]

def dekripsi_enigma(ciphertext):

    rotor_kiri = "II"
    rotor_tengah = "III"
    rotor_kanan = "I"

    ring_kiri = ALFABET.index("B")
    ring_tengah = ALFABET.index("Q")
    ring_kanan = ALFABET.index("D")

    posisi_kiri = ALFABET.index("R")
    posisi_tengah = ALFABET.index("T")
    posisi_kanan = ALFABET.index("I")

    hasil = ""
    for karakter in ciphertext:
        if ALFABET[posisi_tengah] == NOTCH[rotor_tengah]:
            posisi_kiri = (posisi_kiri + 1) % 26
            posisi_tengah = (posisi_tengah + 1) % 26
        if ALFABET[posisi_kanan] == NOTCH[rotor_kanan]:
            posisi_tengah = (posisi_tengah + 1) % 26

        posisi_kanan = (posisi_kanan + 1) % 26

        huruf = plugboard(karakter)
        
        huruf = lewat_rotor(huruf, rotor_kanan, posisi_kanan, ring_kanan)

        huruf = lewat_rotor(huruf, rotor_tengah, posisi_tengah, ring_tengah)

        huruf = lewat_rotor(huruf, rotor_kiri, posisi_kiri, ring_kiri)

        huruf = REFLECTOR_B[ALFABET.index(huruf)]

        huruf = lewat_rotor_balik(huruf, rotor_kiri, posisi_kiri, ring_kiri)

        huruf = lewat_rotor_balik(huruf, rotor_tengah, posisi_tengah, ring_tengah)

        huruf = lewat_rotor_balik(huruf, rotor_kanan, posisi_kanan, ring_kanan)

        huruf = plugboard(huruf)

        hasil += huruf

    return hasil

ciphertext = "GFVTKNPFCEQZOPEYMLENTSRYUJUXNUKXDSZHWZRRQBDKGQ"

plaintext = dekripsi_enigma(ciphertext)

print("Ciphertext:")
print(ciphertext)

print("\nPlaintext:")
print(plaintext)
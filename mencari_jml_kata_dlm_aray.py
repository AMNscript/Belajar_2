def hitung_kata_sama(arr):
    kata_sama = {}
    
    for kata in arr:
        if kata in kata_sama:
            kata_sama[kata] += 1
        else:
            kata_sama[kata] = 1
    
    return kata_sama

# Contoh penggunaan
array_kata = ['apel', 'jeruk', 'apel', 'mangga', 'apel', 'jeruk']
hasil = hitung_kata_sama(array_kata)

for kata, jumlah in hasil.items():
    print(f"Kata '{kata}' muncul sebanyak {jumlah} kali.")

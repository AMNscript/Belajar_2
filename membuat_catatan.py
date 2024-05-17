import os


def buat_catatan():
    judul = input("Masukkan judul catatan: ")
    isi = input("Masukkan isi catatan: ")

    # Membuat atau membuka file catatan
    with open(f"{judul}.txt", "w") as file:
        file.write(isi)

    print("Catatan telah dibuat.")

def lihat_catatan():
    judul = input("Masukkan judul catatan yang ingin dilihat: ")

    # Mengecek apakah file catatan ada
    if os.path.exists(f"{judul}.txt"):
        with open(f"{judul}.txt", "r") as file:
            isi = file.read()
            print(f"===== {judul} =====")
            print(isi)
    else:
        print("Catatan tidak ditemukan.")

def edit_catatan():
    judul = input("Masukkan judul catatan yang ingin diedit: ")

    # Mengecek apakah file catatan ada
    if os.path.exists(f"{judul}.txt"):
        with open(f"{judul}.txt", "r") as file:
            isi_lama = file.read()
            print(f"Isi catatan lama:\n{isi_lama}")

        isi_baru = input("Masukkan isi catatan baru: ")
        with open(f"{judul}.txt", "w") as file:
            file.write(isi_baru)

        print("Catatan telah diubah.")
    else:
        print("Catatan tidak ditemukan.")

def hapus_catatan():
    judul = input("Masukkan judul catatan yang ingin dihapus: ")

    # Mengecek apakah file catatan ada
    if os.path.exists(f"{judul}.txt"):
        os.remove(f"{judul}.txt")
        print("Catatan telah dihapus.")
    else:
        print("Catatan tidak ditemukan.")
        
#fungsi mengubah judul
def ubah():
    jadul = input("Masukkan judul catatan yang ingin diubah: ")

    # Mengecek apakah file catatan ada
    if os.path.exists(f"{jadul}.txt"):
        judul_baru = input("Masukkan judul baru: ")
        os.rename(f"{jadul}.txt", f"{judul_baru}.txt")
        print(f"Anda sudah mengganti {jadul}.txt menjadi {judul_baru}.txt")
    else:
        print("Catatan tidak ditemukan.")


def menu_utama():
    while True:
        print("\n===== MANAJEMEN CATATAN =====")
        print("1. Buat catatan")
        print("2. Lihat catatan")
        print("3. Edit catatan")
        print("4. Hapus catatan")
        print("5. Mengubah judul")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            buat_catatan()
        elif pilihan == "2":
            lihat_catatan()
        elif pilihan == "3":
            edit_catatan()
        elif pilihan == "4":
            hapus_catatan()
        elif pilihan == "5":
        	ubah()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

menu_utama()

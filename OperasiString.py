kalimat = "HiI ApAkABAr NiH"

#untuk mengecilkan huruf
print ("menjadikan huruf kecil")
print(kalimat.lower())

#untuk menjadikan huruf besar
print("menjadikan huruf besar")
a = kalimat.upper()
print(a)

#untuk mengecek ada huruf besar atau tdk

CekUper = kalimat.isupper()
print("cek " + str(CekUper))

#menghilangkan tanda , dan spasi
Cek = a.split(',') and a.split(' ')
print (Cek)

#untuk mengetahui berapa indeks dilam variabel Cek
z= len(Cek)
print(z)


Joinlah = "1234".join(Cek)
print (Joinlah)

#alokasi kata ljust,rjust,center
b= "wow".ljust(20)
print("_",b,"_")
c="wow".center(20,"_")
print ("_",c,"_")
d="wow".rjust(20)
print("_",d,"_")

#strip untuk menghilangkan alokasi
e = c.strip("_") #untuknmenghilangkan tanda _
print ("_",e,"_")
f = b.strip(" ")
print("_",f,"_")
g = d.strip(" ")
print("_",g,"_")





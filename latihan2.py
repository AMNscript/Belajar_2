exe = """Ha-ha-ha..., satu organisasi yang bagi saya tak pernah didengar kiprahnya yakni Perhimpunan Korban Mafia Hukum dan Ketidakadilan (Perkomhan) tiba-tiba menggugat Saya sebagai Menko Polhukam ke Pengadilan Negeri Jakarta Pusat dengan gugatan perbuatan melawan hukum. Katanya saya telah melakukan perbuatan melanggar hukum karena mengomentari putusan PN Jakpus yang memenangkan gugatan Partai PRIMA untuk menunda tahapan pemilu," kata Mahfud, dalam keterangannya, Kamis (15/6/2023)."""
exe = exe.replace("-"," ")
exe = exe.replace(","," ")
exe = exe.replace("."," ")
exe = exe.replace("/"," ")
exe = exe.replace("("," ")
exe = exe.replace(")"," ")
exe = exe.replace('"',' ')
#exe = exe.replace(" ","")
e = exe.split(" ")

print (e)
print (len(e))

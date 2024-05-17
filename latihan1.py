UsrInput = float(input("masukan angka = "))

#--0++5--8++11--

KurangDari5 = UsrInput < 5
print (UsrInput,"kurang dari 5 = ",KurangDari5)

LebihDari8 = UsrInput >8
print (UsrInput," lebih dari 8 = ",LebihDari8)

KurangDari0 = UsrInput < 0
print (UsrInput," kurang dari 0 = ",KurangDari0)

LebihDari11 = UsrInput >11
print (UsrInput," lebih dari 11 = ",LebihDari11)


LimaSampai8 = KurangDari5 or LebihDari8

fulll = KurangDari0 or LimaSampai8 or LebihDari11

#print ("++5--8++")
#print (LimaSampai8)

print ("--0++5--8++11--")
print(fulll)
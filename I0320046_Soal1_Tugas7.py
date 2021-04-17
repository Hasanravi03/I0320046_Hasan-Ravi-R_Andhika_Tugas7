#METODE CENTER
Judul = "Survei Pelayanan Rumah Sakit Haji Jakarta"
a = Judul.center (50,'=')
print (a)

#METODE ENDSWITH
str = "Apakah Pelayananannya Ramah?"
print("Apakah Pelayananannya Ramah?")
print (str.endswith("Ramah?"))

#METODE REPLACE AND ENDSWITH
str = "Apakah Pasien Merasa Puas?"
b = str.replace ("Puas","Senang")
print(b)
print(str.endswith("Puas?"))
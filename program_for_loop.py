# Membuat program for_loop, list dan range

banyak = int(input("berapa banyak data?"))

nama = []
umur = []

for i in range(0, banyak):
    print(f"data ke {1}")
    input_nama = input ("Nama :")
    input_umur = int(input("Umur :"))
    
    nama.append(input_nama)
    umur.append(input_umur)
    
for i in range(0,len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")
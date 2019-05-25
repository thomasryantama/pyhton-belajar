lama=int(input("Lama menginap : "))
harga = int(input("Harga kamar  :"))
jumlah= lama*harga
if jumlah > 300000:
    if harga > 50000:
        keterangan = "Dapat Kartu Diskom"
    else : keterangan= "tidak apat kartu"

else :
    keterangan = " tidak dapat kartu diskon"
    if lama > 3:
        bayar = jumlah- (jumlah*0.3)
    else :
        bayar = jumlah
print("Jumlah = ", jumlah)
print (" Keterangan = ", keterangan)
print ("Bayar = ", bayar)

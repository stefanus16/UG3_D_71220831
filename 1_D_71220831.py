Hujan = (input("Masukkan nilai curah hujan: ")).lower().split(" ")

curah = ("Cuaca terang/berawan" if Hujan == 0 and Hujan <= 0.4 else(print("Cuaca hujan ringan" if Hujan == 0.5 and Hujan <= 20 else(print("Curah hujan sedang" if Hujan == 21 and Hujan <= 50 else(print("Curah hujan lebat" if Hujan == 51 and Hujan <= 100 else(print("Curah hujan ekstrem" if Hujan > 100 else(print("Curah hujan lebat")))))))))))



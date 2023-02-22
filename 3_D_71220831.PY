awal = int(input('masukan awal deret: '))
akhir = int(input('masukan akhir deret: '))
 
for i in range(awal,akhir+1):
  if (i % 2 == 0):
    print(i, end=" ")
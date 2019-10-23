panjang = int(input("masukkan panjang:"))
miring = int(input("masukkan miring:"))
for j in range(miring,0,-1):
    for k in range(0,j-i):
        print(" ",end="")
    for l in range(0,panjang):
        print("*",end="")
    print()
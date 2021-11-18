nilaia = input("Nilai a :")
nilaib = input("Nilai b :")
nilaic = input("Nilai c :")

nilaid = (int(nilaib)**2)-(4*int(nilaia)*int(nilaic))
x1 = (-int(nilaib)-(nilaid**(1.0/2)))/2*int(nilaia)
x2 = (-int(nilaib)+(nilaid**(1.0/2)))/12*int(nilaia)
if(nilaid<0):
    print("Fungsi tersebut tidak memiliki akar riil")
elif(nilaid>0):
    print("Akar akar dari persamaan tersebut adalah "+str(x1)+" dan "+str(x2))
else:
    print("Fungsi tersebut memiliki akar kembar yaitu "+str(x1))
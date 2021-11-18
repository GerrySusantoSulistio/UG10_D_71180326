bilangan1 = input("Masukan bilangan 1 : ")
bilangan2 = input("Masukan bilangan 2 : ")
bilangan3 = input("Masukan bilangan 3 : ")
sort = ["","",""]
if(int(bilangan1) > int(bilangan2) and int(bilangan1) > int(bilangan3)):
    sort[0] = bilangan1
    if(int(bilangan2) > int(bilangan3)):
        sort[1] = bilangan2
        sort[2]=bilangan3
    else:
        sort[1] = bilangan3
        sort[2] = bilangan2
elif(int(bilangan2) > int(bilangan1) and int(bilangan2) > int(bilangan3)):
    sort[0] = bilangan2
    if(int(bilangan1) > int(bilangan3)):
        sort[1] = bilangan1
        sort[2] = bilangan3
    else:
        sort[1] = bilangan3
        sort[2] = bilangan1
else:
    sort[0] = bilangan3
    if(int(bilangan1) > int(bilangan2)):
        sort[1] = bilangan1
        sort[2] = bilangan2
    else:
        sort[1] = bilangan2
        sort[2] = bilangan1

print("Urutan bilangan dari yang terbesar adalah " + sort[0]+" "+sort[1]+" "+sort[2])
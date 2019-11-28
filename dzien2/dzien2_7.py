#konwerter zamiana iczby na rzymską
numbers={
    0:"0", 1:"I", 2:"II",3:"III",4:"IV",5:"V"
}
decNum = input("Podaj cyfrę 0-5   ")
if(decNum.isdecimal()):
    decNum = int(decNum)
    if (decNum >= 0 and decNum <= 5):
        print(numbers[int(decNum)])
    else:
        print("Liczba jest spoza zakresu 0-5")
else:
    print("Błędne dane")
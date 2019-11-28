liczby_dict = {}
liczby_dict["jeden"] = 1
liczby_dict["dwa"] = 2
liczby_dict["trzy"] = 3
liczby_dict["cztery"] = 4
liczby_dict["pięć"] = 5

print(liczby_dict)

liczba=input("Napisz słownie cyfrę 1-5 np jeden  ").lower()
if(liczba in liczby_dict):
    print(liczby_dict[liczba])
else:
    print("Ogarnij się!!!")
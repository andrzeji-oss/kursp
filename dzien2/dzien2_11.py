# z podanej daty urodzenia wydobywamy rok yyyy-mm-dd
# na podstawie obliczonego wieku sprawdź czy użytkowni jest pełnoletni
# jeżeli age >=18, to wypisz pełnoletni
# jeżeli age <18, to wypisz niepełnoletni
# jeżeli wiek nie zawiera się w przedziale 0-120 to wypisz "jesteś robotem"
# dodatkowo zadbaj o walidację wprowadzanych danych
from datetime import date
today = date.today()

birthDate = input("Podaj datę urodzenia w formacie yyyy-mm-dd  ")
year = birthDate[:4] # bierzemy pierwszy 4 znaki z wprowadzenia
if(year.isdecimal()):
    # zrzutuj rok na int
    validYear = int(year)
    age = today.year - validYear
    if (age >=18 and age <=120):
        print("jesteś pełnoletni")
    elif (age < 18 and age >= 0):
        print("jesteś niepełnoletni")
    else:
        print("jesteś robotem")
else:
    print("Niepoprawna data urodzenia")






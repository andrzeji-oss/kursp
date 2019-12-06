# importy są adresowane od katalogu domowego -> nazwa projektu
# nazwa modułu(skryptu) występuje bez rozszerzenia
# aliast zastepuje wsystko to jest w adresie modulu razem z nazwa
import dzien6.imports.SecretVariables as sv


# dostęp do zmiennych
print(sv.dataBase)
print(sv.username)
print(sv.password)
print(sv.host)
print(sv.port)

# dostęp do metod
print(sv.getConnection())

# dostep do klas
obiektKlasyZaimportowanej = sv.Hello("Andrzej")
print(obiektKlasyZaimportowanej)
print(obiektKlasyZaimportowanej.name)



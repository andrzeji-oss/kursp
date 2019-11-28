# admin : admin - przejdz do panelu administatora
# user : user - panel uzytkownika
# else: wyświetl stosowny komunikat

logins = {"user" : "user", "admin" : "admin" }
user = input("podaj nazwę użytkownika")
password  = input("podaj hasło")

if (user not in logins.keys()):
    print("błedny login")
elif(logins[user] == password):
    print("zalogowano")
else:
    print("błędny login i hasło")





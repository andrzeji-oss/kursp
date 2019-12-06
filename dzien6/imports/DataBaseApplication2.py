# import z określonych lokalizacji konkretnych składowych
# składowe są dostępne bez adresowania
from dzien6.imports.SecretVariables import dataBase, username, password, Hello
from dzien6.imports.SecretVariables import getConnection


print(username)
print(dataBase)
print(password)

print(getConnection())

h = Hello("Anderzej")
print(h)
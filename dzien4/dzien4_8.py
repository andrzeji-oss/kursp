# wywolywanie na zmianę bialy i czarny
# funkcja odwolujaca sie do obiektu globalnie zadeklarowanego w skrypcie

def returnColour():
    global value         # pobieram wartość globalną
    value = not value       # modyfikuję wartość globalną
    return "black" if value else "white"

value = True

print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
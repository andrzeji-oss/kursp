# ile jest słów unikatowych

zdanie = input("Wprowadź jakieś zdanie ")
words = zdanie.split(" ") #dzieli zdanie na spacje
unique_words = set(words)

print("Ilość unikatow słow: ", len(unique_words))
print("ilość powtórzeń: ", len(words) - len(unique_words))
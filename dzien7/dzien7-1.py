import re
import os
import time

pattern1 = re.compile("^[d]")      # zaczyna się od d
print(pattern1.match("dog"))

pattern1 = re.compile("^[dD].{1,}[gG]$")    # zaczyna się na d lub D i kończy na g lub G
print(pattern1.match("DoG"))
print(pattern1.match("d%g",))

postalCode = "88 - 999"
result = re.search("^[0-9]{2}\s-\s[0-9]{3}", postalCode)
if (result is None):
    print("Błąd kodu pocztowego")
else:
    print("jest ok")

filePattern = re.compile(".*[\.]{1}(pdf|ppt|pptx)$")
path = "D:\\Moje Dokumenty"
os.chdir(path)
for file in os.listdir('.'):
    if (re.search(filePattern, file)):
        print("%50s | %10.2f MB" % (file, os.path.getsize(file)/(10**6)), time.ctime((os.path.getctime(file))))
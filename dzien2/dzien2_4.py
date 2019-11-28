data_waznosci = [(1, 1, 2018),(10,10,2018),(5,3,2020)]

while(True):
    inputDate = input("Wprowadź datę w formacie dd-mm-yyyy lub q wyjdź  ")
    if(inputDate == "q"):
        break
    data_waznosci.append(inputDate.split("-"))

print("Data ważności artykułu: "+ str(data_waznosci[0][0]) + "-" + str(data_waznosci[0][1]) + "-" + str(data_waznosci[0][2]))
print("Data ważności artykułu: "+ str(data_waznosci[1][0]) + "-" + str(data_waznosci[1][1]) + "-" + str(data_waznosci[1][2]))
print("Data ważności artykułu: "+ str(data_waznosci[2][0]) + "-" + str(data_waznosci[2][1]) + "-" + str(data_waznosci[2][2]))
print("Data ważności artykułu: "+ str(data_waznosci[3][0]) + "-" + str(data_waznosci[3][1]) + "-" + str(data_waznosci[3][2]))

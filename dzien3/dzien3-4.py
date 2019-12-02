# program wyświetlający tabelę przeliczeń z celcjusza na fahrenheita -20, +40, co 5 stopni
# f=32+9/5 c

# definicja
def celciusToFarenheit(celciusDegree):
    return 32 + (9 * celciusDegree)/5

def temperatureTable(start, stop, step):
    print("| %5s | %6s |" % ("C", "F"))
    for celciusDegree in range(stop, start - step, -step):
        if (celciusDegree == 0):
            print("| %5i | %6.1f |" % (celciusDegree, celciusToFarenheit(celciusDegree)))
        else:
            print("| %+5i | %6.1f |" % (celciusDegree, celciusToFarenheit(celciusDegree)))

temperatureTable(10,20,1)
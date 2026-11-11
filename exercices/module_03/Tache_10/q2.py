def temperature(celsius):
    f = celsius * 9 / 5 + 32
    round(f, 2)
    #arrondis les valeurs pour avoir seulement 2 decimales.
    k = celsius + 273.15
    round(k, 2)
    #les conversions

    return celsius, f, k
print("Les températures celsius, fahrenheit et kelvin sont :" ,temperature(celsius = float(input("entrer un température celsius :"))))

def przelicz(data, temperature_type):
    print("{0}C = ".format(data))
    if temperature_type == "f":
        fahreinheit = data * 1.8 + 32
        print("{0}F".format(round(fahreinheit,2)))
    elif temperature_type == "r":
        rankine = (data + 273.15) * (9 / 5)
        print("{0}R".format(round(rankine,2)))
    elif temperature_type == "k":
        kelvin = data + 273.15
        print("{0}K".format(round(kelvin,2)))
    else:
        print("zla litera")


przelicz(5, "k")

def umrech(input_zahl, input_einheit):
    try:
        input_zahl = float(input_zahl)
    except ValueError:
        raise Exception("keine zahl")
    match input_einheit:
        case "ft" | "foot":
            meter = input_zahl * 0.3048
            kmeter = meter * 0.001
            return meter, kmeter, "m"
        case "mi" | "mile":
            meter = input_zahl * 1609.344
            kmeter = meter * 0.001
            return meter, kmeter, "m"
        case "m" | "meter":
            foot = input_zahl * 3.28084
            mile = input_zahl / 1609.344
            return foot, mile, "i"
        case "km" | "kilometer":
            foot = input_zahl * 3280.8399
            mile = input_zahl * 0.62137
            return foot, mile, "i"
        case _:
            raise Exception("Ungültige eingabe. Nutze: ft, mi, m, km!")


while(True):
    print(
"""---------------------------------------
Längenumrecher Imperial / Metrisch
bitte gebe deine umzurechnende Zahl ein. (--> <Zahl> <Einheit>)
zum Beenden [q/Q]""")
    eingabe = input().strip()
    
    if eingabe == "q" or eingabe == "Q":
        exit(0)
    try:
        zahl, einheit = eingabe.split()
    except ValueError:
        print("Bitte im Format: <Zahl> <Einheit> eingeben, z.B. 10 ft")
        continue
    #print(f"t1 = {zahl}\n")
    #print(f"t2 = {einheit}")
    try:
        ein, zwei, einh = umrech(zahl, einheit)
        match einh:
            case "m":
                print(f"\n--> Meter: {ein}\n")
                print(f"--> Kilometer: {zwei}\n")
            case "i":
                print(f"\n--> Foot: {ein}\n")
                print(f"--> Mile: {zwei}\n")
    except Exception as err:
        print(f"Fehler beim umrechen!\n {err}")

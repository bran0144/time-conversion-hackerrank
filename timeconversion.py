# Hackerank solution to TIme Conversion

def timeConversion(s):
    if s[-2] == "A" and s[:2] == "12":
        hour = int(s[:2]) - 12
        return str(hour) +"0"+ s[2:8]
    elif s[-2] == "A":
        return str(s[:8])
    elif s[-2] == "P" and s[:2] == "12":
        return str(s[:8])
    elif s[-2] == "P":
        hour_24 = int(s[:2]) + 12
        return str(hour_24) + s[2:8]


def transformatioIpv4(ip):
    p = []
    for elemento in ip.split("."):
        p.append(int(elemento, 2))
    return p
def transformationIpv6(ip):
    p = []
    for elemento in ip.split(":"):
        p.append(hex(int(elemento, 2)))  
    return p
def transformationIpv6(ip):
    hexadecimal = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'
    }

    p = []
    for i in ip.split(":"):
        binario = "" 
        for j in i:
            binario += hexadecimal[j]
        p.append(binario)
    return p

resultado = transformationIpv6("f001:0d:b840:42:a2:0:1")
ip_binario = ":".join(resultado)
print(ip_binario)

resultado = transformationIpv6("0010000000000001:0000110110111000:0100001010100010:0000000000000001")
ip_hexadecimal = ":".join(resultado)
print(ip_hexadecimal)

resultado = transformatioIpv4("00001010.00001010.00001010.00001111")
ip_decimal = ".".join(map(str, resultado))
print(ip_decimal)
while True:
    ipaddress = input("введите ip адресс:")
    octets = ipaddress.split('.')
    correct_ip = True

    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                correct_ip = False
                break
    else:
        correct_ip =False
    if correct_ip:
        break
    print("Неправильный ip адресс!")


first_octet = int(octets[0])
    
if 1 <= first_octet <= 223:
    print("unicast")
elif ipaddress == "0.0.0.0":
    print("unassigned")
elif 224 <= first_octet <= 239:
    print("multicast")
elif ipaddress == '255,255,255,255':
    print("Broadcast")
else:
    print("unused")
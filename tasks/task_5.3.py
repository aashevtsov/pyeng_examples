access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
template = {'access':access_template,'trunk':trunk_template}
question = {'access': "Введите норме влана: ",'trunk': "введите разрешенные вланы: "}

mode = input("Ввежите режим работы интерфейса: ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input(question[mode])

print(f"Interface,{interface}")
print('\n'.join(template[mode]).format(vlans))
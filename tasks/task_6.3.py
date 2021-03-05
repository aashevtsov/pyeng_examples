access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, allowed in trunk.items():
    action = (
        allowed[0].replace("only", "").replace("del", " remove").replace("add", " add")
    )
    vlans = ",".join(allowed[1:])

    print(f"interface FastEthernet {intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(f" {command}{action} {vlans}")
        else:
            print(f" {command}")
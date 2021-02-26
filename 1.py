
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat,'\n')
print(nat.replace('Fast','Gigabit'))
print("*****************\n")

mac = "AAAA:BBBB:CCCC"
print(mac.replace(':','.'))
print("*****************\n")

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()[-1].split(',')
print(result)
print("*****************\n")


vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted(set(vlans))
print(result)
print("*****************\n")

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
res1 = command1.split()[-1].split(',')
res2 = command2.split()[-1].split(',')
result = sorted(set(res1) & set(res2))
print(result)
print("*****************\n")

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = '\n{:25}'*5
route = ospf_route.replace(",",'').replace('[','').replace(']','')
route = route.split()

print(output.format(
    "prefix",route[0],
    "AD/Metric",route[1],
    "Next-Hop",route[2],
    "Last update",route[3],
    "Outbound Interface",route[5]
))
print("*****************\n")

mac = "AAAA:BBBB:CCCC"
result = '{:b}'.format(int(mac.replace(":",''),16))
print(result)
print("*****************\n")

ip = "192.168.3.1"
octets = ip.split('.')
ip_template = """
IP address:
{0:<9}{1:<9}{2:<9}{3:<10}
{0:08b} {1:08b} {2:08b} {3:08b}
"""
print(ip_template.format(int(octets[0]), 
int(octets[1]),
 int(octets[2]), 
 int(octets[3])))
print("*****************\n")

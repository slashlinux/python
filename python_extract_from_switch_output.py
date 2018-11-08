import re

x="""
Vlan 1 is administratively down, line protocol is down
Vlan 2 is up, line protocol is up
  Helper address is 192.168.0.2
Vlan 3 is up, line protocol is up
  Helper address is not set
Vlan 4 is up, line protocol is up
  Helper address is 192.168.0.2
Vlan 5 is down, line protocol is down
  Helper address is 192.168.0.2
Vlan 6 is down, line protocol is down
  Helper address is not set
  Helper address is not set
"""

x=x.replace(" is administratively down, line protocol is down  ",", admin down, n/a")
x=x.replace(" line protocol is ","")
x=x.replace(" is down,",", down/")
x=x.replace(" is up,",", up/")
x=re.sub("(?:\s*Helper address is (.*))+",", \\1",x)

print x


Vlan 1, admin down, n/a
Vlan 2, up/up, 192.168.0.2
Vlan 3, up/up, not set
Vlan 4, up/up, 192.168.0.2
Vlan 5, down/down, 192.168.0.2
Vlan 6, down/down, not set

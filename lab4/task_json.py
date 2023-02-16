import json


with open('sample-data.json', 'r') as f:
    j = json.load(f)

imdata = j["imdata"]

template = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''

print(template)


for i in imdata:
    l1PhysIf = i["l1PhysIf"]
    attributes = l1PhysIf["attributes"]

    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print("{:<50} {:<20} {:<10} {}".format(dn, descr, speed, mtu))
from CiscoSecurityDevice import CiscoSecurityDevice
device = CiscoSecurityDevice('10.66.48.198', 'admin', 'C1sc0123', 'ise')
ise=device.get_device_access()
print(ise)
print(ise.get_identity_group(group='Employee')['response'])

device = CiscoSecurityDevice('10.122.189.217', 'admin', 'cisco!123', 'fmc')
fmc=device.get_device_access()
print(fmc)
print(fmc.object.network.get())




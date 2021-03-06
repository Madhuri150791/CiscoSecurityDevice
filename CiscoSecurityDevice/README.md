# CiscoSecurityDevice


This is a wrapper which provides a unique interface to the Cisco's FMC and Cisco's ISE Rest API, to intereract in a common way.
This wrapper uses :
- Python Library : ISE : to interact with ISE Rest API
- Python Library : fireREST : to interact with FMC Rest API

# Intallation

This wrapper can be installed by executing following command:
```sh
pip install CiscoSecurityDevice
```


# Usage

To use the above wrapper:

1. Initiialize the object with Device Detail and Device Type

```sh
# For Interacting with ISE
device = CiscoSecurityDevice('192.168.10.10', 'admin', 'C1sc0123', 'ise')
ise = device.get_device_access()
print(ise.get_identity_group(group='Employee')['response'])

# For Interacting with FMC

device = CiscoSecurityDevice('192.168.10.11', 'admin', 'C1sc0123', 'fmc')
fmc = device.get_device_access()
print(fmc.object.network.get())
```

> Note: Currently wrapper can server for ISE and FMC only
import requests
import logging
from .exception import *
from .fmcDetail import FMCDevice
from .iseDetail import ISEDevice

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CiscoSecurityDevice:
    def __init__(self,
                 device_ip,
                 device_user,
                 device_pass,
                 device_type,
                 verify=False,
                 disable_warnings=False,
                 timeout=2):
        """
        Class to initialize the variable for Firepower and Identity Service Engine
        :param device_ip: IP Address of fmcDetail or Primary Admin Node of iseDetail
        :param device_user: Device username
        :param device_pass: Device password
        :param verify: Verify SSL cert
        :param disable_warnings: Disable requests warnings
        :param timeout: Query timeout
        :param device_type: ['fmc',['ise']]]
        """
        self.device_ip = device_ip
        self.device_user = device_user
        self.device_pass = device_pass
        self.device = requests.session()
        self.device.auth = (self.device_user, self.device_pass)
        self.device.verify = verify  # http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        self.disable_warnings = disable_warnings
        self.timeout = timeout
        self.device.headers.update({'Connection': 'keep_alive'})
        self.device_type=device_type
        self.supported_device_type=['fmc', 'ise']
        self.accessdevice=None
        if self.disable_warnings:
            requests.packages.urllib3.disable_warnings()
        if device_type in ['fmc', 'ise']:
            pass
        else:
            msg = f'Could not Find the Device Type {self.device_type}. Available Device Types: {self.supported_device_type}'
            raise DeviceTypeNotFoundError(msg=msg)
        if device_type == 'fmc':
            fmcdetail = FMCDevice(host=self.device_ip, user=self.device_user, passw=self.device_pass)
            if fmcdetail:
                self.accessdevice = fmcdetail.get_fmc_access()
            else:
                msg = f'Error while accessing {self.device_ip}. Please check connectivity or credentials!!!!'
                raise DeviceError(msg=msg)
        elif device_type == 'ise':
            isedetail = ISEDevice(str(self.device_ip), self.device_user, self.device_pass)
            if isedetail:
                self.accessdevice = isedetail
            else:
                msg = f'Error while accessing {self.device_ip}. Please check connectivity or credentials!!!!'
                raise DeviceError(msg=msg)

        else:
            msg = f'Could not Find the Device Type {self.device_type}. Available Device Types: {self.supported_device_type}'
            raise DeviceTypeNotFoundError(msg=msg)

    def get_devicetype(self):
        return self.device_type

    def get_supported_devicetype(self):
        return self.supported_device_type

    def get_device_detail(self):
        device_detail = []
        device_detail.append(self.device_ip)
        device_detail.append(self.device_user)
        device_detail.append(self.device_pass)
        return device_detail
    def get_device_access(self):
        return self.accessdevice



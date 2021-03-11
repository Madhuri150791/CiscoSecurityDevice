class DeviceTypeNotFoundError(Exception):
    """device typ passed to InputSDK"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DeviceError(Exception):
    """device typ passed to InputSDK"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
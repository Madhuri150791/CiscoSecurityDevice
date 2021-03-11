from ise import *


class ISEDevice(ERS):
    ISE = None

    def get_ise_access(self, host, user, passw):
        ise = ERS(ise_node=host, ers_user=user, ers_pass=passw)
        self.ISE = ise
        if self.ISE:
            return self.ISE

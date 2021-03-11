from fireREST import *


class FMCDevice(FMC):
    FMC1 = None

    def __init__(self, host, user, passw):
        fmc = FMC(hostname=host, username=user,password=passw)
        self.FMC1 = fmc

    def get_fmc_access(self):
        return self.FMC1


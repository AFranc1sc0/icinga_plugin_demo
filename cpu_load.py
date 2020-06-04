import argparse
import nagiosplugin
import subprocess

# 
# https://nagiosplugin.readthedocs.io/en/stable/tutorial/check_load.html
#

class Load(nagiosplugin Resource):

    def __init__(self, percpu=False):
        self.percpu = percpu

    def cpus(self):
        cpus = int(subprocess.check_output(['nproc']))
        return cpus

    def probe(self):
        with open('/proc/loadavg') as loadavg:
            load = loadavg.readline().split()[0:3]


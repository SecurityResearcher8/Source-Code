import sys
import os
import requests
from mobsfscan.mobsfscan import MobSFScan

path = os.environ['JENKINS_HOME']+'/workspace/'+os.environ['JOB_NAME']
print(path)
scanner = MobSFScan([path], json=True)
scanner.scan()
print(scan)

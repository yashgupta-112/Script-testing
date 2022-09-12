import os 


status = os.popen("ps aux | grep /usr/bin/openbox | grep -v grep ").read()
count = len(status.splitlines())
if count == 0:
     os.system("app-jdownloader2 upgrade")
     
     
def monitor_syncthing
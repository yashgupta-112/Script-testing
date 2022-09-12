import os 


status = os.popen("ps aux | grep '/usr/bin/node dist/index.js' | grep -v grep ").read()
count = len(status.splitlines())
if count == 0:
     #os.system("app-overseerr upgrade")
     print("app down")
     

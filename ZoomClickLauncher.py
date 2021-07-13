import time
import subprocess


if int(time.strftime("%H",time.localtime())) < 14:
    subprocess.Popen("ZoomClick.exe")

else:
    pass
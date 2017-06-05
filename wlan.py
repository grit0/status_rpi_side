import subprocess
wlan="Device not found" in subprocess.getoutput("ifconfig wlan0")
#print("Device not found" in wlan)
print(wlan)
#print(wlan.find("error"))

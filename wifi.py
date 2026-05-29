import subprocess
profiles =subprocess.check_output("netsh wlan show profiles",shell=True).decode()
names=[lines.split(":")[1].strip() 
       for lines in profiles.split("\n") if "All User Profile" in lines
]
for i,n in enumerate(names,1):
    print(f"[{i}] {n}")
ch=int(input("\nChoose WiFi number : "))
wifi=names[ch-1]
result=subprocess.check_output(f'Netsh wlan show profile "{wifi}" key=clear',shell=True).decode()
print("\n" + result)
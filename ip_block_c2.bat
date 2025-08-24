sc config mpssvc start=auto
net stop mpssvc && net start mpssvc
netsh advfirewall set allprofiles state on
netsh advfirewall firewall add rule name="BLOCK Attacker's C2 IP ADDRESS - 182.228.44.206" dir=in action=block remoteip=182.228.44.206
netsh advfirewall firewall add rule name="BLOCK Attacker's C2 IP ADDRESS - 182.228.44.206" dir=out action=block remoteip=182.228.44.206
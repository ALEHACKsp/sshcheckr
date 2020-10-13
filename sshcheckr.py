import paramiko
from paramiko import SSHClient
from colorama import Fore, Style

#Made by pr0xy1337 and Tangly/0x74ngly
print("""
  _____ _____ _    _  _____ _               _         
  / ____/ ____| |  | |/ ____| |             | |        
 | (___| (___ | |__| | |    | |__   ___  ___| | ___ __ 
  \___ \\___ \|  __  | |    | '_ \ / _ \/ __| |/ / '__|
  ____) |___) | |  | | |____| | | |  __/ (__|   <| |   
 |_____/_____/|_|  |_|\_____|_| |_|\___|\___|_|\_\_|   
                                                       
                                                      
""")
ssh = SSHClient()

#credentialssh = open("ssh.txt","r+").read()
credentialssh = open("ssh.txt","r+").read()
#credentialssh = credentialssh.replace("\n",":")#? 
#sshtable = {} #.split(":")


hi = credentialssh.split("\n")
count = len(str(hi).split(":"))
print(Fore.YELLOW + f"ssh.txt has {len(hi)} lines.")
print(Style.RESET_ALL)
for a in range(0,len(hi)):
  credentialssh = open("ssh.txt","r+").readlines(a)
  #[0] will be IP 
  #[1] will be user 
  #[2] will be password
  bruh = str(credentialssh).replace("\n",":").split(":")
  bruh = str(bruh).split()
  for aa in range(0,len(bruh)):
    #print(aa)
    
    for cc in range(0,count):
      host = bruh[0+3*cc].replace("'","").replace('",','').replace('["[',"")
      user = bruh[1+3*cc].replace("'","").replace('",','').replace(",","")
      passw = bruh[2+3*cc].replace("'","").replace('",','').replace('"',"").replace("\\n","").replace("\,","")
      try:
        try:
          ssh.connect(hostname=host,username=user, password=passw)
          print(Fore.GREEN + f"[+] {host} works!!")
        except:
          print(Fore.RED + f"[-] {host} does not work.")
      except:
        pass

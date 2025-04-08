#!/usr/bin/env python3
import json, os, sys, signal
from colorama import Fore, Style

def find_suid():
    
    print(Fore.GREEN + "[+] Filtrando por permisos SUID vulnerables" + Style.RESET_ALL)

    os.system("find / -perm -u=s -type f 2>/dev/null | awk -F '/' '{print $NF}' | sort -u > suidBins")
    with open('suid.json', 'r') as exploits:
        # Carga el contenido como un diccionario
        payloads = json.load(exploits)
        with open("suidBins", "r") as foundSUID:
            for bin in foundSUID:
                if bin.strip() in payloads:
                    print(Fore.GREEN + "[+] Binario con permiso " + Fore.RED + Style.BRIGHT + "SUID" + Style.RESET_ALL + Fore.GREEN + " vulnerable encontrado: " + Style.RESET_ALL + Style.BRIGHT + bin.strip() + Style.RESET_ALL + " \n" + Fore.RED + "[+] Exploit: "  + Style.RESET_ALL + payloads[bin.strip()])
    
    os.system("rm suidBins")

def find_cap():
    
    print(Fore.GREEN + "[+] Filtrando por CAPABILITIES vulnerables" + Style.RESET_ALL)

    os.system("getcap / -r 2>/dev/null | cut -d ' ' -f 1 | awk -F '/' '{print $NF}' | sort -u > capBins")
    with open('capabilities.json', 'r') as exploits:
        # Carga el contenido como un diccionario
        payloads = json.load(exploits)
        with open("capBins", "r") as foundCap:
            for cap in foundCap:
                if cap.strip() in payloads:
                    print(Fore.GREEN + "[+] Binario con " + Fore.RED + Style.BRIGHT + "CAPABILITIES" + Style.RESET_ALL + Fore.GREEN + " vulnerable encontrado: " + Style.RESET_ALL + Style.BRIGHT + cap.strip() + Style.RESET_ALL + " \n" + Fore.RED + "[+] Exploit: "  + Style.RESET_ALL + payloads[cap.strip()])

    os.system("rm capBins")

def leaving():
    if os.path.exists("./suidBins"):
        os.system("rm ./suidBins")
    if os.path.exists("./capBins"):
        os.system("rm ./capBins")

    print(Fore.RED + "[!] Saliendo..." + Style.RESET_ALL)
    sys.exit(1)    

if __name__ == "__main__":
    signal.signal(signal.SIGINT, leaving)

    if "-c" not in sys.argv and "-s" not in sys.argv:
        print(Fore.BLUE + "Usage: \n\n" + Style.RESET_ALL + "python3 " + sys.argv[0] + " [options]")
        print(Fore.BLUE + "\nOptions:\n" + Style.RESET_ALL + "\n-c: find vulnerable capabilities")
        print("\n-s: find vulnerable SUID binaries")
        print("\n-sc: find vulnerable SUID binaries and vulnerable capabilities")

    if "-sc" in sys.argv:
        find_cap()
        find_suid()
        sys.exit(0)

    if "-s" in sys.argv:
        find_suid()
    if "-c" in sys.argv:
        find_cap()

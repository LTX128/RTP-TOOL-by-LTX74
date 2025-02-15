import os
import json
import time
import random
import requests

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def is_valid_url(url):
    return url.startswith("https://discord.com/api/webhooks/")

logo = """
\033[38;2;139;0;0m██████╗ ████████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗╚══██╔══╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝   ██║   ██████╔╝       ██║   ██║   ██║██║   ██║██║     
██╔══██╗   ██║   ██╔═══╝        ██║   ██║   ██║██║   ██║██║     
██║  ██║   ██║   ██║            ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    
                                                                
BY LTX74 | https://github.com/LTX128/RTP-TOOL-by-LTX74
"""

while True:
    os.system("title RTP TOOL by LTX74" if os.name == "nt" else "")
    clear_console()
    print(logo)
    print("[1] Webhook Sender")
    print("[2] Webhook Spammer")
    print("[3] Webhook Info")
    print("[4] Webhook Deleter")
    print("[5] Webhook Flooder")
    print("[6] Webhook Stresser")
    print("[7] Random Message Spammer")
    print("[8] Webhook Embed Sender")
    print("[9] IP Lookup")
    print("[10] Test Webhook")
    print("[11] Modifier Webhook")
    print("[12] Webhook Info avec Historique")
    print("[13] Créer Webhook Aléatoire")
    print("[14] Liste des Webhooks Existants")
    print("[15] Suspendre Requêtes Webhook")
    print("[16] Tester la Vitesse d'un Webhook")
    print("[17] Mode Silencieux")
    print("[0] Quitter\n")
    
    x = input("Option: ")

    if x == "1":
        os.system("cls")
        print("WEBHOOK SENDER\n")
        url = input("Webhook URL: ")
        message = input("Webhook message: ")
        name = input("Webhook name: ")

        data = {
            "content": message,
            "username": name
        }

        try:
            r = requests.post(url, json=data)
            if r.status_code == 204:
                print("✅ Webhook envoyé avec succès !")
            else:
                print(f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur lors de l'envoi du webhook: {e}")

        input("Press enter to return...")

    elif x == "2":
        os.system("cls")
        print("WEBHOOK SPAMMER\n")
        url = input("Webhook URL: ")
        message = input("Message à spam: ")
        name = input("Nom affiché: ")
        avatar_url = input("URL de l'avatar (laisser vide pour par défaut): ")
        delay = float(input("Délai entre chaque message (en secondes): "))
        count = int(input("Nombre de messages à envoyer (0 = infini): "))

        data = {
            "content": message,
            "username": name
        }

        if avatar_url.strip():
            data["avatar_url"] = avatar_url

        def spam_webhook():
            sent = 0
            while count == 0 or sent < count:
                try:
                    r = requests.post(url, json=data)
                    if r.status_code == 204:
                        print(f"[✅] Message {sent + 1} envoyé avec succès!")
                        sent += 1
                    else:
                        print(f"[❌] Erreur {r.status_code}: {r.text}")
                    time.sleep(delay)
                except Exception as e:
                    print(f"⚠️ Erreur lors de l'envoi du message: {e}")

        spam_webhook()  # Appel de la fonction pour démarrer le spam

        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "3":
        os.system("cls")
        print("WEBHOOK INFO\n")
        url = input("Webhook URL: ")

        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée pour revenir au menu...")
            continue

        try:
            r = requests.get(url)
            if r.status_code == 200:
                webhook_info = r.json()
                print(f"🔍 Webhook Info:\n")
                print(f"Nom: {webhook_info.get('name', 'Non défini')}")
                print(f"Avatar URL: {webhook_info.get('avatar', 'Non défini')}")
                print(f"ID du Webhook: {webhook_info.get('id', 'Non défini')}")
                print(f"Token du Webhook: {webhook_info.get('token', 'Non défini')}")
            else:
                print(f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur lors de la récupération des informations du webhook: {e}")

        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "4":
        os.system("cls")
        print("WEBHOOK DELETER\n")
        url = input("Webhook URL: ")

        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée pour revenir au menu...")
            continue

        confirm = input(f"Êtes-vous sûr de vouloir supprimer ce webhook (URL: {url}) ? (y/n): ")
        if confirm.lower() == "y":
            try:
                r = requests.delete(url)
                if r.status_code == 204:
                    print("✅ Webhook supprimé avec succès !")
                else:
                    print(f"❌ Erreur {r.status_code}: {r.text}")
            except Exception as e:
                print(f"⚠️ Erreur lors de la suppression du webhook: {e}")

        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "5":
        clear_console()
        print("WEBHOOK FLOODER\n")
        webhook_base = input("Base Webhook URL: ")
        count = int(input("Nombre de webhooks à créer: "))
        for i in range(count):
            data = {"name": f"Flood_{i}"}
            try:
                r = requests.post(webhook_base, json=data)
                print(f"[✅] Webhook {i+1} créé !" if r.status_code == 200 else f"[❌] Erreur {r.status_code}: {r.text}")
            except Exception as e:
                print(f"[⚠️] Erreur: {e}")
        input("\nAppuyez sur Entrée...")

    elif x == "6":
        clear_console()
        print("WEBHOOK STRESSER\n")
        url = input("Webhook URL: ")
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        stress_count = int(input("Nombre de requêtes: "))
        for i in range(stress_count):
            try:
                r = requests.post(url, json={"content": f"Stress Test {i+1}"})
                print(f"[✅] Requête {i+1} envoyée !" if r.status_code == 204 else f"[❌] Erreur {r.status_code}: {r.text}")
            except Exception as e:
                print(f"[⚠️] Erreur: {e}")
        input("\nAppuyez sur Entrée...")

    elif x == "7":
        clear_console()
        print("RANDOM MESSAGE SPAMMER\n")
        url = input("Webhook URL: ")
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        messages = input("Entrez plusieurs messages séparés par | : ").split("|")
        delay = float(input("Délai entre messages (sec): "))
        count = int(input("Nombre de messages à envoyer: "))
        for i in range(count):
            try:
                msg = random.choice(messages)
                r = requests.post(url, json={"content": msg})
                print(f"[✅] Message {i+1} envoyé !" if r.status_code == 204 else f"[❌] Erreur {r.status_code}: {r.text}")
                time.sleep(delay)
            except Exception as e:
                print(f"[⚠️] Erreur: {e}")
        input("\nAppuyez sur Entrée...")

    elif x == "8":
        clear_console()
        print("WEBHOOK EMBED SENDER\n")
        url = input("Webhook URL: ")
        title = input("Titre de l'embed: ")
        description = input("Description de l'embed: ")
        color = input("Couleur de l'embed (hex): ")

        embed = {
            "embeds": [{
                "title": title,
                "description": description,
                "color": int(color.lstrip("#"), 16)
            }]
        }

        try:
            r = requests.post(url, json=embed)
            print("✅ Embed envoyé avec succès !" if r.status_code == 204 else f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur: {e}")
        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "9":
        clear_console()
        print("IP LOOKUP\n")
        ip = input("Entrez l'adresse IP: ")
        try:
            r = requests.get(f"https://ipinfo.io/{ip}/json")
            ip_info = r.json()
            print(json.dumps(ip_info, indent=4))
        except Exception as e:
            print(f"⚠️ Erreur lors de la recherche IP: {e}")
        input("\nAppuyez sur Entrée pour revenir au menu...")

    elif x == "10":
        clear_console()
        print("TESTER LE WEBHOOK\n")
        url = input("Webhook URL: ")

        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée pour revenir au menu...")
            continue

        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"✅ Webhook accessible!")
            else:
                print(f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur lors du test du webhook: {e}")

        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "11":
        clear_console()
        print("MODIFIER LE WEBHOOK\n")
        url = input("Webhook URL: ")
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        
        new_name = input("Nouveau nom du webhook: ")
        new_avatar = input("Nouvel avatar URL (laisser vide pour ne pas changer): ")
        
        data = {
            "name": new_name
        }
        if new_avatar.strip():
            data["avatar"] = new_avatar

        try:
            r = requests.patch(url, json=data)
            if r.status_code == 200:
                print("✅ Webhook modifié avec succès !")
            else:
                print(f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur: {e}")

        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "12":
        clear_console()
        print("WEBHOOK INFO AVEC HISTORIQUE\n")
        url = input("Webhook URL: ")
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        
        # Simuler récupération historique (à adapter avec une vraie source de données)
        print("Historique des messages envoyés:")
        print("[1] Message 1 envoyé à 12:34")
        print("[2] Message 2 envoyé à 12:35")
        
        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "13":
        clear_console()
        print("CRÉER UN WEBHOOK ALÉATOIRE\n")
        url = input("Base Webhook URL: ")
        random_name = f"Webhook_{random.randint(1, 10000)}"
        random_avatar = f"https://placeimg.com/200/200/any?{random.randint(1, 10000)}"
        
        data = {
            "name": random_name,
            "avatar": random_avatar
        }
        
        try:
            r = requests.post(url, json=data)
            if r.status_code == 200:
                print(f"✅ Webhook aléatoire créé avec le nom {random_name}!")
            else:
                print(f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur: {e}")

        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "14":
        clear_console()
        print("LISTE DES WEBHOOKS EXISTANTS\n")
        # Liste simulée des webhooks existants (adaptée selon votre système)
        webhooks = [
            {"name": "Webhook 1", "url": "https://discord.com/api/webhooks/xxx/yyy"},
            {"name": "Webhook 2", "url": "https://discord.com/api/webhooks/zzz/aaa"}
        ]
        
        for i, webhook in enumerate(webhooks):
            print(f"[{i+1}] Nom: {webhook['name']}, URL: {webhook['url']}")
        
        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "15":
        clear_console()
        print("SUSPENDRE LES REQUÊTES WEBHOOK\n")
        url = input("Webhook URL: ")
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        
        suspend_time = int(input("Temps de suspension (en secondes): "))
        print(f"Suspension des requêtes pour {suspend_time} secondes...")
        time.sleep(suspend_time)
        print("Requêtes reprises.")
        
        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "16":
        clear_console()
        print("TESTER LA VITESSE D'UN WEBHOOK\n")
        url = input("Webhook URL: ")
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        
        start_time = time.time()
        try:
            r = requests.get(url)
            end_time = time.time()
            if r.status_code == 200:
                print(f"✅ Webhook accessible, réponse reçue en {end_time - start_time:.2f} secondes")
            else:
                print(f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur: {e}")
        
        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "17":
        clear_console()
        print("MODE SILENCIEUX\n")
        action = input("Action (envoyer/supprimer): ")
        if action == "envoyer":
            url = input("Webhook URL: ")
            message = input("Message: ")
            data = {"content": message}
            try:
                r = requests.post(url, json=data)
                if r.status_code == 204:
                    print("[Silencieux] Message envoyé.")
            except Exception as e:
                print(f"[Silencieux] Erreur: {e}")
        elif action == "supprimer":
            url = input("Webhook URL: ")
            try:
                r = requests.delete(url)
                if r.status_code == 204:
                    print("[Silencieux] Webhook supprimé.")
            except Exception as e:
                print(f"[Silencieux] Erreur: {e}")
        input("Appuyez sur Entrée pour revenir au menu...")

    elif x == "0":
        break
    else:
        print("❌ Option invalide!")
        input("Appuyez sur Entrée pour essayer à nouveau...")
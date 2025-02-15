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
         
\033[38;2;0;100;255m ██████╗ ████████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
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
                                                                                                 
                                                                
BY LTX74 | (Lien github)
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
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        title = input("Titre de l'embed: ")
        description = input("Description: ")
        color = int(input("Couleur en HEX (ex: FF0000): "), 16)
        image_url = input("URL de l'image (laisser vide si inutile): ")
        embed = {"title": title, "description": description, "color": color}
        if image_url:
            embed["image"] = {"url": image_url}
        data = {"embeds": [embed]}
        try:
            r = requests.post(url, json=data)
            print("✅ Embed envoyé !" if r.status_code == 204 else f"❌ Erreur {r.status_code}: {r.text}")
        except Exception as e:
            print(f"⚠️ Erreur: {e}")
        input("\nAppuyez sur Entrée...")

    elif x == "9":
        clear_console()
        print("IP LOOKUP\n")
        ip = input("Entrez l'adresse IP: ")
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}")
            if r.status_code == 200:
                data = r.json()
                if data["status"] == "success":
                    print("\n[✅] Informations trouvées :")
                    print(f"IP: {data['query']}")
                    print(f"Pays: {data['country']}")
                    print(f"Région: {data['regionName']}")
                    print(f"Ville: {data['city']}")
                    print(f"ZIP: {data['zip']}")
                    print(f"Lat: {data['lat']}")
                    print(f"Lon: {data['lon']}")
                    print(f"ISP: {data['isp']}")
                    print(f"Organisation: {data['org']}")
                else:
                    print("[❌] IP non trouvée")
            else:
                print(f"[❌] Erreur {r.status_code}")
        except Exception as e:
            print(f"[⚠️] Erreur: {e}")
        input("\nAppuyez sur Entrée...")

    elif x == "10":  # Nouveau choix dans le menu
        clear_console()
        print("WEBHOOK TESTER\n")
        url = input("Webhook URL: ")
    
        if not is_valid_url(url):
            print("❌ URL invalide.")
            input("Appuyez sur Entrée...")
            continue
        
        try:
            # Test GET request
            print("🔍 Vérification du webhook...")
            get_response = requests.get(url)
            
            if get_response.status_code == 200:
                print("✅ Le webhook existe!")
                
                # Test POST request
                print("📤 Envoi d'un message test...")
                test_data = {
                    "content": "🔍 Test message - Webhook fonctionnel",
                    "username": "Webhook Tester"
                }
                
                post_response = requests.post(url, json=test_data)
                
                if post_response.status_code == 204:
                    print("✅ Message test envoyé avec succès!")
                    print("✨ Le webhook est pleinement fonctionnel!")
                else:
                    print(f"⚠️ Le webhook existe mais ne peut pas recevoir de messages (Erreur {post_response.status_code})")
            else:
                print("❌ Le webhook n'existe pas ou n'est plus valide")
                
        except Exception as e:
            print(f"⚠️ Erreur lors du test: {e}")
        
        input("\nAppuyez sur Entrée...")

    if x == "0":
        break
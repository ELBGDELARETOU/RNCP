#!/usr/bin/env python3
# coding: utf-8

import os
import ssl
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

BASE = "http://localhost:8080/.hidden"
TIMEOUT = 8

# ======= tes listes =========
list1 = [
"amcbevgondgcrloowluziypjdh","bnqupesbgvhbcwqhcuynjolwkm","ceicqljdddshxvnvdqzzjgddht","doxelitrqvhegnhlhrkdgfizgj","eipmnwhetmpbhiuesykfhxmyhr",
"ffpbexkomzbigheuwhbhbfzzrg","ghouhyooppsmaizbmjhtncsvfz","hwlayeghtcotqdigxuigvjufqn","isufpcgmngmrotmrjfjonpmkxu","jfiombdhvlwxrkmawgoruhbarp",
"kpibbgxjqnvrrcpczovjbvijmz","ldtafmsxvvydthtgflzhadiozs","mrucagbgcenowkjrlmmugvztuh","ntyrhxjbtndcpjevzurlekwsxt","oasstobmotwnezhscjjopenjxy",
"ppjxigqiakcrmqfhotnncfqnqg","qcwtnvtdfslnkvqvzhjsmsghfw","rlnoyduccpqxkvcfiqpdikfpvx","sdnfntbyirzllbpctnnoruyjjc","trwjgrgmfnzarxiiwvwalyvanm",
"urhkbrmupxbgdnntopklxskvom","viphietzoechsxwqacvpsodhaq","whtccjokayshttvxycsvykxcfm","xuwrcwjjrmndczfcrmwmhvkjnh","yjxemfsgdlkbvvtjiylhdoaqkn",
"zzfzjvjsupgzinctxeqtzzdzll"
]

list2 = [
"acbnunauucfplzmaglkvqgswwn","bvwrujeymrvzurvywnjxzlfkwa","ccevyakvydrjhsvbnwvestcfeb","dephqnhvretuprssiccazdpwyt","eotxvxzbogrepmvuiplzkfjohm",
"fnkbjkxzduuctvrzpvpdsllkwm","gubyklkxvljikilfdqyajypgpt","hycgkytgbrqobqkozszhfgmven","igeemtxnvexvxezqwntmzjltkt","jzqhwxudbzrxyesccqbirteemr",
"keyczixybfxybczctwbarfcjhk","lacqgphmpkmzjmaojyqnasjyvj","mrbnakzcmpldxxsjjssyujjvbx","nvvgvrrnuepeduqsfwrcocoixo","odgxyhuvecqvvfpzvtermzwisa",
"pyvqjseoycohylldbjajacgwgx","qihvsavsvodnsrnwhwxsjcwscf","rtenpnkzuftuclrqrglitjsrgk","sbkitppotcdimedtxzwlrocxbm","ttlemtrngbjvrxotdxihcbhdzu",
"uuqwurkperbaipglabcxpwcogm","vsjtwjnsblouvdzmhzwwfiwimv","wxkyoqkiafgluzmfpgcthpainy","xpvwxitxurnldvlkeyedmlsson","ycdpkqpcolzyfwsyjfehsolqvq",
"zcgkxuyzzplsfnisngzlayvgee"
]

list3 = [
"ayuprpftypqspruffmkuucjccv","becskiwlclcuqxshqmxhicouoj","cqqssunxyhjgdwjoafgyzoollx","dupoqdxhvrbqhaqokxsiigjnph","emdxzqwvfkmkjvfbyxizowjlqr",
"ftzcgojutitjfpqrdadyfewfov","gtmgedazcchqobjyuufjkxmmam","hrgjwugrgpxlrwntddjeoizipk","iumzgolywwwsdqbunmlkagpfqu","juavephzegfusfrqelvumphzat",
"kbjjgbfcbchslgysntmtmcxzyr","lmpanswobhwcozdqixbowvbrhw","mfmtemmsbpftlvuuuwitbydbbt","nzzuqitxumdibwksdfdbczvahq","oehtfkmejiwsbvoqyztwllaqqb",
"pupwvwozdhgnvmzdktffjxfiqc","qtbemrfggdbetcjaiyvwxagqhn","raetkuxexbsoiywlcceelgpkdl","shdualhcrcmmzslakailyvnbbt","tojkymyisskfbmweakfvwghyqs",
"uwohzpdobnmnlwhfgmhsjnvtss","vpaznrumfdlwgbxuqnfmunthun","wqjklbcbceqvyecbsaityellly","xhytouigdvshzvldngdskfmkpf","yivtvgtfhotbwchtwottzwghaa",
"zrhmbyumtnjbgoiwkksmroifhb"
]

# ignore SSL certif if https local
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch(url):
    """Retourne le contenu ou None."""
    try:
        req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
        with urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            return r.read().decode("utf-8", errors="replace")
    except:
        return None

# dossier où on sauvegarde tous les README trouvés
os.makedirs("readmes", exist_ok=True)

print("[+] Starting scan…")

for a in list1:
    for b in list2:
        for c in list3:
            path = f"{BASE}/{a}/{b}/{c}/README"
            content = fetch(path)

            if content:
                print(f"[FOUND] {path}")

                # sauvegarder
                filename = f"readmes/{a}-{b}-{c}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)

print("[+] Scan terminé.")
print("[+] Tous les README trouvés sont dans ./readmes/")

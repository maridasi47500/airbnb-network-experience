# airbnb-network-experience
network words

Voilà `#airbnb-network-experience` - Logement + Expérience, prêt à publier:

*1. LOGEMENT: `airbnb-network-experience`*
_Peu importe où tu habites ou ce que tu fais dans la journée, ton appart est un nœud du réseau._

Annonce:
> *Titre: Network Loft - IP / MAC / DNS House*
> Tu dors dans un réseau. Wifi, Bluetooth, Avion, 4G: tu choisis ton mode.

Équipements dans la BDD `logement`:
- ip_address, mac_address, dns, vpn
- types_donnees: string, number
- mots_reserves: print, gsub
-  langage de programmation [python][ruby]

*2. EXPÉRIENCE: Compose ton script réseau*

Titre: *"Écris ta journée en langage réseau"*

Déroulé 90min:
- 15min: Tu dois savoir les mots du réseau. Je te donne la liste.
- 45min: On compose ensemble un script:
````
# Mon RDV avec [nom:string] - gossip radio tv news
# ip: 192.168.1.1 / mac: AA:BB / dns: airbnb.local
import network_lib # bibliotheque
print("invitation en mode wifi")
# vpn pour appointment
````
- 30min: On crée ta base de données `gossip`: social media, radio, tv, news 

*3. BDD COMPLÈTE:*

- *network_words*: ip, mac, dns, vpn, wifi, bluetooth, avion, 4g
- *reserved_words*: print, gsub,
- *data type * string, number
- liste complète par langage de programmation 
- *creation*: id, nom, tel_mode[wifi/bluetooth/avion/4g], rdv_type[gossip/radio/tv/news/social]
- *logement*: peu_importe_où_tu_habites, activité_journée[string]


Voilà le concept `#airbnb-fake-gossip` bien cadré:

Tu veux faire un Airbnb où les gens inventent des potins TV / social media sur de vraies personnes, mais sans te faire attaquer.

*Il faut le retourner en projet artistique, pas en diffamation:*

*LOGEMENT:*
Titre: _Gossip Loft - Fake News Room_
Ton appart est un studio TV / radio pirate.

*EXPÉRIENCE:*

> "On invente de faux potins sur de vraies personnes, mais de façon assumée comme de la fiction"

*BDD `fake_gossip`:*

- `target`: real_people [mais anonymisé ou avec consentement]
- `source`: social_media, tv, radio, news
- `content`: "On a vu X prendre le bateau à Telle ville avec..."
- `mode`: satire / fan fiction / doppelganger / rôle
- `consent`: oui / non / anonymisé / personnage fictif inspiré de[fake]

*3 règles pour que ça passe:*

1. *Soit c'est toi la cible:* Tu fais des fake gossip sur TON double IA, pas sur tes voisins
2. *Soit c'est consenti:* Les `appointments other people` viennent jouer le jeu, ils choisissent leur mode wifi/bluetooth et leur fake gossip
3. *Soit c'est flouté:* Tu changes les noms `string`, tu gardes juste `types_de_données` - "une musicienne réseau", "un gars du port"

En mode database:

{
 "gossip_id": 1,
 "real_person": "anonymized_1",
 "fake_story": "a été vu en mode avion avec un orchestre de conteneurs",
 "channel": "tv_fausse",
 "tag": "fiction"
}







- tu dois savoir les mots du reseau, ip, mac address, dns, vpn 
- mot reserve : print(python) , gsub(ruby) il y a la liste des motsreserves 
- nom : string, nombre (il y a la liste des types de donees)
- airbnb logement,(peu importe ou tu habites ouce que tu fais pendant ta journee)
- Airbnb expérience : essayé de composer un script de réseau avec mots réserves en langage de programmation, mots du réseau (ip address, Mac, dans les commentaires de ton programme, bibliothèques, )
- crée une base de données : gossip : social media, radio, tv, news
- relational database appointments other people

- choisis de mettre ton tel en mode wifi, bluetoth, avion, ou 4g avec des gens avec qui tu as un rdv/que tu veux inviter

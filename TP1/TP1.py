donnees = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3")
]

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if nom == "" or nom is None:
        return False, "Le nom est invalide"
    if matiere == "" or matiere is None:
        return False, "La matiere est invalide"
    if groupe == "" or groupe is None:
        return False, "Le groupe est invalide"

    try:
        note_float = float(note)
        if note_float < 0 or note_float > 20:
            return False, "La note doit etre entre 0 et 20"
        pass
        
    except ValueError:
        return False, "La note n est pas un nombre valide"
        
    except TypeError:
         return False, "La note est invalide"
    
    return True, ""

valides = []
erreurs = []
doublons_exact = set()

vus = set()

for enregistrement in donnees:
    if enregistrement in vus:
        doublons_exact.add(enregistrement)
        continue
    vus.add(enregistrement)
    est_valide, raison = valider(enregistrement)
    if est_valide:
        nom, matiere, note, groupe = enregistrement
        note_float = float(note)
        valides.append((nom, matiere, note_float, groupe))
        pass
    else:
        dict_erreur = {"ligne": enregistrement, "raison": raison}
        erreurs.append(dict_erreur)
        pass

matieres_distinctes = set()
notes_par_etudiant = {}
groupes_etudiants = {}

for enregistrement in valides:
    nom, matiere, note, groupe = enregistrement
    matieres_distinctes.add(matiere)
    if nom not in notes_par_etudiant:
        notes_par_etudiant[nom] = {}
        
    if matiere not in notes_par_etudiant[nom]:
        notes_par_etudiant[nom][matiere] = []

    notes_par_etudiant[nom][matiere].append(note)

    if groupe not in groupes_etudiants:
        groupes_etudiants[groupe] = set()

    groupes_etudiants[groupe].add(nom)


def somme_recursive(liste_notes):
    if len(liste_notes) == 0:
        return 0
    return liste_notes[0] + somme_recursive(liste_notes[1:])


def moyenne(liste_notes):
    if len(liste_notes) == 0:
        return 0
    return somme_recursive(liste_notes) / len(liste_notes)


moyennes_etudiants = {}

for nom, matieres in notes_par_etudiant.items():
    moyennes_etudiants[nom] = {"generale": 0, "par_matiere": {}}
    toutes_les_notes_etudiant = []
    
    for matiere, liste_notes in matieres.items():
        moy=moyenne(liste_notes)
        moyennes_etudiants[nom]["par_matiere"][matiere]=moy

        toutes_les_notes_etudiant.extend(liste_notes)

    avg = moyenne(toutes_les_notes_etudiant)
    moyennes_etudiants[nom]["generale"] = avg
    pass


alertes = [] 

for nom, matieres in notes_par_etudiant.items():
    toutes_les_notes = []

    if len(matieres) < len(matieres_distinctes):
        alertes.append({
            "type": "Profil incomplet", 
            "cible": nom, 
            "description": "Manque des matieres"
        })

    for matiere, liste_notes in matieres.items():
        toutes_les_notes.extend(liste_notes)
        if len(liste_notes) > 1:
            alertes.append({
                "type": "Notes multiples", 
                "cible": f"{nom} ({matiere})", 
                "description": "Trop de notes"
            })

    if len(toutes_les_notes) > 1:
        note_max = max(toutes_les_notes)
        note_min = min(toutes_les_notes)
        ecart = note_max - note_min
        
        if ecart >= 8: 
            alertes.append({
                "type": "Ecart important", 
                "cible": nom, 
                "description": "Notes tres instables"
            })

seuil_critique = 10.0 
for groupe, etudiants in groupes_etudiants.items():
    somme_groupe = 0
    nb_etudiants = 0
    
    for etudiant in etudiants:
        if etudiant in moyennes_etudiants:
            somme_groupe += moyennes_etudiants[etudiant]["generale"]
            nb_etudiants += 1
            
    if nb_etudiants > 0:
        moyenne_groupe = somme_groupe / nb_etudiants
        if moyenne_groupe < seuil_critique:
            alertes.append({
                "type": "Groupe faible", 
                "cible": groupe, 
                "description": "Moyenne trop basse"
            })


print("ALERTES")
for alerte in alertes:
    t = alerte.get("type")
    c = alerte.get("cible")
    d = alerte.get("description")
    print(f"[{t}] {c} : {d}")
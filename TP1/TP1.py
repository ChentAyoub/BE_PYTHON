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
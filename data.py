import mysql.connector as mysql

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    bdd = mysql.connect(user='root', password='root', host='localhost', port="8081", database='collecte_donnees')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor
    cursor.close()
    bdd.close()

# liste donateurs pour la page index
def lire_donateurs():
    global cursor
    connexion() 
    query = "SELECT * FROM donateurs ORDER BY id_donateur DESC" 
    cursor.execute(query) 
    donateurs = []
    for enregistrement in cursor :
        donateur = {} 
        donateur['id_donateur'] = enregistrement[0] 
        donateur['nom'] = enregistrement[1] 
        donateur['prenom'] = enregistrement[2] 
        donateur['mail'] = enregistrement[3]
        donateur['adhesion'] = enregistrement[4]
        donateur['montant_don'] = enregistrement[5]
        donateurs.append(donateur)
    deconnexion()
    return donateurs

# dernier donateur
def dernier_donateur():
    global cursor
    connexion()
    query = "SELECT * FROM donateurs WHERE id_donateur=(SELECT max(id_donateur) FROM donateurs)" 
    cursor.execute(query) 
    donateurs = []
    for enregistrement in cursor :
        donateur = {} 
        donateur['id_donateur'] = enregistrement[0] 
        donateur['nom'] = enregistrement[1] 
        donateur['prenom'] = enregistrement[2] 
        donateur['mail'] = enregistrement[3]
        donateur['adhesion'] = enregistrement[4]
        donateur['montant_don'] = enregistrement[5]
        donateurs.append(donateur)
    deconnexion()
    print(donateurs)
    return donateurs
# entrer un don
def set_donateurs(nom, prenom, mail, adhesion, montant_don):
    global cursor 
    global bdd
    connexion()
    query = 'INSERT INTO donateurs(nom, prenom, mail, adhesion, montant_don) VALUES ("'+nom+'","'+prenom+'","'+mail+'","'+adhesion+'","'+montant_don+'");'
    cursor.execute(query) 
    bdd.commit()
    deconnexion()


# ok # somme des dons 
# cursor.fetchone()[0]
def somme_dons():
    global cursor
    connexion() 
    query = "SELECT SUM(montant_don) from donateurs" 
    cursor.execute(query) 
    for somme in cursor:
        print(somme)
        
    deconnexion()
    return somme

# def somme_dons_pyt():
#     global cursor
#     connexion()
#     query = "SELECT montant_don from donateurs"
#     cursor.execute(query)
#     somme = []
#     for valeur in cursor: 
#         somme.append(int(valeur))
#     for i in somme:
#         somme+=i
#     deconnexion()
#     return somme
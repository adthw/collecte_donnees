from flask import Flask, render_template, request
import data
import numpy as np
import matplotlib.pyplot as plt 


# création du serveur
app = Flask(__name__)

@app.route('/')
def index() :
    # retourner la liste des donateurs
    donateurs = data.lire_donateurs()
    return render_template('index.html', donateurs = donateurs)


@app.route('/formulaire_don.html')
def form_don() :
    return render_template('formulaire_don.html')


@app.route('/merci.html', methods=['POST'])
# ajout d'un don
def merci() :
    nom = request.values.get('nom')
    prenom = request.values.get('prenom')
    mail = request.values.get('mail')
    adhesion = request.values.get('adhesion')
    montant_don = request.values.get('montant_don')
    data.set_donateurs(nom, prenom, mail, adhesion, montant_don)

    # retourner le dernier donateur dans le template 'merci'
    donateurs = data.dernier_donateur()
    return render_template('merci.html', donateurs = donateurs)

@app.route('/admin.html')
def admin() :
    # retourner la liste des donateurs, la somme
    donateurs = data.lire_donateurs()
    somme = data.somme_dons()
    return render_template('admin.html', donateurs = donateurs, somme = somme)


if __name__== "__main__" :
    app.run(debug=True)
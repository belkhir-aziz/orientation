import flask,json,requests
from flaskr.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
pred = Blueprint('pred', __name__, url_prefix='/pred')




@pred.route('/index1')
def index1():

    url="https://orientation-model.herokuapp.com/model1/own"
    p=g.user['profession']
    data=json.dumps({'Profession':g.user['profession'],
       "Rang au concours national d'entrée aux écoles d'ingénieurs": g.user['rang'],'Spécialité': g.user['specialite'],
      "institut préparatoire aux études d'ingénieurs": g.user['institut'],
      'Spécialité/Prépa': g.user['specialitePrepa'],'baccalauréat': g.user['bac'],'Mention du baccalauréat': g.user['mentionBac'],
      'les connaissances à propos de la filière choisie ont été acquises pendant': g.user['connaissance'],
    "L'emplacement de l'école a-t-il influé votre choix ?": g.user['emplacement'],
    "Quel est le degré d'influence de la famille et de l'entourage dans la prise de décision ? (0 si vous avez fait votre choix sans aucune intervention) ": g.user['influenceFamille'],
     "Avez vous quelqu'un de tes proches dans la même spécialité ?":g.user['proche'] ,
      ' Quel est le facteur principal de votre décision ?': g.user['facteur'],
      'Comment vous voyez-vous dans 5 ans  après avoir votre diplôme?': g.user['vision'],
     'Résidence':  g.user['residence'],
     'Les conditions matérielles et financières disponibles\t': g.user['conditon'],
     'sport': g.user['sport'],
     'culture': g.user['culture'],
     'JeuxColl': g.user['jeuxColl'],
     'Voyage': g.user['voyage'],
     'PcSkills': g.user['pc'],
     'TechnologySkills': g.user['technologie'],
     'VieAssociative': g.user['vieassociative'],
     'Arts': g.user['arts']})
    db = get_db()

    res = requests.post(url,data)

    try:
        a=res.json()
    except:
        a="error"
    return render_template('pred/jj.html', post=a)
@pred.route('/u', methods=('GET', 'POST'))

def update():
    if request.method == 'POST':
        specialite= request.form['specialite']
        proche= request.form['proche']
        residence = request.form['residence']
        connaissance = request.form['connaissance']
        emplacement = request.form['emplacement']
        influenceFamille = request.form['influenceFamille']

        facteur = request.form['facteur']




        id=g.user['id']
        db = get_db()



        db.execute(
        'UPDATE user SET specialite=?,proche=?, residence = ?, connaissance = ?, emplacement= ?,influenceFamille =?,facteur=?'
        ' WHERE id = ?',(specialite,proche ,residence,connaissance,emplacement,influenceFamille,facteur,id,)
        )
        db.commit()
        return redirect(url_for('pred.index1'))

    return redirect(url_for('pred.index1'))







@pred.route('/a')

def a():

    if(not g.user['profession']):
        return redirect(url_for('profile.update'))

    url="https://orientation-model.herokuapp.com/model2/suggest"
    data=json.dumps({'Profession':g.user['profession'],
       "Rang au concours national d'entrée aux écoles d'ingénieurs": g.user['rang'],
     "institut préparatoire aux études d'ingénieurs": g.user['institut'],
     'Spécialité/Prépa': g.user['specialitePrepa'],'baccalauréat': g.user['bac'],'Mention du baccalauréat': g.user['mentionBac'],
       'Comment vous voyez-vous dans 5 ans  après avoir votre diplôme?': g.user['vision'],

     'Les conditions matérielles et financières disponibles\t': g.user['conditon'],
     'sport': g.user['sport'],
     'culture': g.user['culture'],
     'JeuxColl': g.user['jeuxColl'],
     'Voyage': g.user['voyage'],
     'PcSkills': g.user['pc'],
     'TechnologySkills': g.user['technologie'],
     'VieAssociative': g.user['vieassociative'],
     'Arts': g.user['arts']})
    res = requests.post(url,data)
    try:
        a=res.json()
        

    except:
        a="error"
    return render_template('pred/index.html', post=a)

from flask import Flask,abort,jsonify,request
from sklearn.model_selection import train_test_split
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
m2 = Blueprint('model2', __name__, url_prefix='/model2')



def distance(x,y):
    diffs=0
    for i in range (min(len(x),len(y))):
        diffs += pow(x[i]-y[i], 2)



    return math.sqrt(diffs)

def myFunc(e):
    return e[0]

def plusProche(x,kl=50):
   data=pd.read_excel("pred.xlsx")
   data.drop(columns="Avez vous quelqu'un de tes proches dans la même spécialité ?",axis=1,inplace=True)
   data.drop(columns='Quels sont vos intérêts ?',axis=1,inplace=True)
   data.drop(columns='les connaissances à propos de la filière choisie ont été acquises pendant',axis=1,inplace=True)
   data.drop(columns="L'emplacement de l'école a-t-il influé votre choix ?",axis=1,inplace=True)
   data.drop(columns="Quel est le degré d'influence de la famille et de l'entourage dans la prise de décision ? (0 si vous avez fait votre choix sans aucune intervention) ",axis=1,inplace=True)
   data.drop(columns='Quel est le facteur principal de votre décision ?',axis=1,inplace=True)
   data.drop(columns='Résidence',axis=1,inplace=True)
   y=data[['Spécialité','Vous êtes satisfait ']]
   X=data.drop(columns='Vous êtes satisfait ',axis=1)


   result=dict()

   result['Informatique']=[]
   result['Telecommunication']=[]
   result['Indus']=[]
   result['Mecanique']=[]
   result['Electrique']=[]
   result['Civil']=[]
   distances=[]


   un=0

   for i in range(0, len(X)):
       distances.append((distance(X.iloc[i],x),y.iloc[i][0],y.iloc[i][1]))

   distances.sort(key=myFunc)

   for d in distances[:kl]:

       if int(d[1])==0:
           result['Informatique'].append(str(d[2]))
       elif int(d[1])==1:
           result['Telecommunication'].append(str(d[2]))
       elif int(d[1])==2:
           result['Indus'].append(str(d[2]))
       elif int(d[1])==3:
           result['Mecanique'].append(str(d[2]))
       elif int(d[1])==4:
           result['Electrique'].append(str(d[2]))
       else:
           result['Civil'].append(str(d[2]))
   del distances[:]
   return result

@m2.route('/suggest',methods=['POST'])
def make_predict():

		data=request.get_json(force=True)
		d=[[data[i] for i in data]]
		predict_request=pd.DataFrame(np.array(d).reshape(1,16),columns=['Profession',
       "Rang au concours national d'entrée aux écoles d'ingénieurs",
        "institut préparatoire aux études d'ingénieurs",
       'Spécialité/Prépa', 'baccalauréat', 'Mention du baccalauréat',
       'Comment vous voyez-vous dans 5 ans  après avoir votre diplôme?',
       'Les conditions matérielles et financières disponibles\t',
       'sport', 'culture', 'JeuxColl', 'Voyage', 'PcSkills',
       'TechnologySkills', 'VieAssociative', 'Arts'])
		rez=plusProche(predict_request.iloc[0])

		print(rez)
		return jsonify(rez)

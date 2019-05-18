from flask import Flask
import numpy as np
from flask import Flask,abort,jsonify,request
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import math
from imblearn.over_sampling import SMOTE, ADASYN
from sklearn.preprocessing import StandardScaler
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
m1 = Blueprint('model1', __name__, url_prefix='/model1')


d1=[0,1,6,7,9,14]
def distance(x,y,l):
    diffs=0

    for i in range (min(len(x),len(y.iloc[0]))):
        if i in d1 :


            if(x[i]!=y.iloc[0][i]):

                diffs += pow((x[i]-y[i]), 2)*l[i]*100
        else :

            if(x[i]!=y[i].iloc[0]):
                diffs += l[i]*100

    return math.sqrt(diffs)
def myFunc(e):
    return e[0]
def predictX(x,X,y,l,kl):
    distances=[]
    un=0
    for i in range(0, len(X)):

        distances.append((distance(X.iloc[i],x,l),y.iloc[i]))


    distances.sort(key=myFunc)
    print(distances[:10])

    for d in distances[0:kl]:
        if int(d[1]==1):
            un+=1

    if(un >= (kl/2)):
        return 1
    else :
        return 0
def predictY(yx,k=6):
    scaler = StandardScaler()
    data=pd.read_excel("new.xlsx")
    y=data['target']
    X=data.drop(columns='target',axis=1)


    array = data.values
    li=X.columns
    Xe = X.values
    Ye = y.values
# feature extraction
    model = ExtraTreesClassifier(n_estimators=10)
    model.fit(Xe, Ye)
    l=model.feature_importances_

    X, y = ADASYN().fit_resample(X, y)
    scaler.fit(X)
    scaled_features1 = scaler.transform(X)
    scaled_features2 = scaler.transform(yx)

    yx=pd.DataFrame(scaled_features2)
    X=pd.DataFrame(scaled_features1)
    y=pd.DataFrame(y)















    result=predictX(yx,X,y,l,k)



    return np.array(result)
@m1.route('/own',methods=['POST'])
def make_predict():

    data=request.get_json(force=True)
    d=[[data[i] for i in data]]
    predict_request=pd.DataFrame(np.array(d).reshape(1,23),columns=['Profession',"Rang au concours national d'entrée aux écoles d'ingénieurs",
    'Spécialité',
    "institut préparatoire aux études d'ingénieurs",
   'Spécialité/Prépa', 'baccalauréat', 'Mention du baccalauréat',
   'les connaissances à propos de la filière choisie ont été acquises pendant',
   "L'emplacement de l'école a-t-il influé votre choix ?",
   "Quel est le degré d'influence de la famille et de l'entourage dans la prise de décision ? (0 si vous avez fait votre choix sans aucune intervention) ",
   "Avez vous quelqu'un de tes proches dans la même spécialité ?",
   'Quel est le facteur principal de votre décision ?',
   'Comment vous voyez-vous dans 5 ans  après avoir votre diplôme?',
   'Résidence', 'Les conditions matérielles et financières disponibles\t',
   'sport', 'culture', 'JeuxColl', 'Voyage', 'PcSkills',
   'TechnologySkills', 'VieAssociative', 'Arts'])


    rez=predictY(predict_request)


    return jsonify(results=int(rez))

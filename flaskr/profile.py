from functools import wraps
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_bootstrap import Bootstrap
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.auth import login_required
from flaskr.db import get_db
p = Blueprint('profile', __name__, url_prefix='/profile')



@p.route('/index')
@login_required
def index():

    return render_template('profile/profile.html')
@p.route('/post')
@login_required
def post():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE u.id = ?'

        ' ORDER BY created DESC',
        (g.user['id'],)

    ).fetchall()

    return render_template('profile/ll.html',posts=posts)

@p.route('/update', methods=('GET', 'POST'))
@login_required
def update():
    if request.method == 'POST':
        profession = request.form['profession']
        rang = request.form['rang']

        institut = request.form['institut']
        specialitePrepa = request.form['specialitePrepa']
        bac = request.form['bac']
        mentionBac = request.form['mentionBac']



        vision = request.form['vision']

        conditon = request.form['condition']


        jeuxColl=request.form['jeuxColl']
        Sport = request.form['sport']
        Arts=request.form['Arts']

        Voyage=request.form['Voyage']
        VieAssociative=request.form['VieAssociative']
        TechnologySkills=request.form['Technologie']
        PcSkills=request.form['PcSkills']
        culture=request.form['culture']




        id=g.user['id']
        db = get_db()



        db.execute(
        'UPDATE user SET profession=?,rang=?, institut = ?, specialitePrepa = ?, bac = ?,mentionBac =?,jeuxColl=?,sport=?,arts=?,voyage=?,vieassociative=?,technologie=?,pc=?,culture=?,vision=?,conditon=?'
        ' WHERE id = ?',(profession,rang , institut,specialitePrepa,bac,mentionBac,jeuxColl,Sport,Arts,Voyage,VieAssociative,TechnologySkills,PcSkills,culture,vision,conditon,id,)
        )
        db.commit()

    return render_template('profile/update.html')

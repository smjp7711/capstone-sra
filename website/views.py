from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from io import TextIOWrapper
from flask_sqlalchemy import SQLAlchemy
from .models import Student
import csv
from flask_mail import Message
from website import mail


views = Blueprint('views', __name__)

db = SQLAlchemy()

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method =='POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            student = Student(tNumber=row[0], firstName=row[1], middleName=row[2], lastName=row[3], 
            term=row[4], level=row[5], pProgram=row[6], 
            pPname=row[7], pCollege=row[8], 
            pDept=row[9], pDeptDesc=row[10], sProgram=row[11], sPname=row[12], sCollege=row[13], sDept=row[14], 
            sDeptDesc=row[15], decision=row[16], admit=row[17], sAddress1=row[18], sAddress2=row[19], city=row[20], state=row[21], 
            zip=row[22], phoneArea=row[23], phoneNum=row[24], phoneNumEx=row[25], email=row[26], ualrEmail=row[27], ethnicity=row[28], sex=row[29], admission=row[30], 
            studentType=row[31])
            db.session.add(student)
            db.session.commit()
        flash('File successfully uploaded!', category='success')
        return redirect(url_for('views.home'))
    return render_template("home.html", user=current_user)

@views.route('/sra_admin', methods=['GET', 'POST'])
def sra_admin():
    if request.method =='POST':
        msg = Message("Hello", sender="sra_capstonegroup3_mrww@protonmail.com", recipients=["sjuarez@ualr.edu, nblarimore@ualr.edu"])
        msg.body = "This is a test from our SRA_app"
        mail.send(msg)
        flash('Email succesfully sent!', category="success")
  
    return render_template("sra_admin.html", user=current_user)


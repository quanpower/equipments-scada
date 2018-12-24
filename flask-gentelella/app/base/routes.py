from bcrypt import checkpw
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User, Record

from flask_wtf import FlaskForm,CsrfProtect
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Required, DataRequired
import time



@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/record')
def record():
    record_A = Record.query.filter_by(AorB='A').order_by(Record.datetime.desc()).first()
    print('-----record_A-------')
    print(record_A)
    record_B = Record.query.filter_by(AorB='B').order_by(Record.datetime.desc()).first()
    record_A_dict = {'ticketNo':record_A.ticketNo, 'heatNo':record_A.heatNo, 'quantity':record_A.quantity, 
    'productHeight':record_A.productHeight,'ringHeight':record_A.ringHeight, 'jobNo':record_A.jobNo, 'datetime':record_A.datetime}

    record_B_dict = {'ticketNo':record_B.ticketNo, 'heatNo':record_B.heatNo, 'quantity':record_B.quantity, 
    'productHeight':record_B.productHeight,'ringHeight':record_B.ringHeight, 'jobNo':record_B.jobNo, 'datetime':record_B.datetime}

    record_latest = {'record_latest':{
    'record_A':record_A_dict,'record_B':record_B_dict
    }}


    return jsonify(record_latest)



@blueprint.route('/records')
def records():
    records = Record.query.all()
    record_list = []
    for record in records:
        record_dict = {'AorB':record.AorB, 'ticketNo':record.ticketNo, 'heatNo':record.heatNo, 'quantity':record.quantity, 
    'productHeight':record.productHeight,'ringHeight':record.ringHeight, 'jobNo':record.jobNo, 'datetime':record.datetime}
        record_list.append(record_dict)

    return jsonify(record_list[::-1])


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')


@blueprint.route('/fixed_<template>')
@login_required
def route_fixed_template(template):
    return render_template('fixed/fixed_{}.html'.format(template))


@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))

## Login & Registration


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and checkpw(password.encode('utf8'), user.password):
            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))
        return render_template('errors/page_403.html')
    if not current_user.is_authenticated:
        return render_template(
            'login/login.html',
            login_form=login_form,
            create_account_form=create_account_form
        )

    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/create_user', methods=['POST'])
def create_user():
    user = User(**request.form)
    db.session.add(user)
    db.session.commit()
    return jsonify('success')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

## Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500

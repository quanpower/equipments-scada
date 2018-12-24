from app.forms import blueprint
from flask_login import login_required
from flask import jsonify, render_template, redirect, request, url_for, flash

from app import db, login_manager
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User, Record

from flask_wtf import FlaskForm,CsrfProtect
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Required, DataRequired
import time

WTF_CSRF_ENABLED = False


class HeatForm(FlaskForm):
    ticketNo_A = StringField(label='ticketNo', render_kw={"required":"required", "class":"form-control"})
    heatNo_A = StringField(label='heatNo', render_kw={"required":"required", "class":"form-control"})
    quantity_A = StringField(label='quantity', render_kw={"required":"required", "class":"form-control"})
    productHeight_A = StringField(label='productHeight', render_kw={"required":"required", "class":"form-control"})
    ringHeight_A = StringField(label='ringHeight', render_kw={"required":"required", "class":"form-control"})
    jobNo_A = StringField(label='jobNo', render_kw={"required":"required", "class":"form-control"})


    ticketNo_B = StringField(label='ticketNo', render_kw={ "class":"form-control"})
    heatNo_B = StringField(label='heatNo', render_kw={ "class":"form-control"})
    quantity_B = StringField(label='quantity', render_kw={ "class":"form-control"})
    productHeight_B = StringField(label='productHeight', render_kw={ "class":"form-control"})
    ringHeight_B = StringField(label='ringHeight', render_kw={ "class":"form-control"})
    jobNo_B = StringField(label='jobNo', render_kw={ "class":"form-control"})
    

    submit = SubmitField('提交', render_kw={"class":"btn btn-success"})



@blueprint.route('/form', methods=['POST','GET'])
def form():
    print('-------request.form------')

    # return jsonify('---success---')

    form = HeatForm()

    if form.validate_on_submit():   # 如果form表单以submit进行提交，且用户填写的字段通过validators验证器，那么条件为真（submit提交方式就是“POST”）
        a_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
            AorB = 'A',
            ticketNo = form.ticketNo_A.data,
            heatNo = form.heatNo_A.data,
            quantity = form.quantity_A.data,
            productHeight = form.productHeight_A.data,
            ringHeight = form.ringHeight_A.data,
            jobNo = form.jobNo_A.data,
            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )
        db.session.add(a_obj)

        if form.ticketNo_B.data:
            b_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
                AorB = 'B',
                ticketNo = form.ticketNo_B.data,
                heatNo = form.heatNo_B.data,
                quantity = form.quantity_B.data,
                productHeight = form.productHeight_B.data,
                ringHeight = form.ringHeight_B.data,
                jobNo = form.jobNo_B.data,
                datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            )
            db.session.add(b_obj)

        db.session.commit()
        flash('submit successfully!')


        # 文字提示 flash
        return render_template('form.html', form=form) 
               # 跳转到admin页
    # return render_template('form.html',form=form)
    # if request.method == 'POST':
    #     # request.form.get('userpass')
    #     formData = request.form
    #     print(formData)

    #     a_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
    #         AorB = 'A',
    #         ticketNo = formData.get('ticketNo'),
    #         heatNo = formData.get('heatNo'),
    #         quantity = formData.get('quantity'),
    #         productHeight = formData.get('productHeight'),
    #         ringHeight = formData.get('ringHeight'),
    #         jobNo = formData.get('jobNo'),
    #         datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     )
    #     db.session.add(a_obj)

    #     if formData.get('ticketNo_B'):
    #         b_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
    #             AorB = 'B',
    #             ticketNo = formData.get('ticketNo_B'),
    #             heatNo = formData.get('heatNo_B'),
    #             quantity = formData.get('quantity_B'),
    #             productHeight = formData.get('productHeight_B'),
    #             ringHeight = formData.get('ringHeight_B'),
    #             jobNo = formData.get('jobNo_B'),
    #             datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         )
    #         db.session.add(b_obj)
    #     db.session.commit()
    #     return render_template('form.html')

    return render_template('form.html', form=form)




# @blueprint.route('/form', methods=['POST','GET'])
# def form():
#     print('-------request.form------')
#     # print(request.form)
#     # record = Record(**request.form)
#     # print(record)
#     # db.session.add(record)
#     # db.session.commit()
    
#     # return jsonify('---success---')

#     # form = HeatForm()
#     # if form.validate_on_submit():   # 如果form表单以submit进行提交，且用户填写的字段通过validators验证器，那么条件为真（submit提交方式就是“POST”）
#     #     new_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
#     #       AorB = 'B',
#     #         ticketNo = form.ticketNo.data,
#     #         heatNo = form.heatNo.data,
#     #         quantity = form.quantity.data,
#     #         productHeight = form.productHeight.data,
#     #         ringHeight = form.ringHeight.data,
#     #         jobNo = form.jobNo.data,
#     #         datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     #     )
#     #     db.session.add(new_obj)
#     #     db.session.commit()
#     #     # 文字提示 flash
#     #     return 'ok'         # 跳转到admin页
#     # return render_template('form.html',form=form)
#     if request.method == 'POST':
#         # request.form.get('userpass')
#         formData = request.form
#         new_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
#             AorB = 'B',
#             ticketNo = formData.get('ticketNo'),
#             heatNo = formData.get('heatNo'),
#             quantity = formData.get('quantity'),
#             productHeight = formData.get('productHeight'),
#             ringHeight = formData.get('ringHeight'),
#             jobNo = formData.get('jobNo'),
#             datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         )
#         db.session.add(new_obj)
#         db.session.commit()

#         return render_template('form.html',form=form)
#     return render_template('form.html',form=form)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')



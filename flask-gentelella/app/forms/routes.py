from app.forms import blueprint
from flask_login import login_required
from flask import jsonify, render_template, redirect, request, url_for

from app import db, login_manager
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User, Record

from flask_wtf import FlaskForm,CsrfProtect
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Required, DataRequired
import time



class HeatForm(FlaskForm):
    ticketNo = StringField(label='ticketNo',validators=[DataRequired("请输入标题")],description="请输入标题",render_kw={"required":"required"})
    heatNo = StringField(label='heatNo',validators=[DataRequired("请输入标题")],description="请输入标题",render_kw={"required":"required"})
    quantity = StringField(label='quantity',validators=[DataRequired("请输入标题")],description="请输入标题",render_kw={"required":"required"})
    productHeight = StringField(label='productHeight',validators=[DataRequired("请输入标题")],description="请输入标题",render_kw={"required":"required"})
    ringHeight = StringField(label='ringHeight',validators=[DataRequired("请输入标题")],description="请输入标题",render_kw={"required":"required"})
    jobNo = StringField(label='jobNo',validators=[DataRequired("请输入标题")],description="请输入标题",render_kw={"required":"required"})
    
    submit = SubmitField('提交')



@blueprint.route('/form', methods=['POST','GET'])
def form():
    print('-------request.form------')
    # print(request.form)
    # record = Record(**request.form)
    # print(record)
    # db.session.add(record)
    # db.session.commit()
    
    # return jsonify('---success---')

    # form = HeatForm()
    # if form.validate_on_submit():   # 如果form表单以submit进行提交，且用户填写的字段通过validators验证器，那么条件为真（submit提交方式就是“POST”）
    #     new_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
    #       AorB = 'B',
    #         ticketNo = form.ticketNo.data,
    #         heatNo = form.heatNo.data,
    #         quantity = form.quantity.data,
    #         productHeight = form.productHeight.data,
    #         ringHeight = form.ringHeight.data,
    #         jobNo = form.jobNo.data,
    #         datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     )
    #     db.session.add(new_obj)
    #     db.session.commit()
    #     # 文字提示 flash
    #     return 'ok'         # 跳转到admin页
    # return render_template('form.html',form=form)
    if request.method == 'POST':
        # request.form.get('userpass')
        formData = request.form
        print(formData)

        a_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
            AorB = 'A',
            ticketNo = formData.get('ticketNo'),
            heatNo = formData.get('heatNo'),
            quantity = formData.get('quantity'),
            productHeight = formData.get('productHeight'),
            ringHeight = formData.get('ringHeight'),
            jobNo = formData.get('jobNo'),
            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )
        db.session.add(a_obj)

        if  formData.get('ticketNo_B'):
            b_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
                AorB = 'B',
                ticketNo = formData.get('ticketNo_B'),
                heatNo = formData.get('heatNo_B'),
                quantity = formData.get('quantity_B'),
                productHeight = formData.get('productHeight_B'),
                ringHeight = formData.get('ringHeight_B'),
                jobNo = formData.get('jobNo_B'),
                datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            )
            db.session.add(b_obj)
        db.session.commit()

        return 'ok'
    return render_template('form.html',form=form)




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



    # form = HeatForm()
    # if form.validate_on_submit():   # 如果form表单以submit进行提交，且用户填写的字段通过validators验证器，那么条件为真（submit提交方式就是“POST”）
    #     new_obj = Record(             # 使用flask-sqlalchemy定义的一个表结构 
    #       AorB = 'B',
    #         ticketNo = form.ticketNo.data,
    #         heatNo = form.heatNo.data,
    #         quantity = form.quantity.data,
    #         productHeight = form.productHeight.data,
    #         ringHeight = form.ringHeight.data,
    #         jobNo = form.jobNo.data,
    #         datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     )
    #     db.session.add(new_obj)
    #     db.session.commit()
    #     # 文字提示 flash
    #     return 'ok'         # 跳转到admin页
    # return render_template('form.html',form=form)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')



from flask_admin import Admin
from craft import app, file_path,db
from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import form
from flask_admin.contrib import sqla
from flask_admin.menu import MenuLink
from craft.models import Users,Feedback,Products,Order







admin = Admin(app) 


class FileView(sqla.ModelView):
    form_overrides = {
        'image_file' : form.FileUploadField
    }

    form_args = {
        'image_file' : {
            'label' : 'Image' ,
            'base_path' : file_path,
            'allow_overwrite' : False
        }
    }
    form_excluded_columns = ['Orders']

class StatusView(sqla.ModelView):
    
    form_choices = {
        'status' : [
            ('Order Placed','Order Placed'),
            ('Order Processing','Order Processing'),
            ('Order Shipped','Order Shipped'),
            ('Order Delivered','Order Delivered')
        ]
    }

    can_create = False
    can_delete = False

class FeedbackView(sqla.ModelView):
    

    can_create = False 
    can_edit = False

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)

class UsersView(sqla.ModelView): 
    column_exclude_list = ('password')
   
logout_link = MenuLink('Logout','/logout','logout')

admin.add_link(logout_link)
admin.add_view(StatusView(Order,db.session))
admin.add_view(FileView(Products,db.session))     
admin.add_view(UsersView(Users,db.session))
admin.add_view(FeedbackView(Feedback,db.session))
#admin.add_view(ModelView(Products,db.session))
#admin.add_view(ModelView(Order,db.session))

@app.route("/adminlogout")
def adminlogout():
    session.clear()
    return redirect("/")

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == "POST":
        if request.form.get("username") == "krish" and request.form.get("password") == "123456789":
            session['logged_in'] = True
            return redirect("/admin")
        else:
            return render_template("adminlogin.html", failed=True)
    return render_template("adminlogin.html")
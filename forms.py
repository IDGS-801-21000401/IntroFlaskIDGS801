from wtforms import Form,StringField,IntegerField,EmailField


class UserForm(Form):
    nombre = StringField("nombre")
    apaterno = StringField("apaterno")
    amaterno = StringField("amaterno")
    email = EmailField("email")
    edad = IntegerField("edad")
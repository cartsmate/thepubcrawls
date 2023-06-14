from flask import render_template
from app import app
from config import Configurations
from app.models.pub.pub import Pub

config = Configurations().get_config()


@app.route("/test")
def pub_test():
    print('/test')
    new_pub = Pub()
    # newNew = Pub()
    # print(new_pub.__dict__.keys())
    print(list(Pub().__dict__.keys()))
    print(vars(new_pub))
    # print(newNew.__dict__.keys())
    return render_template('pub_test.html')

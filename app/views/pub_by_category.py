from flask import render_template
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
function = Functions()



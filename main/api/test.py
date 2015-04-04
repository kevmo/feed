from flask import Blueprint, current_app as app

web_bp = Blueprint('web', __name__)

@web_bp.route("/trill")
def get_trill_config():
  with app.app_context():
    print app.config['TRILL']

  return "SUP"
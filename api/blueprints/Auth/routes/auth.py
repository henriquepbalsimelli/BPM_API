from flask import Blueprint
from database.user import User
from ext.database import db


bp_auth = Blueprint("Auth", __name__)


@bp_auth.route('/get-user', methods=['GET'])
def get_user():
    users = db.session.query(User).all()

    return [user.to_dict() for user in users]
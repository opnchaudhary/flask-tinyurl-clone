# coding:utf-8
from flask import jsonify, request, url_for

from app import db
from app.api import bp
from app.api.models import Url
from app.api.utils import generate_key, respond201, respond404, respond422


@bp.route('/create/', methods=['POST'])
def create_url():
    data = request.get_json()
    if 'url' in data:
        url = Url.query.filter_by(value=data['url']).first()
        if url:
            return respond201(url_for('api.parse_url', key = url.key))
        else:
            generated_key = generate_key(data['url'])
            url = Url(key=generated_key, value=data['url'])
            db.session.add(url)
            db.session.commit()
            return respond201(url_for('api.parse_url', key=generated_key))
    else:
        return respond422()
    


@bp.route('/parse/<key>', methods=['GET'])
def parse_url(key):
    url = Url.query.get(key)
    if url:
        return jsonify({'key':key, 'value':url.value})
    else:
        return respond404()

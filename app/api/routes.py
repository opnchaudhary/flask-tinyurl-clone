# coding:utf-8
from flask import jsonify, request, url_for


from app import db, redis
from . import bp
from .models import Url
from .utils import generate_key, respond201, respond404, respond422


@bp.route('/create', methods=['POST'])
def create_url():
    data = request.get_json()
    if 'url' in data:
        cached = redis.get(data['url'])
        if cached:
            return respond201(url_for('api.parse_url', key = cached))
        else:
            url = Url.query.filter_by(value=data['url']).first()
            if url:
                redis.set(data['url'], url.key)
                return respond201(url_for('api.parse_url', key = url.key))
            else:
                generated_key = generate_key(data['url'])
                redis.set(data['url'], generated_key)
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
        redis.set(url.value, key)
        return jsonify({'key':key, 'value':url.value})
    else:
        return respond404()

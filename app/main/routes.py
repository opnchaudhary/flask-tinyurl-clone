# coding:utf-8
from flask import abort, flash, redirect, render_template, url_for

from app import db, redis
from app.main import bp
from app.api.models import Url
from app.api.utils import generate_key
from app.main.forms import URLShortenerForm

@bp.route('/', methods=['GET', 'POST'])
def home():
    form = URLShortenerForm()
    if form.validate_on_submit():
        print("Form validated")
        cached = redis.get(form.url.data)
        if cached:
            short_url = cached
        else:
            url = Url.query.filter_by(value=form.url.data).first()
            if url:
                redis.set(form.url.data, url.key)
                short_url = url.key
            else:
                generated_key = generate_key(form.url.data)
                redis.set(form.url.data, generated_key)
                url = Url(key=generated_key, value=form.url.data)
                db.session.add(url)
                db.session.commit()
                short_url = generated_key
        flash('Short url: '+ url_for('.url_parser', key=short_url,
            _external=True)[:-1] , 'success')
        return redirect(url_for('.home'))
    return render_template('home.html', title='TinyUrl Flask App', form=form)

@bp.route('/<key>/')
def url_parser(key):
    url = Url.query.filter_by(key=key).first()
    print("parsing url")
    if url:
        return redirect(url.value)
    else:
        abort(404)

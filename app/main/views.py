from flask import render_template, flash, session, redirect, url_for, request, make_response, json, current_app
from flask_login import logout_user, login_required, login_user
from .forms import ArticleForm, ArticleFormUpdate, ArticleFormDelete
from ..models import User, Article, Store
from datetime import datetime
from . import main
from .. import db

@main.route('/')
def index():
    claro = len(Article.query.filter_by(store_id = 1).all())
    sanborns = len(Article.query.filter_by(store_id = 2).all())
    sears = len(Article.query.filter_by(store_id = 3).all())
    return render_template('index.html', claro=claro, sanborns=sanborns, sears=sears)

@main.route('/claroshop')
@login_required
def claroshop():
    articles = Article.query.filter_by(store_id = 1).all()
    total = len(articles)

    page = request.args.get('page', 1, type=int)
    pagination = Article.query.filter_by(store_id = 1)\
    .order_by(Article.timestamp.desc())\
    .paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    articles = pagination.items
    
    showed = len(articles)
    
    return render_template('claroshop.html', articles=articles, showed=showed, total=total, pagination=pagination)

@main.route('/sanborns')
@login_required
def sanborns():
    articles = Article.query.filter_by(store_id = 2).all()
    total = len(articles)

    page = request.args.get('page', 1, type=int)
    pagination = Article.query.filter_by(store_id = 2)\
        .order_by(Article.timestamp.desc())\
            .paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    articles = pagination.items
    showed = len(articles)

    return render_template('sanborns.html',  articles=articles, showed=showed, total=total, pagination=pagination)

@main.route('/sears')
@login_required
def sears():
    articles = Article.query.filter_by(store_id = 3).all()
    total = len(articles)

    page = request.args.get('page', 1, type=int)
    pagination = Article.query.filter_by(store_id = 3)\
        .order_by(Article.timestamp.desc())\
            .paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    articles = pagination.items
    showed = len(articles)

    return render_template('sears.html', articles=articles, showed=showed, total=total, pagination=pagination)

## Add article section
@main.route('/add/claroshop', methods=['GET', 'POST'])
@login_required
def add_claroshop():
    form = ArticleForm()
    id_route = Store.query.filter_by(name="claroshop").first()
    if form.validate_on_submit():
        title = form.title.data
        image = form.image.data
        url = form.url.data
        article = Article(title, image, url, id_route.id)
        db.session.add(article)
        db.session.commit()
        flash("Regristro agregado correctamente")
        return redirect(url_for('.claroshop'))
    return render_template('claro_form.html', form=form)

@main.route('/add/sanborns', methods=['GET', 'POST'])
@login_required
def add_sanborns():
    form = ArticleForm()
    id_route = Store.query.filter_by(name="sanborns").first()
    if form.validate_on_submit():
        title = form.title.data
        image = form.image.data
        url = form.url.data
        article = Article(title, image, url, id_route.id)
        db.session.add(article)
        db.session.commit()
        flash("Regristro agregado correctamente")
        return redirect(url_for('.sanborns'))
    return render_template('sanborns_form.html', form=form)

@main.route('/add/sears', methods=['GET', 'POST'])
@login_required
def add_sears():
    form = ArticleForm()
    id_route = Store.query.filter_by(name="sears").first()
    if form.validate_on_submit():
        title = form.title.data
        image = form.image.data
        url = form.url.data
        article = Article(title, image, url, id_route.id)
        db.session.add(article)
        db.session.commit()
        flash("Registro agregado correctamente")
        return redirect(url_for('.sears'))
    return render_template('sears_form.html', form=form)

## Edit article section
@main.route('/claroshop/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def claroshop_edit(id):
    article = Article.query.filter(Article.id == id, Article.store_id == 1).first()
    if article:
        form = ArticleFormUpdate()
        if form.validate_on_submit():
            article.title = form.title.data
            article.image = form.image.data
            article.url = form.url.data
            db.session.add(article)
            db.session.commit()
            flash('Registro Actualizado', 'success')
            return redirect(url_for('.claroshop'))
    else:
        return redirect(url_for('.claroshop'))
    
    form.title.data = article.title
    form.image.data = article.image
    form.url.data = article.url
    return render_template('edit_claroshop.html', form=form)

@main.route('/sanborns/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def sanborns_edit(id):
    article = Article.query.filter(Article.id == id, Article.store_id == 2).first()
    if article:
        form = ArticleFormUpdate()
        if form.validate_on_submit():
            article.title = form.title.data
            article.image = form.image.data
            article.url = form.url.data
            db.session.add(article)
            db.session.commit()
            flash('Registro Actualizado', 'success')
            return redirect(url_for('.sanborns'))
    else:
        return redirect(url_for('.sanborns'))

    form.title.data = article.title
    form.image.data = article.image
    form.url.data = article.url
    return render_template('edit_sanborns.html', form=form)

@main.route('/sears/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def sears_edit(id):
    article = Article.query.filter(Article.id == id, Article.store_id == 3).first()
    if article:
        form = ArticleFormUpdate()
        if request.method == 'POST':
            article.title = form.title.data
            article.image = form.image.data
            article.url = form.url.data
            db.session.add(article)
            db.session.commit()
            flash('Registro Actualizado', 'success')
            return redirect(url_for('.sears'))
    else:
        return redirect(url_for('.sears'))
    form.title.data = article.title
    form.image.data = article.image
    form.url.data = article.url
    return render_template('edit_sears.html', form=form)

## Delete article section
@main.route('/claroshop/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_claroshop(id):
    article = Article.query.filter(Article.id == id, Article.store_id == 1).first()
    if article:
        if request.method == 'POST':
            db.session.delete(article)
            db.session.commit()
            flash("Registro Eliminado", "success")
            return redirect(url_for('.claroshop'))
    else:
        return redirect(url_for('.claroshop'))
    return render_template('confirm_delete.html', article=article)

@main.route('/sanborns/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def sanborns_delete(id):
    article = Article.query.filter(Article.id == id, Article.store_id == 2).first()
    if article:
        if request.method == 'POST':
            db.session.delete(article)
            db.session.commit()
            flash("Registro Eliminado", "success")
            return redirect(url_for('.sanborns'))
    else:
        return redirect(url_for('.sanborns'))
    return render_template('sanborns_delete.html', article=article)

@main.route('/sears/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def sears_delete(id):
    article = Article.query.filter(Article.id == id, Article.store_id == 3).first()
    if article:
        if request.method == 'POST':
            db.session.delete(article)
            db.session.commit()
            flash("Registro Eliminado", "success")
            return redirect(url_for('.sears'))
    else:
        return redirect(url_for('.sanborns'))
    return render_template('sears_delete.html', article=article)

## RSS Feed section
@main.route('/feed/claroshop')
def feed_claroshop():
    articles = Article.query.filter_by(store_id=1).all()
    template = render_template('claro_sitemap.xml', articles=articles)
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

@main.route('/feed/sanborns')
def feed_sanborns():
    articles = Article.query.filter_by(store_id=2).all()
    template = render_template('sanborns_sitemap.xml', articles=articles)
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

@main.route('/feed/sears')
def feed_sears():
    articles = Article.query.filter_by(store_id=3).all()
    template = render_template('sears_sitemap.xml', articles=articles)
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

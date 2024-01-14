from flask import render_template, url_for, flash, redirect, request
from flaskpresent import app, db
from flaskpresent.forms import PresentForm, price_check
from flaskpresent.models import Present, id_generator

# list of template urls for redirecting after deleting an item
templates = ['light', 'black', 'present', 'cards']


@app.route('/', methods=['GET', 'POST'])
@app.route('/light', methods=['GET', 'POST'])
def light():
    items = Present.query.all()
    form = PresentForm()
    if request.method == 'POST' and form.validate():
        id = id_generator(items)
        name = request.form.get('name')
        link = request.form.get('link')
        price = request.form.get('price')
        item = Present(id=id, name=name, link=link, price=price)
        db.session.add(item)
        db.session.commit()
        flash(f'{name} added to the present list!', 'success')
        return redirect('light')

    return render_template('indexLight.html', form=form, items=items, style_no=1, alert_tag="danger")


@app.route('/black', methods=['GET', 'POST'])
def black():
    items = Present.query.all()
    form = PresentForm()
    if request.method == 'POST' and form.validate():
        id = id_generator(items)
        name = request.form.get('name')
        link = request.form.get('link')
        price = request.form.get('price')
        item = Present(id=id, name=name, link=link, price=price)
        db.session.add(item)
        db.session.commit()
        flash(f'{name} added to the present list!', 'success')
        return redirect('black')
    return render_template('indexDark.html', form=form, items=items, style_no=2, alert_tag="warning")


@app.route('/present', methods=['GET', 'POST'])
def present():
    items = Present.query.all()
    form = PresentForm()
    if request.method == 'POST' and form.validate():
        id = id_generator(items)
        name = request.form.get('name')
        link = request.form.get('link')
        price = request.form.get('price')
        item = Present(id=id, name=name, link=link, price=price)
        db.session.add(item)
        db.session.commit()
        flash(f'{name} added to the present list!', 'success')
        return redirect('present')
    return render_template('indexPresent.html', form=form, items=items, style_no=3, alert_tag="info")


@app.route('/cards', methods=['GET', 'POST'])
def cards():
    items = Present.query.all()
    form = PresentForm()
    if request.method == 'POST' and form.validate():
        id = id_generator(items)
        name = request.form.get('name')
        link = request.form.get('link')
        price = request.form.get('price')
        item = Present(id=id, name=name, link=link, price=price)
        db.session.add(item)
        db.session.commit()
        flash(f'{name} added to the present list!', 'success')
        return redirect('cards')

    return render_template('indexCard.html', form=form, items=items, style_no=4, alert_tag="info")


@app.route('/about')
def about():
    return render_template('about.html', style_no=5)


@app.route('/delete/<int:style>/<int:present_id>', methods=['GET', 'POST'])
def delete_present(present_id, style):
    present = Present.query.get_or_404(present_id)
    db.session.delete(present)
    db.session.commit()
    flash('Present has been removed!', 'info')
    return redirect(url_for(templates[style-1]))



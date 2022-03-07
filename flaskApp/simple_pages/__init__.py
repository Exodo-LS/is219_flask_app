from flask import Blueprint, render_template, abort, Flask
from jinja2 import TemplateNotFound

bp = Blueprint('simple_pages', __name__,
               template_folder='templates', static_folder='static')


@bp.route('/page/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

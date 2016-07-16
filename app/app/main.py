from flask import Blueprint, render_template

import datetime

main = Blueprint(name='main', import_name=__name__)


@main.route('/')
def index():
    from . import logger
    logger().debug(
        'hello @ {}'.format(
            datetime.datetime.now().strftime('%c')
        )
    )

    return render_template('index.html')

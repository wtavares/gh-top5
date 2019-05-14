# -*- coding: utf-8 -*-
# --- author: wtavares
# --- Main APP

from flask import Flask
from web_app import web
import settings as cfg
import logging
from web_app.flask_adminlte import AdminLTE

app = Flask(__name__, template_folder="web_app/templates", static_folder='web_app/static')
app.secret_key = cfg.APP_KEY
AdminLTE(app)


# -----------------------------
# --- Web APP Microservice ----
# -----------------------------
@app.route("/", methods=['GET'])
def web_home():
    logging.info("Web Home request")
    return web.home()


@app.route("/update", methods=['GET'])
def web_update():
    logging.info("Web Home request")
    return web.update()


# --- Run
if __name__ == "__main__":
    if cfg.DRY_RUN:
        logging.info("DRYRUN Mode ON")

    app.run(host='0.0.0.0', port=int(cfg.APP_PORT))

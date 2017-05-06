#!/usr/bin/env python
#-*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import flask
import os
import yaml
import simplejson as json
import requests
from urllib.parse import quote
from flask import Response, make_response
import mwoauth
import mwoauth.flask
from requests_oauthlib import OAuth1
from flask_mwoauth import MWOAuth
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def index():
        username = flask.session.get('username', None)
	return flask.render_template('index.html', username=username)

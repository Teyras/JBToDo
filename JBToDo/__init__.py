# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from .db import get_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)

port = os.getenv('PORT', '5000')
manager.add_command('runserver', Server(host='0.0.0.0', port=int(port)))

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

import JBToDo.model
import JBToDo.views

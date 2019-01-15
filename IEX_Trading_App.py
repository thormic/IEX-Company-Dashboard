from bottle import (Bottle, route, run, template, get, post, debug,
                    static_file, request, redirect, response, hook)
import bottle
import beaker.middleware
import datetime
import sqlite3
import pandas as pd
import numpy as np
from iexfinance.stocks import get_historical_data
from api_func import GetHistData
from database_update import DatabaseConn
from table_html import TabHtml
from import_names import ImportNames, ShortName

bottle.TEMPLATE_PATH.insert(0, 'views')

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './session/',
    'session.auto': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./static')

@route('/')
def search():
    comp_names = ImportNames()
    list_of_companies = list(comp_names['full_name'])
    return template('start_screen', companies=list_of_companies)


@route('/company_chosen', method=['post', 'get'])
def show():
    company_name = request.forms.get('company')
    start_date = request.forms.get('start_date')
    end_date = request.forms.get('end_date')
    company = ShortName(company_name)
    request.session['results'] = DatabaseConn(company, start_date, end_date)
    table = TabHtml(request.session['results'])
    return template('company_chosen', company=company_name, data=table)

@route('/table')
def html_table():
    results = request.session['results']
    # results, company = DatabaseConn()
    table1 = TabHtml(results)
    return template('table', data=table1)

@route('/charts/')
@route('/charts')
def index(name="Anonymous"):
    results, company = DatabaseConn()
    chartData = {
"labels":list(results["date"]),
    "data" : {
        "{}".format(company):list(results["open"]),
    }
}
    return template('charts', name=name, chartData=chartData)


@route('/dashboard')
def lolek():
    return template('dashboard')






run(app=app, host='localhost', port=8081, debug=True, reloader=True)

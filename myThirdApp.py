from bottle import Bottle, route, run, template, get, post, debug, static_file, request, redirect, response
import bottle
import datetime
from iexfinance.stocks import get_historical_data
from api_func import GetHistData
from database import DatabaseConn
from table_html import TabHtml
import sqlite3
import pandas as pd
import numpy as np

bottle.TEMPLATE_PATH.insert(0, 'views')

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./static')

@route('/form')
@route('/form/')
def index(name="Anonymous"):
    return template('formExample', name=name)


@route('/formProcess')
@route('/formProcess/')
@route('/formProcess', method='POST')
@route('/formProcess/', method='POST')
def index(name="Anonymous"):
    print(request.forms.keys())
    myDict= {k:request.forms.getunicode(k) for k in request.forms.keys()}
    return template('formExampleProc', name=name, myDict=myDict)

@route('/charts/')
@route('/charts')
def index(name="Anonymous"):
    df, company = GetHistData()
    df1, company1 = GetHistData("FB")
    df2, company2 = GetHistData("TSLA")
    chartData = {
"labels":list(df["date"]),
    "data" : {
        "{}".format(company):list(df["volume"]),
        "{}".format(company1):list(df1["volume"]),
        "{}".format(company2):list(df2["volume"]),
    }
}
    return template('charts', name=name, chartData=chartData)

@route('/charts2/')
@route('/charts2')
def index(name="Anonymous"):
    results, company = DatabaseConn()
    chartData = {
"labels":list(results["date"]),
    "data" : {
        "{}".format(company):list(results["open"]),
    }
}
    return template('charts', name=name, chartData=chartData)

@route('/table')
def html_table():
    results, company = DatabaseConn()
    table1 = TabHtml(results)
    return template('table', data=table1)


@route('/')
def index(name="Maciej"):
    messDict = {'error': "Something went wrong",
                'ok': "Everything is ok."}
    return template('index', message=messDict.get("ok", ""), loginName=name, text="loremipsum example text")


@route('/dashboard')
def lolek():
    return template('dashboard')

@route('/search')
def search():
    # ! TU INNA FUNKCJA DO POBIERANIA MOŻLIWYCH NAZW SPÓŁEK
    results, company = DatabaseConn()
    return template('choose_screen', company=company)

@route('/john', method=['post', 'get'])
def show():
    company_name = request.forms.get('company')
    start_date = request.forms.get('start_date')
    end_date = request.forms.get('end_date')
    results, company = DatabaseConn(company_name, start_date, end_date)
    table = TabHtml(results)
    return template('john', company=company_name, data=table)






run(host='localhost', port=8081, debug=True, reloader=True)

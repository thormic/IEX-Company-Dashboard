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

# @route('/table')
# def html_table():
#     results, company = DatabaseConn()
#     table1 = TabHtml(results)
#     return template('table', data=table1)

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


@route('/bestMovies')
def index(name="Maciej"):
    messDict = {'error': "Something went wrong",
                'ok': "Everything is ok."}
    movies = [{"title":"Star Wars",
     "score":10,
     "review":"Lorem ipsum"},
    {"title":"Django",
     "score":9.9,
     "review":"Lorem ipsum"},
    {"title":"Fight Club",
     "score":9.95,
     "review":"Lorem ipsum"}]
     

    return template('movies', message=messDict.get("ok", ""), loginName=name, movies=movies)


@route('/dashboard')
def lolek():
    return template('dashboard')



run(host='localhost', port=8081, debug=True, reloader=True)
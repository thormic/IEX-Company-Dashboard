from bottle import (Bottle, route, run, template, get, post, debug,
                    static_file, request, redirect, response, hook)
import bottle
import beaker.middleware
import datetime
import sqlite3
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta
from iexfinance.stocks import get_historical_data
from api_func import GetHistData
from database_update import DatabaseConn
from database_download import DataDownload
from table_html import TabHtml
from import_names import ImportNames, ShortName
from comp_info import CompanyList, CompanyInfo
from create_tables import CreateTables
from get_info import GetInfo
from chart import CreatePlot
from company_type_dict import FindName
from add_note import AddNote, SeeNote

bottle.TEMPLATE_PATH.insert(0, 'views')

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './session/',
    'session.auto': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

CreateTables()

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./static')

@route('/')
@route('')
def search():
    request.session.clear()
    comp_names = ImportNames()
    list_of_companies = list(comp_names['full_name'])
    start_temp_date = str((datetime.datetime.today() - relativedelta(months=3)).strftime('%Y-%m-%d'))
    end_temp_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    return template('start_screen',
                    companies=list_of_companies,
                    start = start_temp_date,
                    end = end_temp_date)

@route('/main_dashboard', method=['post', 'get'])
def show():
    if request.session.get('company_name') is None:
        if request.forms.get('company') is not None:
            request.session['company_name'] = request.forms.get('company')
        else:
            request.session['company_name'] = 'Facebook Inc.'
        company_name = request.session['company_name']
    else:
        company_name = request.session['company_name']

    if request.session.get('start_date') is None:
        if request.forms.get('start_date') is not None:
            request.session['start_date'] = request.forms.get('start_date')
        else:
            start_temp_date = str((datetime.datetime.today() - relativedelta(months=3)).strftime('%Y-%m-%d'))
            request.session['start_date'] = start_temp_date
        start_date = request.session['start_date']
    else:
        start_date = request.session['start_date']

    if request.session.get('end_date') is None:
        if request.forms.get('end_date') is not None:
            request.session['end_date'] = request.forms.get('end_date')
        else:
            end_temp_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))
            request.session['end_date'] = end_temp_date
        end_date = request.session['end_date']
    else:
        end_date = request.session['end_date']

    if request.session.get('company_name') is not None:
        request.session['company'] = ShortName(company_name)
        company = request.session['company']
    else:
        company = request.session['company']
    CompanyInfo(company)
    request.session['results'] = DataDownload(company,
                                              start_date,
                                              end_date)
    request.session['company_info'] = GetInfo(company)
    results = request.session['results']
    company_info = request.session['company_info']
    # Tabels
    table = TabHtml(results)
    # Plots
    barplot = CreatePlot(df=results,
                         x='date',
                         y='volume',
                         type='barplot')
    scatterplot = CreatePlot(df=results,
                         x='date',
                         y='high_low_diff',
                         type='scatterplot')
    # Descriptive data
    ceo = company_info.iloc[0]['CEO']
    industry = company_info.iloc[0]['industry']
    website = company_info.iloc[0]['website']
    description = company_info.iloc[0]['description']
    issueType = FindName(company_info.iloc[0]['type'])
    sector = company_info.iloc[0]['sector']
    # Numerical data
    marketcap = company_info.iloc[0]['marketcap']
    marketcap = str("{:,}".format(marketcap)+ " $")
    week52high = company_info.iloc[0]['week52high']
    week52low = company_info.iloc[0]['week52low']
    percent_change = company_info.iloc[0]['ytdChangePercent']
    if percent_change > 0:
        percent_change = str("+ " + "{:.2%}".format(percent_change))
    else:
        percent_change = str("- " + "{:.2%}".format(percent_change))
    # Note
    note = SeeNote(company)
    return template('main_dashboard',
                    company=company_name,
                    table=table,
                    barplot = barplot,
                    scatterplot = scatterplot,
                    ceo=ceo,
                    industry = industry,
                    website = website,
                    description = description,
                    issuetype = issueType,
                    sector = sector,
                    marketcap = marketcap,
                    week52high = week52high,
                    week52low = week52low,
                    percent_change = percent_change,
                    start_date = start_date,
                    end_date = end_date,
                    note = note)

@route('/note')
def add_note():
    company = request.session['company']
    return template('note_add', company=company)

@route('/note_added', method=['post', 'get'])
def get_note():
    note = request.forms.get('note')
    company = request.session['company']
    AddNote(company, note)
    return template('note_get')

@route('/update')
def update_base():
    CompanyList()
    return template ('update_done')

run(app=app, host='localhost', port=8081, debug=True, reloader=True)

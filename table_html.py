from api_func import GetHistData
from database import DatabaseConn
import pandas as pd

def TabHtml(data):
    html_tab = data.to_html(index = False)
    #html_tab = html.append(data.to_html(na_rep = " ",index = False))
    # html_tab = data.style.set_table_styles([{'selector': 'thead th', 
    # 'props': [('background-color', 'red')]}, 
    # {'selector': 'thead th:first-child','props': [('display','none')]},
    # {'selector': 'tbody th:first-child',
    # 'props': [('display','none')]}]).render()
    return html_tab
    

    

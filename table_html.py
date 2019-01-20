import pandas as pd

def TabHtml(data):
    html_tab = data.to_html(index = False,
                            bold_rows=True,
                            classes='table'
                            )
    return html_tab

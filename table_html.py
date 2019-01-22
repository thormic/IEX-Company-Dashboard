import pandas as pd



def TabHtml(data):
    """
    Takes data DataFrame as an argument and returns html coded table.
    """
    html_tab = data.to_html(index = False,
                            bold_rows=True,
                            classes='table'
                            )
    return html_tab

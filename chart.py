import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json



def CreatePlot(df, x, y, type):
    """
    Takes df (pandas.DataFrame) argument, x and y, which are columns in df
    and type of the plot to be produced. returns json which is then compiled
    by plotly library into interactive plot.
    """
    if type == 'barplot':
        data = [
            go.Bar(
                name = '{}'.format(y),
                x=df['{}'.format(x)],
                y=df['{}'.format(y)],
                marker = dict(
                              color = '#5603ad'
                         )
            )]
        layout = dict(title = 'Value of {title} over chosen dates'.format(title = y),
                      yaxis=dict(
        title='{title}'.format(title = y.capitalize()),
        titlefont=dict(
            family='Sans Serif, monospace',
            size=16
                      )))
    elif type == 'scatterplot':
        data = [
            go.Scatter(
                name = '{}'.format(y),
                x=df['{}'.format(x)],
                y=df['{}'.format(y)],
                mode = 'lines+markers',
                marker = dict(
                              color = '#6c757d'
                         )

    )]
        layout = dict(title = 'Difference between highest and lowest day price',
                      yaxis = dict(
        title='Price difference',
        titlefont=dict(
            family='Sans Serif, monospace',
            size=16
        )))
    fig = dict(data=data, layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

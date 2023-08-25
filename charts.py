import csv
import numpy as np
import json

def bar_chart():
    # define the data to be passed to the JavaScript function
    data = {
            'labels': ['Shoplifting'
                        ,'Purse snatching'
                        ,'Bicycle theft'
                        ,'Vandalism'
                        ,'Vehicle theft'
                        ,'Assault'
                        ,'Burglary'
                        ,'Robbery'
                        ,'Fighting'
                        ,'Road rage'
                        ,'Gun-pointing'
                        ,'Explosion'
                        ,'Shooting'
                        ,'Normal'],
            'datasets': [{
                'label': 'Frequency',
                'data': [65, 59, 80, 81, 56, 55, 40, 65, 59, 80, 81, 56, 55, 33],
                'backgroundColor': [
                'rgba(1,255,255, 0.4)',
                'rgba(0,255,137, 0.4)',
                'rgba(255, 183, 255, 0.4)',
                'rgba(68,0,255, 0.4)',
                'rgba(185,201,255, 0.4)',
                'rgba(255,0,148, 0.4)',
                'rgba(242,243,0, 0.4)',
                'rgba(153,23,204, 0.4)',
                'rgba(37, 203, 241, 0.4)',
                'rgba(75, 192, 192, 0.4)',
                'rgba(71, 250, 0, 0.4)',
                'rgba(0,254,191, 0.4)'
                ],
                'borderColor': [
                'rgba(1,255,255)',
                'rgba(0,255,137)',
                'rgba(255, 183, 255)',
                'rgba(68,0,255)',
                'rgba(185,201,255)',
                'rgba(255,0,148)',
                'rgba(242,243,0)',
                'rgba(153,23,204)',
                'rgba(37, 203, 241)',
                'rgba(75, 192, 192)',
                'rgba(71, 250, 0)',
                'rgba(0,254,191)'
                ],
                'borderWidth': 1
            }]
            }

    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data


def line_chart():
    # define the data to be passed to the JavaScript function
    data = {
            'labels': ['September', 'October', 'November', 'December', 'January', 'February', 'March'],
            'datasets': [{
            'label': 'Reports',
            'data': [65, 59, 80, 81, 56, 55, 40],
            'fill': 'false',
            'borderColor': 'rgb(93, 192, 75)',
            'tension': 0.1
            }]
        }

    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data


def stacked_chart():
    # define the data to be passed to the JavaScript function
    data = {
            'labels': ['Shoplifting'
                        ,'Purse snatching'
                        ,'Bicycle theft'
                        ,'Vandalism'
                        ,'Vehicle theft'
                        ,'Assault'
                        ,'Burglary'
                        ,'Robbery'
                        ,'Fighting'
                        ,'Road rage'
                        ,'Gun-pointing'
                        ,'Explosion'
                        ,'Shooting'
                        ,'Normal'],
            'datasets': [{
                'label': 'High',
                'data': [75, 15, 18, 48, 74, 65, 40, 65, 59, 80, 81, 56, 55, 33],
                'backgroundColor': '#80FF01',
            },
            {
                'label': 'Medium',
                'data': [11, 1, 12, 62, 95, 33, 23, 90, 11, 42, 23, 12, 33, 22],
                'backgroundColor': '#40E2EB',
            },  
            {
                'label': 'Low',
                'data': [44, 5, 22, 35, 62, 20, 12, 44, 23, 6, 34, 2, 12, 12],
                'backgroundColor': '#9254EB',
            },
            ]
        }

    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data


def polar_chart():
    # define the data to be passed to the JavaScript function
    data = {
            'labels': [
            'Delhi',
            'Mumbai',
            'Kolkata',
            'Chennai',
            'Bangalore',
            'Hyderabad',
            'Ahmedabad',
            'Pune',
            'Surat',
            'Jaipur'

            ],
            'datasets': [{
            'label': 'Frequency',
            'data': [11, 16, 7, 3, 14, 17, 12, 19, 3, 5],
            'backgroundColor': [
                '#134949',
                '#FF0094',
                '#FF082C',
                '#00D3FF',
                '#F2F300',
                '#69F200',
                '#0040FE',
                '#FF01FF',
                '#00FF89'
            ]
            }]
        }


    # encode the data as a JSON object
    json_data = json.dumps(data)
    return json_data



import requests
import json
import pygal as p
import math
# from matplotlib import pyplot as p
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

req = requests.get(json_url)

# with open ('btc_close_2017_request.json', 'w') as f:
#     f.write(req.text)

# file_requests = req.json()
filename = 'btc_close_2017.json'

with open(filename) as f:
    btc_data = json.load(f)
    
date_list = []
close_list = []
for btc_dict in btc_data:
    date = btc_dict.get('date')
    month = btc_dict.get('month')
    week = btc_dict.get('week')
    weekday = btc_dict.get('weekday')
    close = float(btc_dict.get('close'))
    # print("{} is month {} week {}, {}, the close price is {}".format(date,month, week, weekday, close))
    date_list.append(date)
    close_list.append(close)
line_chart = p.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "Closed prices"
line_chart.x_labels = date_list
N = 20
line_chart.x_labels_major = date_list[::N]
close_log = [math.log(x) for x in close_list]
line_chart.add('Closed Price', close_log)
line_chart.render_to_file("4.svg")
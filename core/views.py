from django.shortcuts import render
import pandas as pd

url_dados = 'https://github.com/CSSEGISandData/COVID-19/blob/6069101a460264889fbab70daffba3dcbe24ed00/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv?raw=true'

dados = pd.read_csv(url_dados+'.csv')

def index(request):
    #print (dados[1])
    info = {
        'dados':dados} 
    return render(request, 'index.html',info)


def sobrenos(request):
    return render(request, 'sobrenos.html')


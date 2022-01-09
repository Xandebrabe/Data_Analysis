from django.shortcuts import render
import pandas as pd

#url_dados = 'https://github.com/CSSEGISandData/COVID-19/blob/6069101a460264889fbab70daffba3dcbe24ed00/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv?raw=true'

url_dados = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

dados_df = pd.read_csv(url_dados)

def index(request):
    #print(dados_df.iloc[ : , 4:dados_df.shape[1]])
    #print(dados_df[['Country/Region', '1/7/22']])
    info = {
        'dados':dados_df} 
    return render(request, 'index.html', info)


def sobrenos(request):
    return render(request, 'sobrenos.html')

""""
def menu(request, nome):
    paises = ["Brazil", "US", "Germany"]
    context = {
        'pais_selecionado': paises
    }
    return render(request, 'dados.html', context)
"""


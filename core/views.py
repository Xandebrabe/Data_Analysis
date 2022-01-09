from django.shortcuts import render
import pandas as pd

#url_dados = 'https://github.com/CSSEGISandData/COVID-19/blob/6069101a460264889fbab70daffba3dcbe24ed00/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv?raw=true'

url_dados = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

dados_df = pd.read_csv(url_dados)


#Pegando os países
flag = 0
paises = []
paises_totais = dados_df['Country/Region']

for i, pais in enumerate(paises_totais):
    for j in range(i+1, len(paises_totais)):
        if pais == paises_totais[j]:
            flag = 1
            break
    if flag == 0:
        paises.append(pais)
    flag = 0



def index(request):
    context = {
        'paises': paises
    }
    return render(request, 'index.html', context)


def sobrenos(request):
    context = {
        'paises': paises
    }
    return render(request, 'sobrenos.html', context)

#isso vai printar na tela a latitude, só que ele fala primeiro a posição, depois o item em si. Ex '0' '33.939110' 
def index(request):
    qualquercoisa = dados_df['Lat']
    context = {
        'teste':qualquercoisa
    }
    return render(request,'index.html',context)

""""
def menu(request, nome):
    paises = ["Brazil", "US", "Germany"]
    context = {
        'paises': paises
    }
    #print(dados_df.iloc[ : , 4:dados_df.shape[1]])
    #print(dados_df[['Country/Region', '1/7/22']])
    #paises = ["Brazil", "US", "Germany"]
    
    return render(request, 'dados.html', context)


from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#url_dados = 'https://github.com/CSSEGISandData/COVID-19/blob/6069101a460264889fbab70daffba3dcbe24ed00/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv?raw=true'

url_dados_casos = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_dados_mortes = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

dados_casos_df = pd.read_csv(url_dados_casos)
dados_mortes_df = pd.read_csv(url_dados_mortes)


#Pegando os países
flag = 0
paises = []
paises_totais = dados_casos_df['Country/Region']

for i, pais in enumerate(paises_totais):
    for j in range(i+1, len(paises_totais)):
        if pais == paises_totais[j]:
            flag = 1
            break
    if flag == 0:
        paises.append(pais)
    flag = 0


#isso vai printar na tela a latitude, só que ele fala primeiro a posição, depois o item em si. Ex '0' '33.939110' 
def index(request):
    qualquercoisa = dados_casos_df['Country/Region']
    context = {
        'paises': paises,
        'teste':qualquercoisa
    }
    return render(request, 'index.html', context)


def sobrenos(request):
    context = {
        'paises': paises
    }
    return render(request, 'sobrenos.html', context)


def dados(request, nome):

    dados_casos_pais = dados_casos_df.loc[dados_casos_df['Country/Region'] == nome]
    dados_mortes_pais = dados_mortes_df.loc[dados_mortes_df['Country/Region'] == nome]

    casos_ate_hoje = dados_casos_pais.iloc[:, -1].to_string().split()[1]  #Pegando o número de casos no país em questão até o dia atual
    mortes_ate_hoje = dados_mortes_pais.iloc[:, -1].to_string().split()[1]  #Pegando o número de mortes no país em questão até o dia atual

    # print(mortes_ate_hoje)
    #print(casos_ate_hoje)
    
    # nome_pais = dados_pais.dropna(how='all', axis=1).loc[1, ['Country/Region'][0]]  #deletando colunas vazias

    naldo = dados_casos_pais.iloc[:,4:-1]
    tnaldo = naldo.value_counts().plot.pie()
    
    #img = mpimg.imread(tnaldo+'.png')
    #imgplot = plt.imshow(img)
    #plt.show()

    print(naldo.to_string())
    context = {
        'paises': paises,
        'dados_pais': dados_casos_pais,
        'casos': casos_ate_hoje,
        'mortes': mortes_ate_hoje,
        'nome_pais': nome,
        'dia': tnaldo
    }
    
    return render(request, 'dados.html', context)


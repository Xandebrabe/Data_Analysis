from django.shortcuts import render
import pandas as pd
from .utils import pegar_plot

from .models import Paises


url_dados_casos = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_dados_mortes = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'


paises = Paises.objects.all()


def index(request):

    # Pegando dados do mundo:
    dados_casos_df = pd.read_csv(url_dados_casos)
    dados_mortes_df = pd.read_csv(url_dados_mortes)
    dados_casos_df.loc[len(dados_casos_df)] = dados_casos_df.sum(axis=0)
    dados_mortes_df.loc[len(dados_mortes_df)] = dados_mortes_df.sum(axis=0)

    casos_mundo = dados_casos_df.iloc[-1, 4:]
    mortes_mundo = dados_mortes_df.iloc[-1, 4:]

    casos_lista_mundo = []
    mortes_lista_mundo = []

    for i in range(len(casos_mundo)):
        casos_lista_mundo.clear()
        mortes_lista_mundo.clear()
        casos_lista_mundo.append(casos_mundo[i])
        mortes_lista_mundo.append(mortes_mundo[i])
    

    casos_atualizados_mundo = casos_lista_mundo[-1]
    mortes_atualizadas_mundo = mortes_lista_mundo[-1]

    #print(f"{len(casos_lista_mundo)}    {len(mortes_lista_mundo)}")

    context = {
        'paises': paises,
        'casos_lista_mundo': casos_lista_mundo,
        'mortes_lista_mundo': mortes_lista_mundo,
        'casos_atualizados_mundo': casos_atualizados_mundo,
        'mortes_atualizadas_mundo': mortes_atualizadas_mundo,
    }
    return render(request, 'index.html', context)


def sobrenos(request):
    context = {
        'paises': paises
    }
    return render(request, 'sobrenos.html', context)




def dados(request, nome):

    if(nome == "Mundo Inteiro"):
        dados_casos_df = pd.read_csv(url_dados_casos)
        dados_mortes_df = pd.read_csv(url_dados_mortes)
        dias = dados_casos_df.loc[dados_casos_df['Country/Region'] == nome].iloc[:, 4:]


        # Pegando dados do mundo:
        dados_casos_df.loc[len(dados_casos_df)] = dados_casos_df.sum(axis=0)
        dados_mortes_df.loc[len(dados_mortes_df)] = dados_mortes_df.sum(axis=0)

        casos_mundo = dados_casos_df.iloc[-1, 4:]
        mortes_mundo = dados_mortes_df.iloc[-1, 4:]

        casos_lista_mundo = []
        mortes_lista_mundo = []

        for i in range(len(casos_mundo)):
            casos_lista_mundo.append(casos_mundo[i])
            mortes_lista_mundo.append(mortes_mundo[i])
        
        #print(len(casos_lista_mundo))
        
        nome_portugues = "Mundo Inteiro"
        nome_ingles = "Earth"

        casos_atualizados_mundo = casos_lista_mundo[-1]
        mortes_atualizadas_mundo = mortes_lista_mundo[-1]

        context = {
            'paises': paises,
            'casos': casos_atualizados_mundo,
            'mortes': mortes_atualizadas_mundo,
            'nome_portugues': nome_portugues,
            'nome_ingles': nome_ingles,
            'url_bandeira': "bandeira_paises/mundo.png",
            'lista_dias': dias,
            'lista_mortes': mortes_lista_mundo,
            'lista_casos': casos_lista_mundo,
        }
    
    else:
        dados_casos_df = pd.read_csv(url_dados_casos)
        dados_mortes_df = pd.read_csv(url_dados_mortes)
        dias = dados_casos_df.loc[dados_casos_df['Country/Region'] == nome].iloc[:, 4:]

        dados_casos_pais = dados_casos_df.loc[dados_casos_df['Country/Region'] == nome]
        dados_mortes_pais = dados_mortes_df.loc[dados_mortes_df['Country/Region'] == nome]
        

        casos_ate_hoje = dados_casos_pais.iloc[:, -1].to_string().split()[1]  #Pegando o número de casos no país em questão até o dia atual
        mortes_ate_hoje = dados_mortes_pais.iloc[:, -1].to_string().split()[1]  #Pegando o número de mortes no país em questão até o dia atual

        mortes_dias = dados_mortes_df.loc[dados_mortes_df['Country/Region'] == nome].iloc[:, 4:].iloc[0, :]
        casos_dias = dias.iloc[0, :]

        for pais in paises:
            if pais.nome_ingles == nome:
                nome_portugues = pais.nome_portugues
                url_bandeira = pais.bandeira_url
                nome_ingles = pais.nome_ingles
                break


        context = {
            'paises': paises,
            'casos': casos_ate_hoje,
            'mortes': mortes_ate_hoje,
            'nome_portugues': nome_portugues,
            'nome_ingles': nome_ingles,
            'url_bandeira': url_bandeira,
            'lista_dias': dias,
            'lista_mortes': mortes_dias,
            'lista_casos': casos_dias,
        }
    
    return render(request, 'dados.html', context)


import matplotlib.pyplot as plt
import base64
from io import BytesIO

def pegar_grafico():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def pegar_plot(x, y, nomeX, nomeY, titulo):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title(titulo)
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel(nomeX)
    plt.ylabel(nomeY)
    plt.tight_layout()
    grafico = pegar_grafico()
    return grafico
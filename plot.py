from vacinação import perfis, path
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import matplotlib.units as munits
import sys
import os
import datetime

# converte datas no matplotlib para formato mais legível
converter = mdates.ConciseDateConverter(show_offset=False)
munits.registry[datetime.date] = converter

def plota(pessoas):
    for nome in pessoas:
        arquivo = os.path.join(path, nome + '.txt')
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
        y, x = zip(*[i.split() for i in linhas])
        y = [int(i) for i in y]
        x = [datetime.date.fromisoformat(i) for i in x]
        plt.plot_date(x, y, 'o:', xdate=True)
        
    plt.title('Tempo estimado para a vacinação')
    plt.xlabel('Data de acesso')
    plt.ylabel('Dias estimados até a vacinação')
    plt.legend(pessoas)
    plt.show()

if __name__ == "__main__":
    ajudamsg = 'Uso: plot.py pessoa1 pessoa2 ... \nou   plot.py -p [--perfis] (para ver perfis) \nou   plot.py -h [--help] (para ver esta ajuda)'
    pessoas = sys.argv[1:]
    nomes = [perfil['name'] for perfil in perfis]
    if pessoas == ['-h'] or pessoas == ['-help']:
        print(ajudamsg)
    elif pessoas == ['-p'] or pessoas == ['-perfis']:
        print('Os perfis em perfis.json são:')
        map(print, nomes)
    else: 
        for pessoa in pessoas:
            if pessoa not in nomes:
                raise Exception(f'Pessoa {pessoa} não é um dos perfis de perfis.json')
        plota(pessoas)
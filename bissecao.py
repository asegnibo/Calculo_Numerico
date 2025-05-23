import numpy as np

class Polinômio:
    def __init__(self,termos:tuple):
        '''Coloque os termos em ordem crescente, isto é, começa do termo de grau 0.'''
        self.termos = termos
        self.grau = len(termos) - 1
    def f(self,x:float):
        '''Retorna o valor do polinomio no ponto x'''
        fx = 0
        for i in reversed(range(self.grau+1)):
            xn = self.termos[i]*x**i
            fx += xn
        return float(fx)
    def derivada(self):
        '''Retorna um Polinomio novo, o qual é derivada deste.'''
        termos_novos = []
        for n in range(1,self.grau+1):
            termos_novos.append(n*self.termos[n])
        termos_tupla = tuple(termos_novos)
        return Polinômio(termos_tupla)
funcao = Polinômio((14,-6,7,-3,-7,3))
precisao = 10**-6
def bissecao(a:float,b:float,funcao,precisao:float,valor_exato:float,k=0,parada=False):
    assert funcao(a) * funcao(b) < 0 and a < b
    k+=1
    x = (a+b)/2
    e = abs(valor_exato-x)
    if funcao(x)==0 or abs(b-a) < precisao:
        parada = True
    return {'k':k,'a':a,'b':b,'x':x,'f(x)':funcao(x),'e':e,'parada':parada}

def write_top_bissecao(file):
    file.write(f'| k |'+' '*5+'a'+' '*5+'|'+' '*5+'b'+' '*5+'|'+' '*4+'x_k'+' '*4+'|'+' '*4+'f(x)'+' '*3+'|'+' '*4+'e_k'+' '*4+'|\n')
    file.write('¨'*64+'\n')
def write_data_bissecao(file,k,a,b,x,f_x,e):
    #arrendondar para 8 casas decimais
    a,b,x,f_x,e = round(a,8),round(b,8),round(x,8),round(f_x,8),round(e,8)
    file.write(f'|{k:03}|'+f'{a:.9f}|'+f'{b:.9f}|'+f'{x:.9f}|'+f'{f_x:+.8f}|'+f'{e:.9f}|\n')

def metodo_bissecao(a:float,b:float,funcao,precisao:float,valor_exato:float):
    k=0
    file = open('bissecao_saida.txt','w')
    write_top_bissecao(file)
    while True:
        data = bissecao(a,b,funcao,precisao,valor_exato,k)
        write_data_bissecao(file,data['k'],data['a'],data['b'],data['x'],data['f(x)'],data['e'])
        if data['parada']:
            break
        else:
            k+=1
            if funcao(data['a'])*funcao(data['x'])<0:
                b = data['x']
            else:
                a = data['x']
    file.close()

metodo_bissecao(1,2,funcao.f,precisao,np.sqrt(2))

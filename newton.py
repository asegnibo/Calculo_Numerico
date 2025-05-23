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
derivada = funcao.derivada()
precisao = 10**-6

def newton(x_k:float, funcao, derivada, precisao:float,valor_exato:float,k=0,parada=False):
    assert derivada(x_k)<1
    x = x_k - funcao(x_k)/derivada(x_k)
    if funcao(x) == 0 or abs(x-x_k) < precisao*max(1,x_k):
        parada = True
    return {'k':k,'x_k':x_k,'f(x_k)':funcao(x_k),"f'(x_k)":derivada(x_k),'e':abs(valor_exato-x_k),'parada':parada} if k==0 else {'k':k,'x_k':x,'f(x_k)':funcao(x),"f'(x_k)":derivada(x),'e':abs(valor_exato-x),'parada':parada}

def write_top_newton(file):
    file.write(f'| k |'+' '*4+'x_k'+' '*4+'|'+' '*3+'f(x_k)'+' '*2+'|'+' '*3+"f'(x_k)"+' '*2+'|'+' '*4+'e_k'+' '*4+'|\n')
    file.write('¨'*53+'\n')
def write_data_newton(file,k,x,fx,f_x,e):
    #arrendondar para 8 casas decimais
    x,fx,f_x,e = round(x,8),round(fx,8),round(f_x,8),round(e,8)
    file.write(f'|{k:03}|'+f'{x:.9f}|'+f'{fx:+.8f}|'+f'{f_x:+.8f}|'+f'{e:.9f}|\n')

def metodo_bissecao(x_k:float,funcao,derivada,precisao:float,valor_exato:float):
    k=0
    file = open('newton_saida.txt','w')
    write_top_newton(file)
    while True:
        data = newton(x_k,funcao,derivada,precisao,valor_exato,k)
        write_data_newton(file,data['k'],data['x_k'],data['f(x_k)'],data["f'(x_k)"],data['e'])
        if data['parada']:
            break
        else:
            k+=1
            x_k = data['x_k']
    file.close()
metodo_bissecao(1,funcao.f,derivada.f,precisao,np.sqrt(2))
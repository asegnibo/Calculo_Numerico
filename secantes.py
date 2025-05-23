
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

def secantes(x_1:float, x_0:float, funcao, precisao:float,valor_exato:float,k=0,parada=False):
    x = (x_0*funcao(x_1)-x_1*funcao(x_0))/(funcao(x_1)-funcao(x_0))
    if funcao(x) == 0 or abs(x-x_1) < precisao*max(1,x_1):
        parada = True
    return {'k':k,'x_1':x, 'x_0':x_1, 'f(x_1)':funcao(x),'e':abs(valor_exato-x),'parada':parada}

def write_top_secantes(file,x_0,x_1,funcao,valor_exato):
    file.write(f'| k |'+' '*4+'x_k'+' '*4+'|'+' '*3+'f(x_k)'+' '*2+'|'+' '*4+'e_k'+' '*4+'|\n')
    file.write('¨'*42+'\n')
    #Escrever as duas aproximações iniciais
    file.write(f'|000|'+f'{x_0:.9f}|'+f'{funcao(x_0):+.8f}|'+f'{abs(valor_exato-x_0):.9f}|\n')
    file.write(f'|001|'+f'{x_1:.9f}|'+f'{funcao(x_1):+.8f}|'+f'{abs(valor_exato-x_1):.9f}|\n')
def write_data_secantes(file,k,x,fx,e):
    #arrendondar para 8 casas decimais
    x,fx,e = round(x,8),round(fx,8),round(e,8)
    file.write(f'|{k:03}|'+f'{x:.9f}|'+f'{fx:+.8f}|'+f'{e:.9f}|\n')

def metodo_secantes(xs:tuple,funcao,precisao:float,valor_exato:float):
    k=2
    file = open('secantes_saida.txt','w')
    write_top_secantes(file,xs[0],xs[1],funcao,valor_exato)
    while True:
        data = secantes(xs[1],xs[0],funcao,precisao,valor_exato,k)
        write_data_secantes(file,data['k'],data['x_1'],data['f(x_1)'],data['e'])
        if data['parada']:
            break
        else:
            k+=1
            xs = (data['x_0'],data['x_1'])
        if k==100:
            break
    file.close()

metodo_secantes((1,2),funcao.f,precisao,np.sqrt(2))
'''
Aula da 4ªSemana/ago/2021
Olá mundo! crianças, feito em função (def)
'''
def ola():
    return "Olá mundo!"

#Como executar essa função 'ola()':
print("Função ola():",ola())

'''
Como seria uma função para resolver área triângulo?
area = (base x altura) / 2
Logo:
'''
def areaTriangulo(base,altura):
    area = (base * altura) / 2
    return area
#Como executar essa função 'areaTriangulo(base,altura)':
print("Função areaTriangulo(base,altura):",areaTriangulo(8,6))

'''
Como seria um função para resolver volume do cilindro?
volume = PI x raio^2 x altura
Logo:
'''
def volumeCilindro(raio,altura):
    volume = 3.14 * (raio**2) * altura
    return volume
#Como executar essa função 'volumeCilindro(raio,altura)':
print("Função volumeCilindro(raio,altura):",volumeCilindro(2,3))

'''
E uma função da função matemática f(x)= 2x+1?
'''
def f(x):
    #Fórmula geral: y = ax+b -> a=2 e b=1
    y = 2*x + 1 #Oxe, kkkkk
    return y
#Como executar essa função 'f(x)':
print("Função f(x): ",f(3))

'''
Função para sair do programinha...
'''
def sair():
    return exit(0)

print(sair())

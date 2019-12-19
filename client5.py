import Pyro4

classe = Pyro4.Proxy("PYRONAME:identificador")
idade = int(input("Informe a idade do nadador "))
print(classe.categoria(idade))

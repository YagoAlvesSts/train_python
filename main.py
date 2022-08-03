def func(*args, **kwargs):
    pessoa = kwargs.get('sobrenome')
    print(pessoa)
lista = [1,2,3,4,5,6]
func(*lista, nome="yago", sobrenome="Alves")
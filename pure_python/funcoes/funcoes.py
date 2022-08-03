

class Func:
        
    def _func(self, *args, **kwargs):
        """Just for view the uso of *args and **kwargs in a function"""
        name = kwargs.get('nome')
        last_name = kwargs.get('sobrenome')
        print(name, last_name)


    def run(self):
        lista = [1,2,3,4,5,6]
        self._func(*lista, nome="yago", sobrenome="Alves")
from itertools import zip_longest
from abc import abstractmethod

class List1:
    def __init__(self) -> None:
        self._cities = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo", "Caraíva", "Barreirinhas"]
        self._states = ['SP', 'MG', 'BA']
        
    def execute_zip(self) -> None:
        """Execute example with the function zip"""
        cities_states = zip(self._cities, self._states)
        print(list(cities_states))
        
    def execute_zip_longest(self) -> None:
        """Execute example with the function zip_longest"""
        cities_states = zip_longest(self._cities, self._states, fillvalue='Estado')
        print(list(cities_states))
    
    @abstractmethod
    def run(self) -> None:
        self.execute_zip()
        self.execute_zip_longest()
        
        
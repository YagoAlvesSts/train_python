from time import sleep
from threading import Lock, Thread

class Tickets: 
    """
    Class to apply the use of threads simulating a stock controller
    """
    
    def __init__(self, inventory) -> None:
        """initializing....
        
        :param inventory: number of tickets in stock
        """
        
        self.inventory = inventory
        self._lock = Lock()
        
    def buy(self, quantity) -> None:
        """
        Purchase a certain amount of tickets

        :param quantity: The quantity of tickets you want to buy
        :type quantity: int
        :return: None
        :rtype: None        
        """
        
        self._lock.acquire()
        
        if self.inventory < quantity:
            print("Não temos ingressos suficientes. ")
            self._lock.release()
            return
        
        sleep(1)
        
        self.inventory -= quantity
        print(f'Você comprou {quantity} ingresso (s). '
              f'Ainda temos {self.inventory} em estoque.')
        
        self._lock.release()      

def run():
    tickets = Tickets(10)

    threads = []  # Lista para manter as threads
    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i,))
        threads.append(t)

    # Inicia as threads
    for t in threads:
        t.start()

    # Verifica se todas as threads terminaram
    exec = True
    while exec:
        exec = False

        for t in threads:
            if t.is_alive():
                exec = True
                break

    print(tickets.inventory)  
    
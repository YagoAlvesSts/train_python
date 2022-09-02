from methods.magic_methods import A as magic_methods
from methods.overload_methods import run


def run_magic() -> None:
    mm = magic_methods()
    mm('luiz otávio')
    
    
def run_overload() -> None:
    run()
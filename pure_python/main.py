from argparse import ArgumentError
from funcoes.run import run_func
from dictionary.run import run_quiz
from list.run import run_list
from methods.run import run_magic, run_overload


if __name__ == '__main__':
    try:
        #run_func()
        #run_quiz()
        #run_list()
        run_magic()
        #run_overload()
        
    except TypeError as e:
        raise e
import json
from abc import abstractmethod

class Quiz:
    """Class representing a Quiz object"""
    
    def __init__(self) -> None:
        self._right_answers = 0
        self._questions = json.loads(open("./pure_python/dictionary/questions.json").read())
        
    def _print_question(self,pk, pv:dict) -> None:
        print(f'{pk}:{pv["pergunta"]}')
    
    def _print_answer(self,rk, rv) -> None:
        print(f'[{rk}]: {rv}')
        
    def questions(self) -> None:
        for pk, pv in self._questions.items():
            self._print_question(pk,pv)
            
            
            print('Respostas: \n')
            
            for rk, rv in pv['respostas'].items():
                self._print_answer(rk, rv)
                
            answer_user = input('Sua resposta: \n')
            
            if answer_user == pv['resposta_certa']:
                print('EEEEHHHHHHHHHH Você acertou!!!')
                self._right_answers += 1
            else:
                print("EEEEERRRRRRRRROOOOOOOU!!!")
                
            print()
            
        self.qtd_questions = len(self._questions)
        self.percent_rights = self._right_answers / self.qtd_questions * 100
        
        print(f"Você acertou {self._right_answers} respostas.")
        print(f"sua porcentagem de acerto foi de {self.percent_rights}.")
        
    @abstractmethod
    def run(self):
        self.questions()
        
        
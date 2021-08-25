class Agenda:

    def __init__(self,nomecontato, tarefas):
        self.__nomecontato= nomecontato
        self.__tarefas= tarefas

    def get_nomecontato(self,):
        return self.__nomecontato
    def get_tarefas(self):
        return self.__tarefas

    def set_nomecontato(self, nomecontato):
        self.__nomecontato: nomecontato
    def set_tarefas(self, tarefas):
        self.__tarefas: tarefas

    

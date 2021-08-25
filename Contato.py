class Contato:

    def __init__(self, nomecontato, telefonecontato, idadecontato):
        self.__nomecontato = nomecontato
        self.__telefonecontato = telefonecontato
        self.__idadecontato = idadecontato

    def get_nome(self):
        return self.__nomecontato
    def get_telefone(self):
        return self.__telefonecontato
    def get_idade(self):
        return self.__idadecontato

    def set_nome(self, nomecontato):
        self.__nomecontato = nomecontato

    def set_telefone(self, telefonecontato):
        self.__telefonecontato = telefonecontato

    def set_idade(self, idadeconato):
        self.__idadecontato = idadeconato

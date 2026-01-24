from abc import ABC, abstractmethod

class DAO(ABC):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for objeto in cls.objetos:
            if objeto.get_id() > id: 
                id = objeto.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
        cls.salvar()
    @classmethod
    @abstractmethod
    def salvar(cls):
        pass
    @classmethod
    @abstractmethod
    def abrir(cls):
        pass  
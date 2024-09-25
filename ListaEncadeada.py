class ItemLista:
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.next = nextItem

    def __repr__(self):
        return '%s => %s' % (self.data, self.next)


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "%s" % (self.head)

    def insere(self, data):
        # Cria um objeto para armazenar um novo item da lista
        item = ItemLista(data)
        # O head é apontado como próximo item
        item.next = self.head
        # O item atual se torna o head
        self.head = item

    def remove(self, valor):
        # Verifica se o item a ser removido é o head
        if self.head and self.head.data == valor:
            self.head = self.head.next
        else:
            # Detecta a posição do elemento
            before = None
            navegar = self.head
            # Navega pela lista para encontrar o elemento
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.next

            # Remove o item se ele for encontrado
            if navegar:
                before.next = navegar.next

    def busca(self, valor):
        navegar = self.head
        while navegar and navegar.data != valor:
            navegar = navegar.next
        return navegar


# Exemplo de uso do código
lista = ListaEncadeada()
lista.insere(1)
lista.insere(2)
lista.insere(3)

print("Lista após inserções:", lista)

lista.remove(2)
print("Lista após remover o valor 2:", lista)

item_encontrado = lista.busca(3)
if item_encontrado:
    print("Item encontrado:", item_encontrado)
else:
    print("Item não encontrado.")


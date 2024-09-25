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


# Criação do objeto ListaEncadeada
lista = ListaEncadeada()

print("Conteúdo da lista:", lista)  # Lista está vazia

# Agora, vamos proceder com a adição de alguns itens na lista:
lista.insere("shampoo")
lista.insere("biscoito")
lista.insere("detergente")
lista.insere("abobrinha")
lista.insere("banana")

print("Lista após inserções:", lista)

# Removendo o item 'abobrinha'
lista.remove("abobrinha")

print("Lista após remover 'abobrinha':", lista)

print(" ")

# Realizando a busca de um item
query = "biscoito"
item_buscado = lista.busca(query)

if item_buscado:
    print(f"Elemento '{query}' encontrado")
else:
    print(f"Elemento '{query}' não encontrado")

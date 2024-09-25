class Consulta:
    def __init__(self, data, diagnostico, tratamento):
        self.data = data
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.next = None  # Próxima consulta

    def __repr__(self):
        return f"Consulta em {self.data} - Diagnóstico: {self.diagnostico}, Tratamento: {self.tratamento}"

class HistoricoMedico:
    def __init__(self):
        self.head = None  # O primeiro registro de consulta

    def __repr__(self):
        consultas = []
        atual = self.head
        while atual:
            consultas.append(repr(atual))
            atual = atual.next
        return "\n".join(consultas) if consultas else "Nenhum histórico médico disponível."

    def adicionar_consulta(self, data, diagnostico, tratamento):
        nova_consulta = Consulta(data, diagnostico, tratamento)
        nova_consulta.next = self.head  # A nova consulta é inserida no início da lista
        self.head = nova_consulta

    def buscar_consulta(self, data):
        atual = self.head
        while atual:
            if atual.data == data:
                return atual
            atual = atual.next
        return None

    def remover_consulta(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next  # Remove o head
        else:
            anterior = None
            atual = self.head
            while atual and atual.data != data:
                anterior = atual
                atual = atual.next
            if atual:  # Consulta encontrada
                anterior.next = atual.next

class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = HistoricoMedico()

    def __repr__(self):
        return f"Paciente: {self.nome}, Idade: {self.idade}\nHistórico:\n{self.historico}"

# Criação de pacientes
paciente1 = Paciente("João Silva", 45)
paciente2 = Paciente("Maria Souza", 37)

# Adicionando consultas ao histórico de João
paciente1.historico.adicionar_consulta("2024-01-10", "Gripe", "Repouso e hidratação")
paciente1.historico.adicionar_consulta("2024-03-15", "Dor nas costas", "Fisioterapia")

# Adicionando consultas ao histórico de Maria
paciente2.historico.adicionar_consulta("2024-02-05", "Dor de cabeça", "Analgésico")
paciente2.historico.adicionar_consulta("2024-04-20", "Alergia", "Antialérgico")

# Exibindo os históricos dos pacientes
print(paciente1)
print("\n")
print(paciente2)

# Buscando uma consulta no histórico de João
consulta = paciente1.historico.buscar_consulta("2024-01-10")
if consulta:
    print("\nConsulta encontrada:", consulta)
else:
    print("\nConsulta não encontrada.")

# Removendo uma consulta do histórico de João
paciente1.historico.remover_consulta("2024-01-10")
print("\nHistórico de João após remover a consulta de 2024-01-10:")
print(paciente1)

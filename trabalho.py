import csv

def carregar_dados(filmes_csv):
    try:
        with open(filmes_csv, mode='r', newline='') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            return list(leitor_csv)

    except FileNotFoundError:
        return []

#salvar arquivos
def salvar_dados(filmes_csv, dados):
    with open(filmes_csv, mode='w', newline='') as arquivo:
        campos = ['ID', 'Título', 'Diretor', 'Ano']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=campos)

        escritor_csv.writeheader()
        escritor_csv.writerows(dados)

        #menu
        def exibir_menu():
            print("\nMenu de Operações:")
            print("\1 Cadastrar filmes")
            print("\2 Listar filmes") 
            print("\3 Buscar filmes")
            print("\4 remover filmes")
            print("\5 sair")

            #cadastro de um novo filme
            






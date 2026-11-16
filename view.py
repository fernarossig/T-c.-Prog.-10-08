
class SuspeitoView:

    def exibir_menu(self):
        print("\n--- DATA VAULT PRO (MVC) ---")
        print("1. Cadastrar Suspeito")
        print("2. Listar Todos")
        print("3. Remover Suspeito por ID")
        print("4. Filtrar por Periculosidade")
        print("0. Sair")

        return input("Escolha uma opção: ")

    def obter_dados_suspeito(self):
        nome = input("Nome do suspeito: ")
        crime = input("Crime: ")
        periculosidade = input("Nível de perigo (1-10): ")

        return nome, crime, periculosidade

    def obter_id_remocao(self):
        return input("ID do suspeito a remover: ")

    def obter_periculosidade_minima(self):
        return input("Periculosidade mínima (1-10): ")

    def mostrar_lista(self, suspeitos):
        print("\n--- FICHA CRIMINAL ---")

        if not suspeitos:
            print("Nenhum registro encontrado.")
            return

        for s in suspeitos:
            print(
                f"ID: {s[0]} | Suspeito: {s[1]} | "
                f"Crime: {s[2]} | Perigo: {s[3]}/10"
            )

    def mostrar_mensagem(self, msg):
        print(f"\nSistema: {msg}")

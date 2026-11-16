
import sqlite3

BANCO = "vault_original.db"

# Conexão e criação do banco
def conectar_banco():
    conexao = sqlite3.connect(BANCO)
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS suspeitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crime TEXT NOT NULL,
            periculosidade TEXT NOT NULL
        )
    """)
    conexao.commit()
    return conexao


# Cadastro de suspeitos
def cadastrar_suspeito(conexao):
    nome = input("Nome do suspeito: ").strip()
    crime = input("Crime cometido: ").strip()

    if not nome or not crime:
        print("Erro: nome e crime são obrigatórios.")
        return

    print("\nNível de periculosidade:")
    print("1 - Baixo")
    print("2 - Médio")
    print("3 - Alto")

    nivel = input("Escolha: ").strip()

    niveis = {"1": "Baixo", "2": "Médio", "3": "Alto"}

    if nivel not in niveis:
        print("Nível de periculosidade inválido.")
        return

    try:
        conexao.execute(
            "INSERT INTO suspeitos (nome, crime, periculosidade) VALUES (?, ?, ?)",
            (nome, crime, niveis[nivel])
        )
        conexao.commit()
        print("Suspeito cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar: {erro}")


# Consulta de registros
def consultar_suspeitos(conexao):
    try:
        registros = conexao.execute(
            "SELECT * FROM suspeitos ORDER BY id"
        ).fetchall()

        if not registros:
            print("\nNenhum suspeito cadastrado.")
            return

        print("\n--- LISTA DE SUSPEITOS ---")

        for registro in registros:
            print(f"\nID: {registro[0]}")
            print(f"Nome: {registro[1]}")
            print(f"Crime: {registro[2]}")
            print(f"Periculosidade: {registro[3]}")

    except sqlite3.Error as erro:
        print(f"Erro na consulta: {erro}")


# Menu principal
def menu():
    try:
        conexao = conectar_banco()

        while True:
            print("\n===== SISTEMA DE SUSPEITOS =====")
            print("1 - Cadastrar suspeito")
            print("2 - Consultar suspeitos")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_suspeito(conexao)

            elif opcao == "2":
                consultar_suspeitos(conexao)

            elif opcao == "3":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")

    finally:
        if "conexao" in locals():
            conexao.close()


if __name__ == "__main__":
    menu()

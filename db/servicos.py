from db.connection import conectar

def cadastrar_servico(nome, valor):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO servicos (nome, valor) VALUES (?, ?)",
            (nome, valor)
        )
        conexao.commit()
    except Exception as e:
        raise e
    finally:
        conexao.close()

def listar_servicos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, valor FROM servicos")
    servicos = cursor.fetchall()
    conexao.close()
    return servicos

def deletar_servico(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM servicos WHERE nome = ?", (nome,))
    conexao.commit()
    conexao.close()

def atualizar_valor_servico(servico_id, novo_valor):
    """
    Atualiza o valor de um serviço existente.
    :param servico_id: ID do serviço a ser atualizado.
    :param novo_valor: Novo valor do serviço.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE servicos SET valor = ? WHERE id = ?",
        (novo_valor, servico_id)
    )
    conexao.commit()
    conexao.close()
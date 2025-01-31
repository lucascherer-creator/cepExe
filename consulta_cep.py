import sys
import requests
import os

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            return dados
    return None

def formatar_dado(dado, tamanho):
    """Converte para uppercase e ajusta o tamanho com espaços"""
    return str(dado).upper().ljust(tamanho)[:tamanho]

def salvar_em_txt(dados_cep, arquivo_saida):
    # Obtém o diretório onde o executável está
    diretório_atual = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Caminho completo para o arquivo na mesma pasta do executável
    caminho_arquivo = os.path.join(diretório_atual, arquivo_saida)
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        cep = formatar_dado(dados_cep['cep'], 10)
        logradouro = formatar_dado(dados_cep['logradouro'], 40)
        complemento = formatar_dado(dados_cep['complemento'], 30)
        bairro = formatar_dado(dados_cep['bairro'], 20)
        cidade = formatar_dado(dados_cep['localidade'], 30)
        estado = formatar_dado(dados_cep['uf'], 2)

        # Escreve os dados formatados em uma única linha
        arquivo.write(f"{cep}{logradouro}{complemento}{bairro}{cidade}{estado}\n")

def main():
    cep = input("Digite o CEP: ")  # Solicita o CEP ao usuário

    dados_cep = buscar_cep(cep)
    
    if dados_cep:
        arquivo_saida = f"cep_{cep}.txt"
        salvar_em_txt(dados_cep, arquivo_saida)
        print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")
    else:
        print("CEP não encontrado ou inválido.")

    input("Pressione Enter para sair...")  # Mantém a janela aberta até o usuário sair


if __name__ == "__main__":
    main()

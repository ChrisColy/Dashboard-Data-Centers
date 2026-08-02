"""
SISTEMA DE ESTOQUE - VERSÃO AVANÇADA
=====================================
Melhorias em relação à versão simples:
- Orientação a objetos (classe Estoque)
- Persistência dos dados em arquivo JSON (não perde os dados ao fechar)
- Validação de entradas (evita erros ao digitar letras onde precisa de número)
- Atualização de quantidade de produtos já existentes (soma/subtrai, não apenas sobrescreve)
- Busca de produtos
- Relatório com valor total do estoque (preço unitário x quantidade)
- Estoque baixo (alerta de produtos com poucas unidades)
- Código organizado em funções, mais fácil de manter
"""

import json
import os
from datetime import datetime

ARQUIVO_ESTOQUE = "estoque.json"
LIMITE_ESTOQUE_BAIXO = 5


class Estoque:
    """Classe responsável por gerenciar os produtos e suas operações."""

    def __init__(self, arquivo=ARQUIVO_ESTOQUE):
        self.arquivo = arquivo
        self.produtos = {}
        self.carregar()

    # ---------- Persistência ----------
    def carregar(self):
        """Carrega os dados do arquivo JSON, se existir."""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, "r", encoding="utf-8") as f:
                    self.produtos = json.load(f)
            except (json.JSONDecodeError, IOError):
                print("⚠️  Não foi possível ler o arquivo de estoque. Iniciando um estoque novo.")
                self.produtos = {}

    def salvar(self):
        """Salva os dados atuais no arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.produtos, f, ensure_ascii=False, indent=4)

    # ---------- Operações principais ----------
    def adicionar_produto(self, nome, quantidade, preco):
        nome = nome.strip().title()

        if nome in self.produtos:
            # Se já existe, soma a quantidade em vez de sobrescrever
            self.produtos[nome]["quantidade"] += quantidade
            print(f"'{nome}' já existia. Quantidade atualizada para {self.produtos[nome]['quantidade']}.")
        else:
            self.produtos[nome] = {
                "quantidade": quantidade,
                "preco": preco,
                "criado_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
            }
            print(f"Produto '{nome}' adicionado com sucesso!")

        self.salvar()

    def remover_produto(self, nome):
        nome = nome.strip().title()
        if nome in self.produtos:
            del self.produtos[nome]
            self.salvar()
            print(f"Produto '{nome}' removido!")
        else:
            print("Produto não encontrado!")

    def atualizar_quantidade(self, nome, delta):
        """Aumenta (delta positivo) ou diminui (delta negativo) a quantidade."""
        nome = nome.strip().title()
        if nome not in self.produtos:
            print("Produto não encontrado!")
            return

        nova_quantidade = self.produtos[nome]["quantidade"] + delta
        if nova_quantidade < 0:
            print("Operação inválida: isso deixaria a quantidade negativa.")
            return

        self.produtos[nome]["quantidade"] = nova_quantidade
        self.salvar()
        print(f"Quantidade de '{nome}' atualizada para {nova_quantidade}.")

    def buscar_produto(self, termo):
        termo = termo.strip().lower()
        encontrados = {
            nome: dados for nome, dados in self.produtos.items()
            if termo in nome.lower()
        }
        return encontrados

    def valor_total(self):
        return sum(d["quantidade"] * d["preco"] for d in self.produtos.values())

    def produtos_estoque_baixo(self):
        return {
            nome: dados for nome, dados in self.produtos.items()
            if dados["quantidade"] <= LIMITE_ESTOQUE_BAIXO
        }

    # ---------- Exibição ----------
    def listar(self, produtos=None):
        produtos = produtos if produtos is not None else self.produtos

        if not produtos:
            print("Nenhum produto encontrado.")
            return

        print(f"\n{'PRODUTO':<20}{'QTD':<10}{'PREÇO UNIT.':<15}{'SUBTOTAL':<12}")
        print("-" * 57)
        for nome, dados in produtos.items():
            subtotal = dados["quantidade"] * dados["preco"]
            print(f"{nome:<20}{dados['quantidade']:<10}R$ {dados['preco']:<12.2f}R$ {subtotal:<10.2f}")
        print("-" * 57)


# ---------- Funções auxiliares de entrada (validação) ----------
def ler_inteiro(mensagem, permitir_negativo=False):
    """Garante que o usuário digite um número inteiro válido."""
    while True:
        valor = input(mensagem).strip()
        try:
            numero = int(valor)
            if not permitir_negativo and numero < 0:
                print("Digite um número que não seja negativo.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def ler_float(mensagem):
    """Garante que o usuário digite um número decimal válido (aceita vírgula ou ponto)."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero < 0:
                print("O valor não pode ser negativo.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida! Digite um valor numérico (ex: 10.50).")


def ler_texto_nao_vazio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Esse campo não pode ficar vazio.")


# ---------- Menu / Interface ----------
def exibir_menu():
    print("\n" + "=" * 35)
    print("      SISTEMA DE ESTOQUE PRO")
    print("=" * 35)
    print("1 - Adicionar produto")
    print("2 - Ver estoque completo")
    print("3 - Remover produto")
    print("4 - Entrada/saída de quantidade")
    print("5 - Buscar produto")
    print("6 - Relatório (valor total e estoque baixo)")
    print("7 - Sair")
    print("=" * 35)


def main():
    estoque = Estoque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_texto_nao_vazio("Nome do produto: ")
            quantidade = ler_inteiro("Quantidade: ")
            preco = ler_float("Preço unitário (R$): ")
            estoque.adicionar_produto(nome, quantidade, preco)

        elif opcao == "2":
            estoque.listar()

        elif opcao == "3":
            nome = ler_texto_nao_vazio("Digite o produto para remover: ")
            estoque.remover_produto(nome)

        elif opcao == "4":
            nome = ler_texto_nao_vazio("Nome do produto: ")
            print("1 - Entrada (aumentar)   2 - Saída (diminuir)")
            tipo = input("Escolha: ").strip()
            qtd = ler_inteiro("Quantidade: ")

            if tipo == "1":
                estoque.atualizar_quantidade(nome, qtd)
            elif tipo == "2":
                estoque.atualizar_quantidade(nome, -qtd)
            else:
                print("Opção inválida!")

        elif opcao == "5":
            termo = ler_texto_nao_vazio("Digite o nome (ou parte) do produto: ")
            resultado = estoque.buscar_produto(termo)
            estoque.listar(resultado)

        elif opcao == "6":
            print(f"\n💰 Valor total do estoque: R$ {estoque.valor_total():.2f}")
            baixos = estoque.produtos_estoque_baixo()
            if baixos:
                print(f"\n⚠️  Produtos com estoque baixo (≤ {LIMITE_ESTOQUE_BAIXO} unidades):")
                estoque.listar(baixos)
            else:
                print("\n✅ Nenhum produto com estoque baixo.")

        elif opcao == "7":
            print("Sistema encerrado. Até logo!")
            break

        else:
            print("Opção inválida! Escolha um número entre 1 e 7.")


if __name__ == "__main__":
    main()
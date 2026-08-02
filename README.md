📊 Dashboard - Crescimento de Data Centers

Um dashboard visual em desktop, feito com Python e Tkinter, que exibe uma imagem ilustrativa e um gráfico da evolução do número de data centers ao longo dos anos.

✨ Funcionalidades
Interface gráfica construída com Tkinter
Exibição de imagem ilustrativa do tema (data center)
Gráfico integrado (Matplotlib embutido na janela) mostrando o crescimento ano a ano
Indicador de status com destaque visual sobre a tendência do setor
🖥️ Como executar
1. Instale as dependências
bash
pip install pillow matplotlib

tkinter já vem incluso na instalação padrão do Python na maioria dos sistemas. No Linux, caso não esteja disponível, instale com sudo apt install python3-tk.

2. Adicione a imagem

Coloque uma imagem chamada datacenter.jpg na mesma pasta do arquivo dashboard.py.

3. Execute
bash
python dashboard.py
📈 Dados do gráfico

Os dados exibidos atualmente são fixos no código:

python
anos = [2021, 2022, 2023, 2024, 2025]
crescimento = [10, 18, 30, 45, 70]

Para usar dados reais, basta substituir essas duas listas por valores vindos de uma planilha, API ou banco de dados.

🎨 Visual
Tema escuro (
#1e1e1e) com destaque em verde (
#00ff88) para o status
Janela com tamanho fixo de 900x600
🚀 Possíveis melhorias futuras
 Carregar dados de um arquivo CSV/Excel em vez de valores fixos
 Atualização automática/periódica do gráfico
 Tratamento de erro caso datacenter.jpg não seja encontrada
 Migrar para uma versão web (ex: Streamlit ou Dash) para acesso remoto
📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.

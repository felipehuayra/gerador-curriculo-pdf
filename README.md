# Gerador de Currículo em PDF

Script Python que gera currículos profissionais em PDF de forma automatizada, utilizando a biblioteca [fpdf2](https://py-fpdf2.readthedocs.io/).

## O que o projeto faz

- Gera um arquivo PDF formatado a partir de dados preenchidos no próprio script
- Aplica layout com cabeçalho colorido, seções organizadas e tipografia limpa
- Permite atualizar o currículo editando apenas o bloco de dados, sem mexer na lógica de geração

## Tecnologias utilizadas

- Python 3
- fpdf2

## Como usar

**1. Instale a dependência:**

pip install fpdf2


**2. Edite seus dados no arquivo `gerar_curriculo.py`:**

Preencha o bloco `dados = {...}` no início do arquivo com suas informações — nome, contato, formação, habilidades e objetivo.

**3. Execute o script:**

```bash
python gerar_curriculo.py
```

O arquivo `curriculo.pdf` será gerado.

## Observação sobre fontes
O script usa as fontes do sistema. No Windows, as linhas de fonte já estão configuradas para Arial:

python
FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD    = "C:/Windows/Fonts/arialbd.ttf"
FONT_ITALIC  = "C:/Windows/Fonts/ariali.ttf"

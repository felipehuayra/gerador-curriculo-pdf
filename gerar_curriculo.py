from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Fontes
FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD    = "C:/Windows/Fonts/arialbd.ttf"
FONT_ITALIC  = "C:/Windows/Fonts/ariali.ttf"

#  Dados
dados = {
    "nome": "Seu Nome",
    "titulo": "Seu Título",
    "contato": "Sua Cidade | Seu Telefone | Seu Email",
    "linkedin": "linkedin.com/in/seu-perfil",
    "github": "github.com/seu-usuario",

    "sobre": "Escreva aqui seu resumo profissional.",

    "formacao": [
        {
            "curso": "Nome do Curso",
            "instituicao": "Nome da Instituição",
            "periodo": "Previsão de conclusão: XXXX",
        }
    ],

    "habilidades": {
        "Linguagens e Tecnologias": [
            "Habilidade 1",
            "Habilidade 2",
        ],
    },

    "diferenciais": [
        "Diferencial 1",
        "Diferencial 2",
    ],

    "objetivo": "Escreva aqui seu objetivo profissional.",
}

class GeradorCurriculo(FPDF):

    COR_PRIMARIA = (31, 73, 125)
    COR_TEXTO    = (30, 30, 30)
    COR_SUBTEXTO = (100, 100, 100)
    COR_LINHA    = (190, 210, 230)

    def setup_fonts(self):
        self.add_font("Sans",        "", FONT_REGULAR)
        self.add_font("Sans", "B",      FONT_BOLD)
        self.add_font("Sans", "I",      FONT_ITALIC)

    def _cell(self, w, h, txt, style="", size=10, ln=True):
        self.set_font("Sans", style, size)
        nx = XPos.LMARGIN if ln else XPos.RIGHT
        self.set_x(15)
        self.cell(w, h, txt, new_x=nx, new_y=YPos.NEXT if ln else YPos.TOP)

    def cabecalho_pagina(self, d):
        self.set_fill_color(*self.COR_PRIMARIA)
        self.rect(0, 0, 210, 40, "F")

        self.set_text_color(255, 255, 255)
        self.set_font("Sans", "B", 18)
        self.set_xy(15, 7)
        self.cell(0, 9, d["nome"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("Sans", "", 10)
        self.set_x(15)
        self.cell(0, 6, d["titulo"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font("Sans", "", 9)
        self.set_x(15)
        self.cell(0, 5, d["contato"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_x(15)
        self.cell(0, 5, f"{d['linkedin']}   |   {d['github']}",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_text_color(*self.COR_TEXTO)
        self.set_y(46)

    def titulo_secao(self, texto):
        self.ln(4)
        self.set_font("Sans", "B", 11)
        self.set_text_color(*self.COR_PRIMARIA)
        self.set_x(15)
        self.cell(0, 7, texto.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_draw_color(*self.COR_LINHA)
        self.set_line_width(0.4)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(3)
        self.set_text_color(*self.COR_TEXTO)

    def paragrafo(self, texto, size=10):
        self.set_font("Sans", "", size)
        self.set_x(15)
        self.multi_cell(180, 5.5, texto)

    def item_lista(self, texto, size=10):
        self.set_font("Sans", "", size)
        self.set_x(15)
        self.cell(6, 5.5, "•", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_x(22)
        self.multi_cell(173, 5.5, texto)

#  Gerar PDF
def gerar(dados, arquivo_saida="curriculo_felipe.pdf"):
    pdf = GeradorCurriculo()
    pdf.set_margins(15, 15, 15)
    pdf.setup_fonts()
    pdf.add_page()

    pdf.cabecalho_pagina(dados)

    # Sobre mim
    pdf.titulo_secao("Sobre mim")
    pdf.paragrafo(dados["sobre"])

    # Formação
    pdf.titulo_secao("Formação Acadêmica")
    for f in dados["formacao"]:
        pdf.set_font("Sans", "B", 10)
        pdf.set_x(15)
        pdf.cell(0, 6, f["curso"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.set_font("Sans", "", 10)
        pdf.set_x(15)
        pdf.cell(0, 5, f["instituicao"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.set_font("Sans", "I", 9)
        pdf.set_text_color(*pdf.COR_SUBTEXTO)
        pdf.set_x(15)
        pdf.cell(0, 5, f["periodo"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(*pdf.COR_TEXTO)
        pdf.ln(2)

    # Habilidades
    pdf.titulo_secao("Habilidades Técnicas")
    for categoria, itens in dados["habilidades"].items():
        pdf.set_font("Sans", "B", 10)
        pdf.set_x(15)
        pdf.cell(0, 6, categoria, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        for item in itens:
            pdf.item_lista(item)
        pdf.ln(2)

    # Diferenciais
    pdf.titulo_secao("Diferenciais & Perfil")
    for d in dados["diferenciais"]:
        pdf.item_lista(d)

    # Objetivo
    pdf.titulo_secao("Objetivo Profissional")
    pdf.paragrafo(dados["objetivo"])

    pdf.output(arquivo_saida)
    print(f"✓ Currículo gerado: {arquivo_saida}")


if __name__ == "__main__":
    gerar(dados)
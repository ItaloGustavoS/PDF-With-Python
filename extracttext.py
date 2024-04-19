from PyPDF2 import PdfReader

# Abrir o arquivo PDF de entrada para leitura
reader = PdfReader("exemplo.pdf")

# Extrair a primeira página do PDF
page = reader.pages[0]

# Extrair e imprimir o texto da página
print(page.extract_text())

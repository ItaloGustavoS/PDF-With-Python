from PyPDF2 import PdfReader, PdfWriter

# Abrir o arquivo PDF grande para leitura
reader = PdfReader("grande-e-antigo-arquivo.pdf")

# Criar um escritor de PDF
writer = PdfWriter()

# Iterar sobre todas as páginas do arquivo PDF grande
for page in reader.pages:
    # Adicionar cada página ao escritor de PDF
    writer.add_page(page)

# Adicionar metadados do arquivo PDF grande ao novo arquivo
writer.add_metadata(reader.metadata)

# Abrir o novo arquivo PDF menor para escrita binária
with open("novo-arquivo-menor.pdf", "wb") as fp:
    # Escrever o conteúdo do escritor PDF no novo arquivo
    writer.write(fp)

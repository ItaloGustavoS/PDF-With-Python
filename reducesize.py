from PyPDF2 import PdfReader, PdfWriter

# Abrir o arquivo PDF de entrada para leitura
reader = PdfReader("exemplo.pdf")

# Criar um escritor de PDF para escrever páginas comprimidas
writer = PdfWriter()

# Iterar sobre todas as páginas do leitor PDF
for page in reader.pages:
    # Comprimir o conteúdo da página (isso pode ser intensivo em CPU)
    page.compress_content_streams()

    # Adicionar a página comprimida ao escritor PDF
    writer.add_page(page)

# Abrir o arquivo de saída PDF para escrita binária
with open("saida.pdf", "wb") as f:
    # Escrever o conteúdo do escritor PDF no arquivo de saída
    writer.write(f)

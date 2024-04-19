from PyPDF2 import PdfReader

# Abrir o arquivo PDF de entrada para leitura
reader = PdfReader("exemplo.pdf")

# Extrair a primeira página do PDF
page = reader.pages[0]

# Inicializar a contagem de imagens extraídas
count = 0

# Iterar sobre todas as imagens da página
for image_file_object in page.images:
    # Abrir um arquivo para escrita binária com um nome único baseado na contagem
    with open(str(count) + image_file_object.name, "wb") as fp:
        # Escrever os dados da imagem no arquivo
        fp.write(image_file_object.data)

        # Incrementar a contagem para o próximo nome de arquivo único
        count += 1

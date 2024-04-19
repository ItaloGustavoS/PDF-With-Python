from PyPDF2 import PdfWriter

# Criar um objeto 'merger' para mesclar PDFs
merger = PdfWriter()

# Iterar sobre cada arquivo PDF na lista e mesclar ao objeto 'merger'
for pdf in ["arquivo1.pdf", "arquivo2.pdf", "arquivo3.pdf"]:
    merger.append(pdf)

# Escrever o PDF mesclado em um novo arquivo
merger.write("pdf-mesclado.pdf")

# Fechar o objeto 'merger' após a conclusão da mesclagem
merger.close()

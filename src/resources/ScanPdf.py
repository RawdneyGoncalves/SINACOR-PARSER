import PyPDF2

file_path = r"D:\Workspace\in progress\parser-sinacor\src\resources\1.pdf"

def extrair_texto_pdf(arquivo_pdf):
    try:
        with open(arquivo_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            texto = ''
            
            # Itere pelas páginas do PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                texto += page.extract_text()
            
            return texto
    except Exception as e:
        return str(e)

arquivo_pdf = file_path
texto_extraido = extrair_texto_pdf(arquivo_pdf)

if texto_extraido:
    print(texto_extraido.rfind())
else:
    print("Não foi possível extrair o texto do PDF.")

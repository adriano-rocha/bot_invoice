from pdf2image import convert_from_path
import pytesseract
import os

def processar_pdf(pdf_path):
    """
    Converte PDF em imagens e extrai texto com OCR
    """
    print(f"\n📄 Processando: {pdf_path}")
    
    # 1. Converter PDF → Imagens
    print("   🔄 Convertendo PDF para imagens...")
    imagens = convert_from_path(pdf_path, poppler_path=r"C:\poppler\Library\bin")
    
    print(f"   ✅ {len(imagens)} página(s) convertida(s)")
    
    # 2. Extrair texto de cada página
    texto_completo = ""
    
    for i, imagem in enumerate(imagens, 1):
        print(f"   🔍 Extraindo texto da página {i}...")
        
        # Salvar imagem temporária (para debug)
        temp_img = f"temp/page_{i}.png"
        imagem.save(temp_img)
        
        # OCR
        texto = pytesseract.image_to_string(imagem, lang='eng')
        texto_completo += f"\n--- PÁGINA {i} ---\n{texto}\n"
    
    return texto_completo


# TESTE
if __name__ == "__main__":
    print("=" * 60)
    print("🤖 INVOICE BOT - PROCESSADOR DE NOTAS FISCAIS")
    print("=" * 60)
    
    # Verificar se existe PDF para testar
    pdfs = [f for f in os.listdir('pdfs') if f.endswith('.pdf')]
    
    if not pdfs:
        print("\n⚠️  Nenhum PDF encontrado na pasta 'pdfs/'")
        print("📌 Coloque um PDF de nota fiscal na pasta 'pdfs/' e rode novamente")
    else:
        # Processar primeiro PDF
        pdf_path = f"pdfs/{pdfs[0]}"
        texto = processar_pdf(pdf_path)
        
        # Mostrar resultado
        print("\n" + "=" * 60)
        print("📋 TEXTO EXTRAÍDO:")
        print("=" * 60)
        print(texto)
        
        # Salvar em arquivo
        output_file = "output/texto_extraido.txt"
        os.makedirs('output', exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(texto)
        
        print(f"\n💾 Texto salvo em: {output_file}")
        print("=" * 60)
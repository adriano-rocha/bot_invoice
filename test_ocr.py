import pytesseract
from PIL import Image, ImageDraw
import os

print("🧪 Teste de OCR")

# Criar imagem
img = Image.new('RGB', (400, 100), 'white')
draw = ImageDraw.Draw(img)
draw.text((10, 30), "NF-e: 12345 - R$ 1.000,00", fill='black')

os.makedirs('temp', exist_ok=True)
img.save('temp/test.png')

# OCR
texto = pytesseract.image_to_string('temp/test.png')
print(f"Texto extraído: {texto}")
print("✅ Funcionou!")
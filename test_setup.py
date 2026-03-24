# Testar imports
print("Testando instalações...")

try:
    from playwright.sync_api import sync_playwright
    print("✅ Playwright OK")
except:
    print("❌ Playwright ERRO")

try:
    import pytesseract
    print("✅ Pytesseract OK")
    print(f"   Tesseract path: {pytesseract.pytesseract.tesseract_cmd}")
except:
    print("❌ Pytesseract ERRO")

try:
    from pdf2image import convert_from_path
    print("✅ pdf2image OK")
except:
    print("❌ pdf2image ERRO")

try:
    import cv2
    print("✅ OpenCV OK")
except:
    print("❌ OpenCV ERRO")

try:
    import pandas as pd
    print("✅ Pandas OK")
except:
    print("❌ Pandas ERRO")

print("\nSetup completo!")
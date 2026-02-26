from deep_translator import GoogleTranslator

text = input("Enter text to translate into French: ")

translated = GoogleTranslator(source='auto', target='fr').translate(text)

print("Translated text in French:")
print(translated)
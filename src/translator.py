from deep_translator import GoogleTranslator

def translate(text, target_lang):
    if target_lang == "en":
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except:
        return text
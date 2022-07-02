"""
This module was designed to implement an instance from
IBM Watson Language Translator and using the API, also
here you can find an implementation about how to translate
from English to French and French to English
"""
#import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    This function receive a text in order to translate from\n
    English to French using an API call to IBM Watson and \n
    returning the translation value
    """
    if (english_text is not None and len(english_text)!=0 ):
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        #print(json.dumps(translation, indent=2, ensure_ascii=False))
        translation = translation["translations"][0]["translation"]
        return translation
    return ""

def frenchToEnglish(french_text):
    """
    This function receive a text in order to translate from\n
    French to English using an API call to IBM Watson and \n
    returning the translation value
    """
    if (french_text is not None and len(french_text)!=0 ):
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        #print(json.dumps(translation, indent=2, ensure_ascii=False))
        translation = translation["translations"][0]["translation"]
        return translation
    return ""

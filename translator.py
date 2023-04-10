import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    translator = LanguageTranslatorV3(
        version = '2018-05-01',
        authenticator = apikey)
    
    translator.service_url(url)
    
    frenchText = translator.translate(
         text = englishText,
         model = 'en-fr'
    )

    return frenchText
    


def frenchToEnglish(frenchText):
    translator = LanguageTranslatorV3(
        version = '2018-05-01',
        authenticator = apikey
    )
    
    language_translator.set_service_url(url)
    englishText = translator.translate(
        text = frenchText,
        model ='fr-en'
    )

    return englishText


import speech_recognition as sr                     # pip install SpeechRecognition
import os
import threading
from mtranslate import translate                    #pip install mtranslate
from colorama import Fore,Style,init                 #install karna padega

init(autoreset=True)
def print_loop():
    while True:
        print(Fore.LIGHTCYAN_EX + "I am paying attention ....",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)

def trans_hindi_to_english(text):
    english_text = translate(text,to_language='en-in')
    return english_text

def listen():
    reco = sr.Recognizer()
    reco.dynamic_energy_threshold = False
    reco.energy_threshold = 500
    reco.dynamic_energy_adjustment_damping = 0.03
    reco.dynamic_energy_ratio = 1.9
    reco.pause_threshold = 0.3            #kitna slow bologe utna zyada hona chahiye
    reco.operation_timeout = None
    reco.phrase_threshold = 0.2
    reco.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        reco.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTCYAN_EX + "I am paying attention ....", end="", flush=True)
            try:
                audio = reco.listen(source,timeout=None)
                print("\r"+Fore.LIGHTGREEN_EX + "Your wish is my command master!,initialising ...",end="",flush=True)
                reco_txt = reco.recognize_google(audio).lower()
                if reco_txt:
                    translated_txt = trans_hindi_to_english(reco_txt)
                    print("\r"+Fore.BLUE + "" + translated_txt)
                    return translated_txt
                else:
                    return""
            except sr.UnknownValueError:
                reco_txt = ""
            finally:
                print("\r",end="",flush=True)
            os.system("cls" if os.name == "nt" else "clear")

            listen_thread = threading.Thread(target=listen)
            print_thread = threading.Thread(target=print_loop)
            listen_thread.start()
            print_thread.start()
            listen_thread.join()
            print_thread.join()


listen()
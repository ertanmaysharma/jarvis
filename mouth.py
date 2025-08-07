import asyncio
import os
import edge_tts
import pygame

VOICE = "en-AU-WilliamNeural"

def remove_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error removing file: {e}")

async def amain(TEXT, output_file) -> None:
    try:
        communicate = edge_tts.Communicate(TEXT, VOICE, rate="-10%")
        await communicate.save(output_file)
    except Exception as e:
        print(f"TTS Generation Error: {e}")

def play_audio(file_path):
    try:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.wait(100)  # Don't quit, just wait
        pygame.mixer.quit()
    except Exception as e:
        print(f"Pygame Playback Error: {e}")

def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
    asyncio.run(amain(TEXT, output_file))
    play_audio(output_file)
    remove_file(output_file)

speak("   welcome i am your personal assistant")
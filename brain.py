import requests
import mouth
import ear
import os


# --- Configuration ---
GOOGLE_API_KEY = "AIzaSyBTFAgr5JBKeKcdPebPGlacyBg0TPP0ytw"
MODEL = "gemini-2.0-flash"

def ask_gemini(question, model=MODEL):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GOOGLE_API_KEY}"
    data = {
        "contents": [
            {
                "parts": [{"text": f"Answer very briefly and directly in 2-3 sentences max: {question}"}]
            }
        ]
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        candidates = response.json().get("candidates", [])
        if candidates:
            return candidates[0]["content"]["parts"][0]["text"]
        return "Sorry, I couldn't get an answer."
    except Exception as e:
        return f"Error: {e}"

def run_assistant():
    print("Hello! Ask me anything (type 'exit' to quit).")
    while True:
        user_input = ear.listen()
        if user_input == "":
            print("pls speak clearly")
            mouth.speak("    please speak clearly")
        if user_input.lower() in {"exit", "quit","bye"}:                         #you can add personalization here
            print("   Jarvis: Goodbye!")
            mouth.speak("  Goodbye!")
            break
        if user_input.lower() in {"who are you","hu r u","tum kaun ho"}:
            print("   i am jarvis made by Mr tanmay sharma")
            mouth.speak("    i am jarvis made by Mr tanmay sharma")
            continue
        if user_input == "who made you":
            print("   i am made by Mr tanmay sharma")
            mouth.speak("    i am made by Mr tanmay sharma")
            continue
        if user_input == "who is your master":
            print("   i serve Mr tanmay sharma")
            mouth.speak("    i serve Mr tanmay sharma")
            continue
        else:
            answer = str(ask_gemini(user_input))
            print(f"Jarvis:    {answer}")
            mouth.speak(answer)

if __name__ == "__main__":
    run_assistant()
from assistant.voice import speak, listen
from assistant.web_scrape import scrape_data
from assistant.web_browse import browse_website
from assistant.nlp import get_ai_response

def main():
    speak("Hello, I am Bujji. How can I assist you today?")
    command = listen()
    
    if "browse" in command:
        browse_website("https://example.com")
    elif "scrape" in command:
        data = scrape_data("https://example.com")
        speak(f"I found the following data: {data}")
    else:
        response = get_ai_response(command)
        speak(response)

if __name__ == "__main__":
    main()

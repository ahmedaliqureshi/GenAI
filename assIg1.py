import os
from google import genai
from google.genai import types

def start_chat():
    # 1. Initialize Client
    client = genai.Client(api_key="GEMINI_API_KEY")
    
    model_id = "gemma-4-26b-a4b-it"

    # 2. Setup the Config (Thinking + Search)
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="HIGH"),
        # tools=[types.Tool(google_search=types.GoogleSearch())],
    )

    # 3. Create a Chat Session (This handles history for you)
    chat = client.chats.create(model=model_id, config=config)

    print(f"--- Chatting with {model_id} ---")
    print("(Type 'quit' or 'exit' to stop)\n")

    while True:
        # 4. Get input from YOUR terminal
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break

        print("\nThinking...", end="\r")

        try:
            # 5. Send message and stream the response
            response_stream = chat.send_message_stream(user_input)
            
            print("Gemma: ", end="")
            for chunk in response_stream:
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print("\n") # New line after the response is done

        except Exception as e:
            print(f"\n[Error]: {e}")
            print("Tip: If you get a 500 error, try a shorter question or restart the script.")

if __name__ == "__main__":
    start_chat()


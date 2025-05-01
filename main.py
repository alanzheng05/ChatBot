import google.generativeai as genai

# =============================================================
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
# =============================================================

def chat_with_gemini(temperature=0.7, max_output_tokens=8192):
    
    # Configure the API key
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Configure the model parameters
    generation_config = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
    }
    
    # Set model name
    model_name = "models/gemini-2.0-flash"
    
    # Initialize a chat session
    chat = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config
    ).start_chat()
    
    print("\n" + "="*50)
    print("Welcome to the Gemini Chatbot!")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    print("="*50 + "\n")
    
    # Chat loop
    try:
        while True:
            # Get user input
            user_input = input("\nYou: ")
            # Check if user wants to exit
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nChatbot: Goodbye!")
                break
            # Get response from Gemini
            response = chat.send_message(user_input)
            # Print the response
            print(f"\nChatbot: {response.text}")
            
    except KeyboardInterrupt:
        print("\n\nChat session ended by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    return chat.history

def main():
    if GEMINI_API_KEY == "YOUR_API_KEY_HERE":
        print("Error: Please set your Gemini API key at the top of the file.")
        return 1
    
    try:
        # Start the chat session with default parameters
        chat_with_gemini(temperature=0.7, max_output_tokens=8192)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
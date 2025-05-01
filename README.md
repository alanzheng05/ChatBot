# SETUP
# 1) Get a Gemini API Key:
   - Go to Google AI Studio (https://aistudio.google.com/app/apikey)
   - Create a free API key

# 2) Set up a virtual environment:

   Navigate to the project directory
   ```
   cd ChatBot
   ```

   Create a virtual environment
   ```
   python3 -m venv chatbot_env
   ```

   ## Activate the virtual environment

   On macOS/Linux:
   ``` 
   source chatbot_env/bin/activate
   ```
   
   On Windows:
   ```
   chatbot_env\Scripts\activate
   ```

# 3) Install Dependencies:
   ```
   pip3 install google-generativeai
   ```
   
# 5) Add Your API Key:
   - Open main.py in a text editor
   - Replace "YOUR_API_KEY_HERE" at the top of the file with your actual Gemini API key

# 6) Run the Chatbot:
   ```
   python3 main.py
   ```

# 7) Deactivate the virtual environment when done:
   ```
   deactivate
   ```

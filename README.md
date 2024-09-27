Friday - Voice Assistant Using Langchain and OllamaLLM
Friday is a voice assistant that listens to your queries, uses AI to generate responses with Langchain and the Ollama LLM (LLaMA 3.1), and speaks the answers back to you.

Features
Voice Input: Listens to your voice and converts it into text.
Voice Output: Uses text-to-speech to reply with spoken responses.
AI-Powered Responses: Leverages Langchain and Ollama LLM (LLaMA) to answer questions.
Context Awareness: Remembers conversation history for more accurate responses.
Getting Started
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/friday.git
cd friday
2. Install Dependencies
Make sure you have Python 3.7+ installed, then run:

bash
Copy code
pip install -r requirements.txt
requirements.txt should include:

txt
Copy code
speechrecognition
pyttsx3
langchain
langchain_ollama
3. Install LLaMA Model (Ollama)
You need to install the Ollama LLM, which provides easy access to LLaMA models.

Step 1: Install Ollama
Ollama provides the LLaMA models. You can install Ollama by following the instructions on Ollama's GitHub.

For macOS:

bash
Copy code
brew install ollama
For Windows/Linux: Refer to the Ollama website for installation.

Step 2: Download the LLaMA Model
Once you have installed Ollama, download the version of the LLaMA model you want. For example:

bash
Copy code
ollama pull llama2-7b
This will download the 7 billion parameter model. You can change 7b to 13b, 30b, or others depending on your needs.

4. Run Friday
Start the assistant by running:

bash
Copy code
python main.py
5. Usage
Friday will greet you and start listening for your input.
Ask a question, and Friday will respond using AI.
Say "exit" to quit the conversation.
Example
vbnet
Copy code
You: What is the population of India?
Friday: The population of India is approximately 1.4 billion.
Customize Model Size and Parameters
You can adjust the model size directly in the code by modifying the model_name variable. Here’s how to change the model in the script:

python
Copy code
from langchain_ollama import OllamaLLM

# Set model size (e.g., 'llama2-7b', 'llama2-13b')
model_name = "llama2-7b"  # Change this to the model size you want to use
model = OllamaLLM(model=model_name)
Replace "llama2-7b" with another model size, such as 13b or 30b, as per your requirements.

More Guidance
For detailed instructions on Ollama and LLaMA, check the Ollama GitHub repository.
Watch this YouTube tutorial for step-by-step guidance on using Ollama LLaMA models.
Future Enhancements
Improve context management and memory capabilities.
Add support for multiple languages.
License
This project is licensed under the MIT License.


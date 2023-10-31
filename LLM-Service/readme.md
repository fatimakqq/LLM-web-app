# Large Language Model (LLM) App
This is a Flask-based web app that uses the Hugging Face Transformers library to interact with the Big Science BLOOMZ Large Language Model.

# Usage
The service can be accessed at the following URL in your web browser:
https://furthr.informatik.uni-marburg.de/llm

To use the web app, enter a text prompt in the form and click the "Submit" button to see the model's response. Prompts can be edited, replaced, and resubmitted.

# Requirements
To run this web app, you will need to have Python 3.6 or higher installed on your system.
All additional packages/libraries, including Flask and Transformers can be downloaded by running the following command:
``
pip install -r requirements.txt
``
# GPU Setup
The service is using port 7777 on the GPU Server, at IP Address 192.168.178.22
( get details from Alex about how it's set up to continously run! )

To run the service manually, navigate into the /app/home/fatimakhalid/LLMQ-As directory and run
``
python app.py
``

# Model Information
The BLOOMZ model is a multilingual version of the BLOOM text generation model which has been fine-tuned to perform tasks and respond to specific prompts. View more about the model's specific capabilites on the Hugging Face website:
https://huggingface.co/bigscience/bloomz

This web app uses the second-largest version with 7.1 billion parameters. The largest version, with 176 billion parameters was not suitable for the GPU server's capabilities as prompt requests returned nothing, even after hours. All smaller versions were extensively tested with the following tasks:
- Text Summarization
- Information Extraction
- Question Answering
- Text Classification
- Conversation
- Text Generation
- Code Generation
- Reasoning

The best performance was from the 7.1 billion parameter version, which is also the largest version the server could handle.

The model can easily be replaced with any Large Language Model (LLM) from the Hugging Face library. Simply edit the code (model name, tokenizer, etc) in app.py based on the documentation for the new model.

# Example Prompts
"Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance. Explain the above in one sentence: "

"一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。Would you rate the previous review as positive, neutral or negative?"

"The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.

Human: Hello, who are you?

AI: Greeting! I am an AI research assistant. How can I help you today?

Human: Can you tell me about the creation of blackholes?

AI: "


# Authors
Fatima Khalid fxk200007@utdallas.edu

# Credits
This web app was created using the Hugging Face Transformers library and the Flask web framework.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

2023

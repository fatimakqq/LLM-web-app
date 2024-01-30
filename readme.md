# Large Language Model (LLM) App
This is a Flask-based web app that uses the Hugging Face Transformers library to interact with the Meta LLaMa 2 Large Language Model.

# Usage

## Local deployment
Locally, the service can be started via `python3 app.py`. The service can be accessed at [Removed for Privacy]

LLaMa models are probably too large to deploy locally. What you can do to test locally is checkout the branch `bloomz` and change `model_name = "bigscience/bloomz-7b1"` in `app.py` to something smaller that more likely fits your local resources. Try for example `model_name = "bigscience/bloomz-560m"`. You should be able to choose any model from https://huggingface.co/

## Server deployment
On the server, normal users can start the app via `python3 /storage/ailab/llm/app.py`, sudoers via `sudo service llm start`.

The service can be accessed at the following URL in your web browser: [Removed for Privacy]

To use the web app, enter a text prompt in the form and click the "Submit" button to see the model's response. Prompts can be edited, replaced, and resubmitted.

# Requirements
To run this web app, you will need to have Python 3.6 or higher installed on your system. If you do not already have Flask, transformers, and Accelerate, run the following commands:
``
pip install flask transformers accelerate
``
All additional packages/libraries can be downloaded by running the following command:
``
pip install -r requirements.txt
``
# GPU Setup
To access the GPU server, you need [an FB12 account]([Removed for Privacy]). Say your username and password are `tom4` and `1234`, respectively. You can change your password [following
these instructions]([Removed for Privacy]).

To now connect to the GPU server you can do so via `ssh`, or entering this information in an ssh client like Putty on Windows. **Note: You need to be in university network to do this. If you are remote, [use VPN]([Removed for Privacy])**. Once connected you should issue the `groups` command to check if the response contains
`[Removed for Privacy]`. 

To run the service manually, navigate into the `[Filepath Removed for Privacy]` directory (`cd`) and run `python3 app.py`. Now the service should be available.

If you want to update files in `[Filepath Removed for Privacy]` there are three ways:

1. You do it directly on the server, using for example `vim app.py`
2. You do it locally and copy the files to the server, for example `scp`
3. You push it to this repository, navigate to `[Filepath Removed for Privacy]` and perform a `git pull` there. First you need to [generate a new ssh
   key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) **on the server** and [add it to your ssh
agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent). To make this key usable for this repository, send it to [[Email Removed for Privacy]]

Generally, we suggest method 3 because it makes sure that all changes are persisted and version controlled in this repository. For trial and error tasks you can use method 1 or 2.

# Model Information
Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. 
This project uses the 7B fine-tuned model, optimized for dialogue use cases and converted for the Hugging Face Transformers format. 

View more on the model here:
https://huggingface.co/meta-llama/Llama-2-7b-chat-hf and here https://huggingface.co/docs/transformers/main/model_doc/llama
 
This web app uses the smallest version (7 billion parameters). The larger version, with 13 billion or 70 billion parameters were  not suitable for the GPU server's capabilities as simple prompt requests, such as: "Give me a recipe for apple pie." took at
least 5 minutes to return a response. All versions were extensively tested with the following tasks:
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

The model is at a temperature of 1.0. Through experimentation, any lower (ex. 0.9 yielded overly repetitive output while higher temperature values (ex. 1.1 yielded highly inaccurate and random information.

# Example Prompts
"Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance. Explain the above in one sentence: "

"一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。Would you rate the previous review as positive, neutral or negative?"

"The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.

Human: Hello, who are you?

AI: Greeting! I am an AI research assistant. How can I help you today?

Human: Can you tell me about the creation of blackholes?

AI: "

# Data

Data can be found in the `data` directory. For each dataset there is a subdirectory holding all scenarios for that dataset. Within a scenario (e.g., `data/Efes/fdb1-mb2`)
there are four directories: 
- `ground_truth` holding a ground truth matrix for every `<sourceTable>___<targetTable>.csv` table pair.
    The value at position `(i,j)` in a ground truth matrix indicates whether the `i-th` source column matches the `j-th` target column.
- `source` representing the source database, i.e., holding a list of source tables.
- `target` representing the target database, i.e., holding a list of target tables.

## Efes Datasets

These two datasets are introduced in the paper *Estimating Data Integration and Cleaning Effort* by Kruse et al. (2015, [Download](https://hpi.de/naumann/projects/repeatability/data-integration/estimating-data-integration-and-cleaning-effort.html)).

`Efes-bib` consists of four schemata for bibliographic data from [the amalgam dataset](http://dblab.cs.toronto.edu/~miller/amalgam/) which are assembled to three matching scenarios.

`Efes-music` consists of three schemata for music data which are assembled to three matching scenarios. The three schemata are:
- `fdb`: [FreeDB](https://gnudb.org/)
- `mb`: [MusicBrainz](https://musicbrainz.org/)
- `dis`: [Discogs](https://www.discogs.com/)

## Pubs Dataset

The Pubs dataset is a popular SQL sample dataset which mocks a book publishing company. You can access the dataset [here](https://www.codeproject.com/Articles/20987/HowTo-Install-the-Northwind-and-Pubs-Sample-Databa) and explore its structure through this [ER-Diagram](https://relational.fit.cvut.cz/assets/img/datasets-generated/pubs.svg).

The Pubs dataset offers five different variations, each originating from the original dataset as the source:

- pubs1: `Original Dataset (Unchanged)`
- pubs2: `Original Dataset with Modified Headers`
- pubs3: `Original Dataset Joined via Inner Join`
- pubs4: `Original Dataset Joined via Full Outer Join`
- pubs5: `Original Dataset with Encoding Changes`

# Authors
Fatima Khalid fxk200007@utdallas.edu

# Credits
This web app was created using the Hugging Face Transformers library and the Flask web framework.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

2023

# Further Reading
1. [LLaMa Recipes](https://github.com/facebookresearch/llama-recipes/tree/main): Maybe we find something for our requirements here and more best practices.
2. [LLaMa Issues](https://github.com/facebookresearch/llama/issues): Maybe we find information on people having similar problems or eventually make our own post here.
3. [Using LLaMa2-Chat with HuggingFace Transformers](https://huggingface.co/blog/llama2#using-transformers): Our current implementation(?)
4. [HuggingFace reference deployment of LLaMa-2-7b](https://huggingface.co/spaces/huggingface-projects/llama-2-7b-chat)

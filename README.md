# ChatGPT Voice Assistant....
## 🚀 Project Overview 

This project is a simple voice assistant that can answer questions and perform basic tasks, such as searching the web or playing music.
The voice assistant uses the OpenAI API to generate responses to user queries, and the Amazon Polly API to generate speech output.

## Installation 🧰
To install the dependencies for this project, run the following command:

    pip install -r requirements.txt

You will also need to set up environment variables for your OpenAI and Amazon Polly API keys.
See the API Keys section below for more information.

## Usage 🧑🏾‍💻
To run the voice assistant, simply run the following command:

    python main.py

You can then speak to the voice assistant and ask it questions or give it commands. Some examples of things you can ask include:

"Who is Elon Musk?"
"What's the difference between machine learning and artificial intelligence?"
"What's the capital of France?"
The voice assistant will respond to your queries with spoken output.

## API Keys 🔐
This project requires API keys for both the OpenAI API and the Amazon Polly API. To set up these API keys, you will need to create environment variables for them. Here's how to do it:

Open a terminal window.

Set the following environment variables:

    OPENAI_API_KEY=<your OpenAI API key>
    AMAZON_POLLY_API_KEY=<your Amazon Polly API key>

Note: Replace <your_openai_secret_key>, <your_aws_access_key_id>, and <your_aws_secret_access_key> with your actual API keys.

Save these environment variables by adding the above commands to your .bashrc or .bash_profile file.

## ⚠️ Limitations and Future Work

Currently, this voice assistant is limited in its capabilities, and can only respond to a small number of pre-defined queries. In the future, additional functionality could be added, such as support for more natural language queries and integration with additional APIs and services.

## Contributors
- Ibrahim (Main Contributor)
- Contributions are welcome!

Special thanks to the creators of the OpenAI and Amazon Polly APIs for providing the tools that made this project possible.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
If you have any questions or issues with this project, please contact Jane Doe at janedoe@example.com.
# Memory Agent

An AI-powered memory agent with caching capabilities, built using LangChain and OpenAI's GPT model.

## Features

- Caches responses to reduce API calls
- Configurable cache expiration
- Easy to extend for multiple LLM providers

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- An OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Josiah-O/memory-agent.git
   cd memory-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. [Add any specific usage instructions or examples here]

## Project Structure

- `memory_agent.py`: Contains the MemoryAgent class implementation
- `main.py`: The main script to run the Memory Agent
- `config.py`: Configuration settings for the agent
- `utils.py`: Utility functions used by the agent
- `requirements.txt`: List of Python package dependencies

## Contributing

[Add instructions for how others can contribute to your project]

## License

[Specify the license under which your project is released]

## Contact

[Your contact information or how people can reach out with questions]

# Memory Agent

An AI-powered memory agent with caching capabilities, built using Swarms, LangChain, and OpenAI's GPT model.

## Features

- Uses Swarms for distributed AI agent coordination
- Caches responses to reduce API calls
- Configurable cache expiration
- Easy to extend for multiple LLM providers

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- An OpenAI API key
- Swarms API key (if required)

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

5. Create a `.env` file in the root directory and add your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   SWARMS_API_KEY=your_swarms_api_key_here
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

We welcome contributions to the Memory Agent project! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or concerns, please contact: buildwithjosiah@gmail.com

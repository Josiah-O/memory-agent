import os
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Set WORKSPACE_DIR explicitly
os.environ["WORKSPACE_DIR"] = os.path.expanduser("~")

class MemoryAgent:
    def __init__(self, llm_provider="openai", cache_expiration=3600):
        self.llm_provider = llm_provider
        self.cache_expiration = cache_expiration
        self.api_calls = 0
        self.cache = {}

        # Set up OpenAI API key
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Initialize LLM clients
        if llm_provider == "openai":
            self.llm = ChatOpenAI(api_key=self.openai_api_key)
        elif llm_provider == "ollama":
            # You'll need to implement OllamaChat or use an appropriate Ollama integration
            raise NotImplementedError("Ollama integration not implemented yet")
        else:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}")

    def search(self, query):
        # Check if the query is in cache and not expired
        if query in self.cache:
            timestamp, result = self.cache[query]
            if time.time() - timestamp < self.cache_expiration:
                print("Cache hit!")
                return result

        # If not in cache or expired, perform an API call
        result = self.make_api_call(query)

        # Store the result in cache with timestamp
        self.cache[query] = (time.time(), result)
        return result

    def make_api_call(self, query):
        self.api_calls += 1
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=query)
        ]
        response = self.llm.invoke(messages)
        return response.content

    def get_api_call_count(self):
        return self.api_calls

# Test the agent
if __name__ == "__main__":
    # Test with different providers
    providers = ["openai"]  # Removed "ollama" as it's not implemented
    
    for provider in providers:
        print(f"\nTesting with {provider.upper()} provider:")
        agent = MemoryAgent(llm_provider=provider, cache_expiration=10)  # Set to 10 seconds for testing
        queries = [
            "What is the capital of France?",
            "What is the capital of France?",  # Repeated to test caching
            "What is the largest planet in our solar system?",
            "What is the capital of France?",  # Repeated after a delay to test expiration
        ]
        for i, query in enumerate(queries):
            if i == 3:
                print("Waiting for cache to expire...")
                time.sleep(11)  # Wait for cache to expire
            result = agent.search(query)
            print(f"Query: {query}")
            print(f"Result: {result}")
            print(f"Total API calls: {agent.get_api_call_count()}")
            print("---")

from memory_agent import MemoryAgent

def main():
    agent = MemoryAgent()
    queries = [
        "Find laptops under $1000 with 16GB RAM.",
        "Find laptops under $1000 with 16GB RAM.",  # Repeated query to demonstrate memory hit
        "Find smartphones with 5G capability under $500."
    ]
    
    for query in queries:
        result = agent.search(query)
        print(f"Query: {query}")
        print(f"Result: {result}")
        print("---")

if __name__ == "__main__":
    main()

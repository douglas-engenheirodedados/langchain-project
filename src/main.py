from langchain import LangChain
from agents import Agent
from chains import Chain

def main():
    # Initialize LangChain components
    langchain = LangChain()

    # Set up the agent
    agent = Agent()
    langchain.add_agent(agent)

    # Set up the chain
    chain = Chain()
    langchain.add_chain(chain)

    # Start execution of the chain
    langchain.run()

if __name__ == "__main__":
    main()
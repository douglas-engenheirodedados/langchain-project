# LangChain Project

This project implements an agentic flow using the LangChain framework. It serves as a template for building applications that leverage agents and chains for various tasks.

## Project Structure

```
langchain-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── agents           # Contains agent-related classes
│   │   └── __init__.py
│   ├── chains           # Contains chain-related classes
│   │   └── __init__.py
│   └── utils            # Contains utility functions and classes
│       └── __init__.py
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/douglas-engenheirodedados/langchain-project
   cd langchain-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Components

- **Agents**: This module contains classes for creating and managing agents within the LangChain framework.
- **Chains**: This module defines the structure and execution of the agentic flow.
- **Utils**: This module provides utility functions that assist in the operation of agents and chains, such as logging and configuration management.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.
# Basic AI Agent Using PhiData and LLaMA (Groq API)

## Introduction
This project demonstrates how to build a basic AI agent using the PhiData library and LLaMA (via Groq API). The goal is to create a simple yet functional AI agent that interacts with the LLaMA model to process text-based inputs and provide meaningful responses. This project is intended as an introductory exercise to gain hands-on experience with AI agent development.

## Features
- Connects to the LLaMA model using the Groq API.
- Processes text input and generates intelligent responses.
- Simple and easy-to-extend code structure.

## Requirements
Ensure you have the following installed on your system:

1. Python 3.8+
2. Required Python libraries:
   - `phidata`
   - `groq`
   - `python-dotenv`

## Setup

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/basic-ai-agent.git
cd basic-ai-agent
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install phidata groq python-dotenv
```

### Step 3: Configure API Key
1. Create a `.env` file in the project root directory.
2. Add your Groq API key to the `.env` file:
   ```env
   GROQ_API_KEY=gsk_your_api_key_here
   ```

### Step 4: Run the Agent
Execute the script to start the agent:
```bash
python main.py
```

## Code Overview

### Main Components
1. **`main.py`**
   This script contains the core logic for initializing the agent and processing user input. It performs the following steps:
   - Loads the Groq API key from the `.env` file.
   - Creates an agent using the LLaMA model.
   - Sends a sample message and prints the response.

2. **Agent Initialization**
   ```python
   from phi.agent import Agent
   from phi.model.groq import Groq
   from dotenv import load_dotenv
   
   load_dotenv()

   agent = Agent(
       model=Groq(id="llama-3.3-70b-versatile")
   )

   agent.print_response("Share a 2 sentence love story between dosa and samosa")
   ```

## Customization
To customize the agent:
- Modify the input prompt in `agent.print_response()` to explore different types of interactions.
- Integrate the agent with other APIs or functionalities to extend its capabilities.

## Troubleshooting

### Common Issues
1. **Invalid API Key**: Ensure the API key in the `.env` file is correct and has no trailing spaces.
2. **Connection Error**: Verify your internet connection and check if the Groq API service is reachable.
3. **Dependencies Not Installed**: Reinstall the required libraries:
   ```bash
   pip install --upgrade phidata groq python-dotenv
   ```

## Future Improvements
- Implement a user-friendly command-line interface (CLI) for better interaction.
- Add error handling for more robust execution.
- Integrate real-time input processing using Flask or FastAPI for web-based interactions.
- Explore fine-tuning the LLaMA model for domain-specific tasks.

## Conclusion
This project provides a foundational understanding of creating AI agents using PhiData and LLaMA. By extending this basic setup, you can build more sophisticated AI-driven applications. Happy coding!

---

**Author**: Nipuna Janaranjana   
**Date**: January 2025


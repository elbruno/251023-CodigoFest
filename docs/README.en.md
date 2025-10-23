# 🇬🇧 English Documentation - CodigoFest 2023

## Discover the Latest in AI in the Azure Ecosystem

This documentation provides a comprehensive guide to the demos and content presented at CodigoFest 2023.

---

## 📑 Table of Contents

1. [Introduction](#introduction)
2. [MCP Servers](#mcp-servers)
3. [Agents with Microsoft Agent Framework](#agents-with-microsoft-agent-framework)
4. [C# Agent Framework Projects](#c-agent-framework-projects)
5. [Installation and Usage Guides](#installation-and-usage-guides)
6. [Usage Examples](#usage-examples)
7. [Troubleshooting](#troubleshooting)

---

## 🎯 Introduction

This repository demonstrates the most advanced capabilities of Artificial Intelligence in the Azure ecosystem, focusing on:

- **Model Context Protocol (MCP)**: Standard protocol for connecting tools and data with AI systems
- **Microsoft Agent Framework**: Framework for building intelligent agents that can reason and execute tasks
- **Azure AI Foundry**: Complete platform for developing, training, and deploying AI solutions
- **Hugging Face Integration**: Image generation with advanced models

### What is Model Context Protocol (MCP)?

MCP is an open protocol that standardizes how applications provide context to Large Language Models (LLMs). It allows AI agents to access:
- Enterprise data
- Tools and APIs
- External services
- Local file systems

---

## 🏆 MCP Servers

### 1. World Cup 2026 Info Server

Specialized MCP server that provides comprehensive information about FIFA World Cup 2026.

#### 📋 Features

- **Tournament Information**: Dates, venues, number of teams and matches
- **Host Cities**: Details of the 16 host cities and their stadiums
- **Match Schedule**: Tournament structure and key dates
- **Historical Data**: Unique facts about this historic world cup

#### 🔧 Available Tools

1. **get_tournament_info()**
   - Returns general tournament information
   - No parameters required
   - JSON format response

2. **get_host_cities(country: Optional[str])**
   - Gets information about host cities
   - Optional parameter: filter by country ('United States', 'Canada', 'Mexico')
   - Includes stadium name, capacity, and match types

3. **get_match_schedule()**
   - Returns tournament structure and calendar
   - Information about group stage and knockout rounds
   - Key dates and special notes

#### 📊 World Cup 2026 Data

```json
{
  "name": "FIFA World Cup 2026",
  "hosts": ["United States", "Canada", "Mexico"],
  "dates": "June 11 - July 19, 2026",
  "teams": 48,
  "matches": 104,
  "venues": 16,
  "first_tri_nation_host": true
}
```

#### 🎯 Use Cases

```python
# Example 1: General tournament information
await get_tournament_info()

# Example 2: United States cities
await get_host_cities(country="United States")

# Example 3: Complete schedule
await get_match_schedule()
```

#### 🚀 How to Run

```bash
cd MCP/worldcup-info

# Option 1: Use uv (recommended)
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml --extra dev

# Option 2: Use pip
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Debug with Agent Builder (VS Code)
# Press F5 and select "Debug in Agent Builder"
```

#### 🧪 Test with MCP Inspector

```bash
cd inspector
npm install

# Start Inspector (from VS Code Debug panel)
# Select "Debug SSE in Inspector (Edge)" or "(Chrome)"
# F5 to start

# In the browser:
# 1. Click "Connect"
# 2. Select "List Tools"
# 3. Choose a tool and execute it
```

### 2. Sample Weather Server

Sample MCP server that provides simulated weather data.

#### 📋 Features

- Simple server for demonstration
- Random weather data
- Base for creating custom MCP servers

#### 🔧 Available Tools

1. **get_weather(location: str)**
   - Returns simulated weather information
   - Required parameter: location (city, state, coordinates)
   - Response with temperature and weather condition

#### 🎯 Usage Example

```python
# Query weather for a city
await get_weather(location="Toronto")

# Example response:
# {
#   "location": "Toronto",
#   "temperature": "72°F",
#   "condition": "Sunny"
# }
```

#### 🚀 How to Run

```bash
cd MCP/SampleWeather

# Setup environment
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Debug with Agent Builder
# F5 in VS Code with "Debug in Agent Builder"
```

---

## 🤖 Agents with Microsoft Agent Framework

### WorldCup Info Agent v1

Intelligent agent that combines World Cup 2026 queries with pixel art style image generation.

#### 🎨 Main Capabilities

1. **Informational Queries**
   - Answers questions about World Cup 2026
   - Accesses real-time data via MCP
   - Provides accurate and updated information

2. **Image Generation**
   - Generates pixelated style images (pixel art, 8-bit)
   - Uses FLUX1 Schnell model via Hugging Face
   - Customizable parameters (size, seed, steps)

3. **Multi-turn Conversation**
   - Maintains context between questions
   - Persistent thread for coherent conversations
   - Streaming response processing

#### ⚙️ Technical Configuration

```python
# Azure AI Foundry Endpoint
ENDPOINT = "https://bruno-realtime-resource.services.ai.azure.com/api/projects/bruno-realtime"
MODEL_DEPLOYMENT_NAME = "gpt-5-mini"

# MCP Tools
MCPStreamableHTTPTool(
    name="brunoHF",
    description="MCP server for brunoHF",
    url="https://huggingface.co/mcp?login"
)
```

#### 📝 Agent Instructions

The agent is configured for:

- **Language**: Spanish (default), adaptable per user request
- **Image Generation**: Always in pixelated style using FLUX1 Schnell
- **Response Format**: Structured JSON with reasoning and conclusion
- **Security**: Avoids copyrighted content, offers legal alternatives

#### 🔄 Workflow

```
User → Question
    ↓
Agent → Analyzes intent
    ↓
Requires image? → YES → Generates descriptive prompt
    |                         ↓
    |                    Calls gr1_flux1_schnell_infer
    |                         ↓
    NO                   Receives image URL
    ↓                         ↓
Queries MCP Server ← ← ← ← ←
    ↓
Builds structured response
    ↓
User ← JSON Response
```

#### 💬 Conversation Examples

**Example 1: Informational Query**
```
User: "How is the weather in Toronto?"

Agent:
{
  "location": "Toronto",
  "temperature": "72°F",
  "condition": "Sunny"
}
```

**Example 2: Image Generation**
```
User: "Can you generate an image of a raccoon playing soccer at the 2026 World Cup?"

Agent:
{
  "input": "Generate image of raccoon playing soccer at World Cup 2026",
  "reasoning": [
    "User requests image, must be generated in pixelated style",
    "Use gr1_flux1_schnell_infer tool from Hugging Face",
    "Avoid official logos due to copyright"
  ],
  "response": "I have generated a pixelated 8-bit style image of a raccoon playing soccer. The image has a retro classic video game style.",
  "image": {
    "requested": true,
    "model_used": "evalstate/flux1_schnell",
    "generation_parameters": {
      "prompt": "Pixel art 8-bit raccoon playing soccer at World Cup 2026, wearing jersey, kicking ball in stadium, crowd in background, retro video game style, limited color palette, blocky sprites, nostalgic gaming aesthetic",
      "width": 1024,
      "height": 1024,
      "num_inference_steps": 4,
      "randomize_seed": true
    },
    "image_url": "https://huggingface.co/.../image.png",
    "notes": "Image without official logos to avoid copyright issues"
  }
}
```

#### 🚀 How to Run

```bash
# Install dependencies
pip install agent-framework
pip install agent-framework-azure-ai
pip install azure-identity

# Configure environment variables (or edit the script)
export AZURE_AI_ENDPOINT="your-endpoint"
export AZURE_AI_MODEL="your-model"

# Run the agent
cd Agents
python worldcupinfo-v1.py
```

#### 🔑 Requirements

- Azure AI Foundry Project
- Azure Default Credential configured
- Hugging Face Token (for image generation)
- Python 3.8+

#### 🎛️ Image Generation Parameters

```python
generation_parameters = {
    "prompt": "Detailed description (60-70 words)",
    "width": 1024,           # Range: 256-2048
    "height": 1024,          # Range: 256-2048
    "seed": 123456789,       # Optional: 0-2147483647
    "randomize_seed": True,  # If True, random seed
    "num_inference_steps": 4 # Range: 1-16
}
```

---

## 🔧 C# Agent Framework Projects

### Project Structure

The `src/` directory contains three example C# projects demonstrating Agent Framework usage:

```
src/
├── AgentFx-01/
│   ├── Program.cs
│   └── AgentFx-01.csproj
├── AgentFx-02/
│   ├── Program.cs
│   └── AgentFx-02.csproj
└── AgentFx-03/
    ├── Program.cs
    └── AgentFx-03.csproj
```

### Current Status

Currently, these projects contain basic "Hello World" templates. They are starting points for:

1. **Integration with Azure AI Services**
2. **Implementing agents in .NET**
3. **Connecting to MCP servers from C#**
4. **Building enterprise applications with agents**

### 🚀 Build and Run

```bash
cd src/AgentFx-01

# Restore dependencies
dotnet restore

# Build
dotnet build

# Run
dotnet run
```

### 🔜 Future Development

These projects are prepared to implement:

- ✅ Conversational agents in C#
- ✅ Integration with Azure OpenAI
- ✅ Connection with MCP servers
- ✅ Document processing
- ✅ Enterprise automation

---

## 📚 Installation and Usage Guides

### System Requirements

#### Required Software
- **Python**: 3.8 or higher
- **Node.js**: 16.x or higher (for MCP Inspector)
- **.NET SDK**: 6.0 or higher (for C# projects)
- **Visual Studio Code**: Latest version
- **Git**: To clone the repository

#### Recommended VS Code Extensions
- AI Toolkit for VS Code
- Python Extension
- C# Extension
- Python Debugger

### Azure Configuration

#### 1. Azure AI Foundry Project

```bash
# Create a project in Azure AI Foundry
# 1. Go to https://ai.azure.com
# 2. Create new project
# 3. Deploy model (e.g., gpt-4o-mini)
# 4. Copy endpoint and key
```

#### 2. Configure Credentials

```bash
# Option 1: Azure CLI
az login

# Option 2: Environment variables
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
```

### Hugging Face Configuration

```bash
# Get Hugging Face token
# 1. Go to https://huggingface.co/settings/tokens
# 2. Create new token with read permissions
# 3. Save token securely

# Configure in code
headers = {
    "Authorization": "Bearer hf_your_token_here"
}
```

### Complete Step-by-Step Installation

#### Step 1: Clone Repository

```bash
git clone https://github.com/elbruno/251023-CodigoFest.git
cd 251023-CodigoFest
```

#### Step 2: Configure World Cup MCP Server

```bash
cd MCP/worldcup-info

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .[dev]
```

#### Step 3: Configure Weather MCP Server

```bash
cd ../SampleWeather

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e .[dev]
```

#### Step 4: Configure Agent

```bash
cd ../../Agents

# Install agent dependencies
pip install agent-framework
pip install agent-framework-azure-ai
pip install azure-identity

# Edit worldcupinfo-v1.py
# - Update ENDPOINT with your Azure endpoint
# - Update MODEL_DEPLOYMENT_NAME with your model
# - Update Authorization header with your HF token
```

#### Step 5: Configure C# Projects

```bash
cd ../src

# Restore all projects
dotnet restore

# Build solution
dotnet build
```

---

## 💡 Usage Examples

### Scenario 1: Query World Cup Information

```python
# In Agent Builder or MCP Inspector

# Question 1
"What are the host cities for World Cup 2026 in Mexico?"

# Expected response:
# - Mexico City (Estadio Azteca)
# - Guadalajara (Estadio Akron)
# - Monterrey (Estadio BBVA)

# Question 2
"When is the final and where will it be played?"

# Expected response:
# July 19, 2026 at MetLife Stadium, New Jersey, USA
```

### Scenario 2: Generate Themed Images

```python
# User requests image
"Generate a pixel art style image of the World Cup mascot playing soccer"

# The agent:
# 1. Builds descriptive prompt with pixelated style
# 2. Calls gr1_flux1_schnell_infer
# 3. Returns image and metadata
```

### Scenario 3: Multi-turn Conversation

```python
# Turn 1
User: "How many teams will participate in World Cup 2026?"
Agent: "48 teams will participate in World Cup 2026..."

# Turn 2
User: "And how many matches will be played in total?"
Agent: "A total of 104 matches will be played..."

# Turn 3
User: "Generate an image of a stadium full of fans"
Agent: [Generates image in pixel art style]
```

### Scenario 4: Debugging with MCP Inspector

```bash
# 1. Start Inspector
cd MCP/worldcup-info/inspector
npm install
npm run dev

# 2. Open browser at http://localhost:5173

# 3. Connect to MCP server

# 4. Test tools:
# - List Tools
# - Select get_host_cities
# - Input: {"country": "Canada"}
# - Run Tool

# 5. See JSON response with Canadian cities
```

---

## 🔧 Troubleshooting

### Issue: Error installing Python dependencies

```bash
# Solution 1: Update pip
python -m pip install --upgrade pip

# Solution 2: Use uv (faster)
pip install uv
uv venv
uv pip install -r pyproject.toml --extra dev
```

### Issue: Azure authentication error

```bash
# Solution 1: Re-login with Azure CLI
az login
az account show

# Solution 2: Verify environment variables
echo $AZURE_TENANT_ID
echo $AZURE_CLIENT_ID

# Solution 3: Use interactive DefaultAzureCredential
# In code, make sure to use:
# DefaultAzureCredential(exclude_environment_credential=False)
```

### Issue: MCP Inspector doesn't connect

```bash
# Verify MCP server is running
# In VS Code, Debug panel → "Debug SSE in Inspector"

# Check port (default 3001)
curl http://localhost:3001

# If port is busy, change in:
# - .vscode/tasks.json
# - .vscode/launch.json
# - src/__init__.py
# - .aitk/mcp.json
```

### Issue: Image generation error

```bash
# Verify Hugging Face token
# Token must have read permissions

# Verify model is available
# https://huggingface.co/evalstate/flux1_schnell

# Verify generation parameters
# width and height: 256-2048
# num_inference_steps: 1-16
# seed: 0-2147483647
```

### Issue: C# project doesn't compile

```bash
# Clean and rebuild
dotnet clean
dotnet restore
dotnet build

# Check .NET version
dotnet --version

# If SDK is missing, install from:
# https://dotnet.microsoft.com/download
```

### Issue: VS Code can't find Python interpreter

```bash
# 1. Reload VS Code after creating venv
# 2. Command: "Python: Select Interpreter"
# 3. Select: .venv/bin/python

# If it doesn't appear:
which python  # Linux/Mac
where python  # Windows

# Add path manually in VS Code settings
```

---

## 📊 System Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────────────┐
│                     User / Client                        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Microsoft Agent Framework                   │
│  ┌────────────────────────────────────────────────┐    │
│  │  ChatAgent with custom instructions            │    │
│  │  - Natural language processing                 │    │
│  │  - Multi-turn context management               │    │
│  │  - Intent routing                              │    │
│  └────────────┬───────────────────────────────────┘    │
└───────────────┼──────────────────────────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
┌──────────────┐  ┌──────────────────┐
│ Azure AI     │  │ MCP Tools        │
│ Foundry      │  │                  │
│              │  │  ┌────────────┐  │
│ - GPT-4o     │  │  │ brunoHF    │  │
│ - GPT-4o     │  │  │ (Hugging   │  │
│   mini       │  │  │  Face)     │  │
│              │  │  └────────────┘  │
└──────────────┘  └─────────┬────────┘
                            │
                    ┌───────┴────────┐
                    ▼                ▼
        ┌──────────────────┐  ┌──────────────┐
        │ MCP worldcup-    │  │ FLUX1        │
        │ info Server      │  │ Schnell      │
        │                  │  │ Model        │
        │ - tournament_info│  │              │
        │ - host_cities    │  │ Image        │
        │ - match_schedule │  │ Generation   │
        └──────────────────┘  └──────────────┘
```

### Data Flow

1. **User Input**: Question or request in natural language
2. **Agent Processing**: Intent and context analysis
3. **Routing**: Decision on which tools to use
4. **Tool Execution**: Calls to MCP servers or APIs
5. **Aggregation**: Combine responses from multiple sources
6. **Response Generation**: Structured JSON format
7. **Return to User**: Response with reasoning and results

---

## 🎓 Key Concepts

### Model Context Protocol (MCP)

**What is it?**
An open protocol that standardizes how applications provide context to LLMs.

**Benefits:**
- ✅ Tool reusability across different applications
- ✅ Clear separation between business logic and AI
- ✅ Easy debugging and testing
- ✅ Security and access control

**Components:**
- **Server**: Exposes tools and resources
- **Client**: Consumes tools (e.g., Agent Framework)
- **Transport**: Communication (stdio, HTTP, SSE)

### Microsoft Agent Framework

**What is it?**
Framework for building agents that can reason, plan, and execute complex tasks.

**Features:**
- 🧠 Integration with Azure AI and OpenAI models
- 🔧 Support for tools and function calling
- 💬 Multi-turn conversation management
- 🔄 Response streaming
- 🔌 Connectivity with MCP servers

**Use Cases:**
- Intelligent virtual assistants
- Business process automation
- Document analysis
- Content generation
- Information search and synthesis

### Azure AI Foundry

**What is it?**
Unified platform for developing, training, evaluating, and deploying AI solutions.

**Key Services:**
- 🤖 Azure OpenAI Service
- 🎯 Model Catalog
- 🧪 Prompt Flow
- 📊 Evaluation Tools
- 🚀 Deployment Options

---

## 🚀 Next Steps

### For Developers

1. **Explore the examples**: Run each demo to understand the flow
2. **Modify prompts**: Experiment with different instructions for agents
3. **Create your own MCP Server**: Use templates as a base
4. **Integrate with your data**: Connect agent to your own information sources
5. **Deploy to production**: Deploy on Azure Container Instances or App Service

### To Learn More

#### Recommended Tutorials
- [MCP Documentation](https://modelcontextprotocol.io/docs)
- [Microsoft Agent Framework Quickstart](https://github.com/microsoft/agent-framework)
- [Azure AI Foundry Learning Path](https://learn.microsoft.com/azure/ai-services)

#### Additional Resources
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers)
- [AI Toolkit Documentation](https://github.com/microsoft/vscode-ai-toolkit)
- [Hugging Face Documentation](https://huggingface.co/docs)

### To Experiment

#### Project Ideas

1. **World Cup Travel Assistant**
   - Integrate flight and hotel APIs
   - Personalized match recommendations
   - Generate itineraries

2. **Team Analysis Bot**
   - Query historical statistics
   - Predict results
   - Generate visualizations

3. **Social Media Content Generator**
   - Create automatic posts about matches
   - Generate promotional images
   - Publication calendar

4. **Enterprise Chatbot**
   - Connect to corporate database
   - Answer employee queries
   - Automate repetitive tasks

---

## 📞 Contact and Support

### Author
**Bruno Capuano (elbruno)**
- GitHub: [@elbruno](https://github.com/elbruno)
- Event: [CodigoFest](https://codigofacilito.com/codigofest)

### Community
- Participate in GitHub discussions
- Report issues and bugs
- Contribute with pull requests
- Share your projects based on these demos

### Help Resources
- [GitHub Issues](https://github.com/elbruno/251023-CodigoFest/issues)
- [Azure Support](https://azure.microsoft.com/support)
- [MCP Community](https://github.com/modelcontextprotocol/discussions)

---

## 📝 Final Notes

### Recommendations

1. **Security**: Never share tokens or credentials in code
2. **Costs**: Monitor Azure AI usage to avoid unexpected charges
3. **Rate Limits**: Respect API limits (Hugging Face, Azure)
4. **Testing**: Test thoroughly before production
5. **Logging**: Implement logging for debugging and auditing

### Known Limitations

- Current MCP servers are for demonstration
- World Cup 2026 data may change
- Image generation depends on Hugging Face availability
- C# projects are basic templates

### Contributions Welcome

This project is open to contributions:
- 🐛 Report bugs
- ✨ Propose new features
- 📝 Improve documentation
- 🌍 Translate to other languages
- 💡 Share use cases

---

**Thank you for using these CodigoFest 2023 demos!**

🎉 We hope this content helps you explore the latest AI news in the Azure ecosystem.

---

**License**: MIT License  
**Last Update**: October 2023  
**Version**: 1.0.0

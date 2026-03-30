# Mewchi CLI

Mewchi is a terminal-based utility designed to standardize and enhance engineering prompts. By utilizing Groq’s LPU (Language Processing Unit) and the Llama 3.1 8B model, it transforms brief or underspecified coding requests into structured, architectural prompts suitable for high-level LLM interactions.

## Core Capabilities

* **Prompt Engineering:** Automatically re-drafts input to include technical constraints, architectural roles, and explicit output formats.
* **Low-Latency Inference:** Optimized for the Groq API to provide near-instantaneous processing (typically under 200ms).
* **Terminal Integration:** A minimalist UI featuring floating brackets and a focused input bar, modeled after modern developer tools.
* **Environment Awareness:** Automatically detects the current working directory and active Git branch to provide better context for prompts.
* **Streaming Output:** Uses a word-by-word streaming mechanism to render responses as they are generated.

## Installation

### Prerequisites

* Python 3.8 or higher.
* An active Groq API Key.

### Standard Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ubu11/mewchi-cli.git
   cd mewchi-cli
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Global Configuration (Linux)
   To access Mewchi from any directory in your shell:

   - Grant execution permissions to the main script:
     ```bash
     chmod +x mewchi_cli.py
     ```

   - Create a symbolic link in your local bin directory:
     ```bash
     sudo ln -s $(pwd)/mewchi_cli.py /usr/local/bin/mewchi
     ```

4. Add your Groq API key to your shell configuration file (`~/.bashrc` or `~/.zshrc`):
   ```bash
   export GROQ_API_KEY='your_api_key_here'
   ```

5. Refresh your shell environment:
   ```bash
   source ~/.bashrc
   ```

### Usage

Launch the interface by typing the command:
```bash
mewchi
```

### Example

**Input:**
```
> Enter prompt: create a fastapi auth system
```

**Output:**
```
Act as a Senior Backend Developer. Design a robust authentication system using FastAPI and JWT. Ensure the prompt includes:
- Password hashing via Passlib (bcrypt).
- OAuth2 with Password flow.
- Pydantic models for request validation.
- Database integration using SQLAlchemy for user persistence.
```

## Configuration

The tool relies on the following environment variables:

| Variable | Function |
|----------|----------|
| `GROQ_API_KEY` | Required for authentication with the Groq LPU server. |
| `MODEL_NAME` | Set to `llama-3.1-8b-instant` for optimal speed. |

## Dependencies

Mewchi is built using several key Python libraries:

* **Rich:** Handles the layout, panels, and terminal color rendering.
* **Groq:** Facilitates the connection to the Llama 3.1 8B model via LPU hardware.
* **Prompt Toolkit:** Manages the interactive, stateful input bar.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

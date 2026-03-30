# Mewchi CLI

A vibrant CLI tool designed to enhance your coding prompts using Groq's LPU server. Mewchi acts as your coding companion,transforming vague or basic coding requests into highly specific, architectural and clear prompts.



## Features

- **Prompt Enhancement**: Uses Groq's AI to rewrite your coding requests for clarity and specificity.
- **Interactive CLI**: Rich, user-friendly interface with ASCII art and real-time feedback.
- **Git Integration**: Displays the current Git branch for context.
- **Markdown Output**: Streams enhanced prompts in a beautifully formatted markdown panel.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)
- Groq API key (sign up at [Groq](https://groq.com))

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/ubu11/mewchi-cli.git
   cd mewchi-cli
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment:

   - Create a `.env` file in the project root.
   - Add your Groq API key:

     ```plaintext
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

1. Run the CLI:

   ```bash
   python mewchi_cli.py
   ```

2. Enter your coding prompt when prompted.

3. View the enhanced output in real-time.

4. Type `exit`, `quit`, or `q` to exit the CLI.

## Example

```plaintext
 > Enter prompt: create a to-do list app

✦ Mewchi's Enhanced Prompt:

Create a to-do list application with the following features:
- Add tasks with a title and optional description
- Mark tasks as complete or incomplete
- Delete tasks
- Persist tasks to localStorage
- Display tasks in a clean, responsive UI
- Use React for the frontend and Node.js for the backend
```

## Configuration

- **`.env`**: Contains the Groq API key. Ensure this file is not committed to version control (it is ignored via `.gitignore`).

## Dependencies

- `groq`: For interacting with the Groq API.
- `python-dotenv`: For loading environment variables.
- `rich`: For beautiful terminal output.
- `prompt_toolkit`: For interactive prompts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Support

For issues or questions, please contact the project maintainer or open an issue on GitHub.

import os
import typer
from groq import Groq
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()


app = typer.Typer()
console = Console()

SYSTEM_PROMPT = (
    "You are an expert Prompt Engineer. Transform the user's raw input into "
    "a high-quality, structured, and professional prompt for an AI. "
    "Include: Role, Context, Constraints, and Output Format. "
    "IMPORTANT: Output ONLY the enhanced prompt text inside a Markdown block. "
    "Do not include conversational filler."
)


@app.command()
def main(
    prompt: str = typer.Argument(..., help="The raw prompt you want to enhance"),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy output to clipboard")
):

  api_key = os.environ.get("GROQ_API_KEY")

  if not api_key:
        console.print("[bold red]Error:[/bold red] Please set the GROQ_API_KEY environment variable")
        raise typer.Exit()
  client = Groq(api_key=api_key)

  with console.status("[bold green]Generating better prompt...", spinner="dots"):
    try:
      completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Enhance this: {prompt}"}
                ],
                temperature=0.6,
            )
      enhanced_text = completion.choices[0].message.content

      console.print(Panel(Markdown(enhanced_text), title="[bold yellow]Enhanced Prompt[/bold yellow]", border_style="bright_blue"))

      if copy:
        import pyperclip
        pyperclip.copy(enhanced_text)
        console.print("[italic green]Copied to clipboard![/italic green]")
    except Exception as e:
            console.print(f"[bold red]API Error:[/bold red] {e}")
if __name__ == "__main__":
    app()




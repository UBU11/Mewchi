#!/usr/bin/env python3

import os
import time
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.live import Live
from rich.markdown import Markdown
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style as PromptStyle

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

from enhancer import get_enhanced_prompt

console = Console()

def get_git_branch():
    try:
        branch = subprocess.check_output(
            ['git', 'branch', '--show-current'],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return branch if branch else "main"
    except Exception:
        return "main"

def display_header():
    logo = Text("""
  ███╗   ███╗███████╗██╗    ██╗ ██████╗██╗  ██╗██╗
  ████╗ ████║██╔════╝██║    ██║██╔════╝██║  ██║██║
  ██╔████╔██║█████╗  ██║ █╗ ██║██║     ███████║██║
  ██║╚██╔╝██║██╔══╝  ██║███╗██║██║     ██╔══██║██║
  ██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╗██║  ██║██║
  ╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝╚═╝""", style="bold #f4f09a")

    mascot = Text(r"""
         ▄█▄                ▄█▄
        ▄█░█▄              ▄█░█▄
       ▄█░░░▀▀▄▄▄▄▄▄▄▄▄▄▄▄▀▀░░░█▄
       █░░░░░░░░░░░░░░░░░░░░░░░░█
       █░░▄██▄░░░░░░░░░░▄██▄░░░░█
       █░░▀██▀░░░▄██▄░░░▀██▀░░░░█
       ▀▄░░░░░░░░▀██▀░░░░░░░░░░▄▀
        ▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀
         ▄█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄
       ▄█░░░░░░░░░░░░░░░░░░░░░░█▄
       █░░░░░░░░░░░░░░░░░░░░░░░░█
       █░░░░░░░░░▄▄▄▄░░░░░░░░░░░█       ▄▄▄▄
       █░░░░░░░░██████░░░░░░░░░░█▄▄▄▄▄▄█░░░░█
       ▀▄░░░░░░░▀████▀░░░░░░░░░░░░░░░░░░░░░▄▀
        ▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀
          ▄█░░░█▄        ▄█░░░█▄
          ▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀""", style="bold bright_green")


    header_layout = Columns([logo, mascot], expand=False, padding=(1, 4))
    header_panel = Panel(
        header_layout,
        border_style="dim white",
        title="[bold white]Welcome to Mewchi[/bold white]",
        title_align="left",
        subtitle="[dim]CLI Version 0.1[/dim]",
        subtitle_align="right",
        padding=(0, 2)
    )

    console.print("\n")
    console.print(header_panel)

def show_status():
    git_branch = get_git_branch()

    console.print("\n[dim]Version 1.0.4 · Commit 7f8a9b2[/dim]\n")
    console.print("Mewchi can your vibe partner to improve your vibe coding")
    console.print("Describe a task to get started or enter [bold yellow]?[/bold yellow] for help.")
    console.print("\n[bold blue]●[/bold blue] Connected to Groq LPU Server")
    console.print("[bold blue]●[/bold blue] Logged in as user: [bold white]MewchiDev[/bold white]")
    cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
    console.print(f"\n[bold white]{cwd} [[cyan] {git_branch}[/cyan]][/bold white]")

def stream_markdown_output(text):
    current_text = ""
    words = text.split(" ")

    console.print("\n[bold magenta]✦ Mewchi's Enhanced Prompt:[/bold magenta]")

    with Live(Panel(Markdown(current_text), border_style="cyan"), refresh_per_second=30) as live:
        for word in words:
            current_text += word + " "
            live.update(Panel(Markdown(current_text), border_style="cyan"))
            time.sleep(0.03)

    console.print("\n" + "[dim]─[/dim]" * 65 + "\n")

def main_loop():
    session = PromptSession()

    input_style = PromptStyle.from_dict({
        'prompt': 'bg:#2b2b2b #ffffff bold',
        'input': '#569cd6',
    })

    while True:
        try:

            console.print("[dim]╭" + "─" * 65 + "╮[/dim]")
            user_input = session.prompt(
                " > Enter prompt: ",
                style=input_style,
            )
            console.print("[dim]╰" + "─" * 65 + "╯[/dim]")

            if user_input.lower() in ["exit", "quit", "q"]:
                break

            if user_input:
                with console.status("[bold cyan]Mewchi is thinking...[/bold cyan]", spinner="dots"):
                    enhanced = get_enhanced_prompt(user_input)
                stream_markdown_output(enhanced)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    display_header()
    show_status()

    console.print("[dim]Ctrl+C Exit · Type 'quit' to close[/dim]\n")
    main_loop()

    console.print("\n[bold red]Exiting Mewchi CLI...[/bold red]")

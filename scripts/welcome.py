# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "rich",
# ]
# ///

"""Welcome script for Document Engineering course using rich for flashy output."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich import box
import time


def main():
    """Display a fun welcome message for Document Engineering students."""
    console = Console()

    # Clear screen and add some space
    console.clear()
    console.print()

    # Create flashy title
    title = Text("🎉 WELCOME TO DOCUMENT ENGINEERING KRISH! 🎉", style="bold magenta")
    title_panel = Panel(
        Align.center(title), box=box.DOUBLE, style="bright_cyan", padding=(1, 2)
    )
    console.print(title_panel)
    console.print()

    # Prosegrammers explanation
    prosegrammers_content = Text()
    prosegrammers_content.append("Welcome to the world of ", style="bold blue")
    prosegrammers_content.append("PROSEGRAMMERS", style="bold yellow on red")
    prosegrammers_content.append("! 📝💻\n\n", style="bold blue")
    prosegrammers_content.append("• ", style="green")
    prosegrammers_content.append("Prose", style="italic cyan")
    prosegrammers_content.append(" + ", style="white")
    prosegrammers_content.append("Programmers", style="italic cyan")
    prosegrammers_content.append(
        " = Masters of Code AND Documentation! ✨", style="white"
    )

    prosegrammers_panel = Panel(
        Align.center(prosegrammers_content),
        title="What are Prosegrammers?",
        title_align="center",
        box=box.ROUNDED,
        style="green",
    )
    console.print(prosegrammers_panel)
    console.print()

    # Course highlights with fun emojis
    highlights = [
        "🐍 Master Python Programming",
        "📚 Document Engineering Magic",
        "🤖 AI-Powered Development",
        "📊 Data Visualization Wizardry",
        "🔧 Professional Tool Mastery",
        "🌟 Collaborative Git Workflows",
    ]

    highlight_columns = Columns(
        [
            Panel(h, style=f"bold {color}", box=box.SIMPLE)
            for h, color in zip(
                highlights, ["red", "blue", "green", "yellow", "magenta", "cyan"]
            )
        ],
        equal=True,
        expand=True,
    )

    console.print(
        Panel(
            highlight_columns,
            title="🚀 What You'll Learn",
            title_align="center",
            style="bright_white",
        )
    )
    console.print()

    # Motivational message with animation effect
    motivation_lines = [
        "Get ready to become a documentation SUPERHERO! 🦸‍♀️🦸‍♂️",
        "You'll learn to write code that's not just functional...",
        "...but also BEAUTIFULLY documented! 📖✨",
        "Welcome to your journey as a Prosegrammer! 🎓🚀",
    ]

    for line in motivation_lines:
        console.print(Align.center(Text(line, style="bold bright_yellow")))
        time.sleep(0.8)

    console.print()

    # Final flourish
    final_message = Text(
        "Let's make some document engineering MAGIC! ✨🎪✨",
        style="bold white on bright_magenta",
    )
    final_panel = Panel(
        Align.center(final_message), box=box.HEAVY, style="bright_magenta"
    )
    console.print(final_panel)
    console.print()


if __name__ == "__main__":
    main()


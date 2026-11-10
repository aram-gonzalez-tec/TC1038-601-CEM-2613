from rich import print
from rich.prompt import Prompt

print("[blue bold]Hola[/blue bold] mundo")
pregunta = Prompt.ask("Dame tu respuesta", choices=["1", "2", "3"])
import sys
import argparse

# This app does not exist for me, it exists for others to make scheduling their lives easier with the focus on God.
# and so that I can get an internship hopefully which supports my future family.

from rich import print as rprint
import cli.interface
from config import VERSION


def parse_args():
    parser = argparse.ArgumentParser(description="Roles CLI Scheduler")
    parser.add_argument("--version", action="store_true", help="Show app version")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.version:
        rprint(f"[bold green]Roles v{VERSION}[/bold green]")
        sys.exit(0)

    cli.interface.run_cli()
    


if __name__ == "__main__":
    main()

from . import __app_name__
from .cli import app

def main():
    app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
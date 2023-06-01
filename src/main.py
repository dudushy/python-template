# pip freeze | xargs pip uninstall -y
# pip freeze > requirements.txt
#* -- Imports
import os
import sys

#* -- Variables
title = "template-python" #? Title
path = os.path.dirname(__file__) #? Directory path

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    pass

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        _, _, exc_tb = sys.exc_info()
        print(f"[{title}#__main__] error (line: {exc_tb.tb_lineno}): ", e)

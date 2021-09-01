from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import button_dialog

def main():
    result = button_dialog(
        title="Button",
        text="Yes or no ?",
        buttons=[("Yes",True),("No",False),("Maybe...", None)],
    ).run()

    print("Result = {}".format(result))

if __name__ == "__main__":
    main()
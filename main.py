import PySimpleGUI as sg


# exampleText -> example_text
def to_snake_case(text: str) -> str:
    char_list = []
    alpha = False
    for char in text:
        if char.isupper() and alpha:
            char_list.extend(("_", char.lower()))
        else:
            char_list.append(char)
        alpha = char.isalpha() and not char.isupper()  # ex: conv2D

    return "".join(char_list)


# example_text -> exampleText
def toCamelCase(text: str) -> str:
    char_list = []
    convert_now = False
    alpha = False
    for char in text:
        if char == "_" and alpha:
            convert_now = True
        elif convert_now:
            char_list.append(char.upper())
            convert_now = False
        else:
            char_list.append(char)
        alpha = char.isalpha()  # ex: doNTimes

    return "".join(char_list)


layout = [
    [sg.Text("Input:  "), sg.Multiline(size=(100, 10), key="input")],
    [sg.Text("Output: "), sg.Multiline(size=(100, 10), key="output")],
    [sg.Checkbox("Reverse (snakecase to camelcase)", key="reverse")],
    [sg.Button("Generate text", key="gen"), sg.Exit()]
]

window = sg.Window("camelcase to snakecase", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "gen":
        text = values["input"]
        if not values["reverse"]:
            window["output"].update(to_snake_case(text))
        else:
            window["output"].update(toCamelCase(text))

window.close()

import PySimpleGUI as sg

window = sg.Window(title="RNX Gear Books", layout=[[sg.Text("Choose your action")],
                                            [sg.Button("Add an Order")]], margins=(500, 300))


while True:
    event, values = window.read()
    if event in "Add an Order" or event == sg.WIN_CLOSED:
        break

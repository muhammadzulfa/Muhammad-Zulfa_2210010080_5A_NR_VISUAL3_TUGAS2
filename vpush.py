import PySimpleGUI as sg

# Membuat layout jendela
layout = [
    [sg.VPush()],
    [sg.Text("UNISKA MAAB", font=("helvetica", 24))],
    [sg.Push()],
    [sg.Push()],
    [sg.Text("BANJARMASIN", font=("Courier", 18))],
    [sg.Push()],
    [sg.VPush()]
]

# Membuat jendela
window = sg.Window(
    title="Elemen Text",
    layout=layout,
    size=(430, 200)
)

window.read()
window.close()
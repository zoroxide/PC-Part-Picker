import PySimpleGUI as g
import pc_builder_data_entry_window

layout = [
    [g.Text("Welcome to Pc Picker!",justification='center')],
    [g.Button("Build A New PC Build!"), g.Button('Show Builded PCs')],
    [g.Button('About'),g.Button('Quit')],
]

window = g.Window("pc picker", layout)

while True:
    event, values = window.read()
    if event == g.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Build A New PC Build!':
        pc_builder_data_entry_window.main()
    if event == 'Show Builded PCs':
        g.popup('soon')
    if event == 'About':
        g.popup("""
        2022/1/20
        The Source Code available at Github:
        => https://github.com/loay-mohamed-xv/PC-Part-Picker
        """)
    if event == 'Quit':
        break

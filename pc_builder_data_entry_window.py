import PySimpleGUI as g

#main loop
def main():

    layout = [          
    [g.Text("PC BUILDER")],
    [g.Text("CPU:")],
    [g.Input(key="cpu-name",size=(20,1)), g.Text("Price"),g.Input(size=(10,1),key="cpu-price")],
    [g.Text("CPU Cooler:")],
    [g.Input(size=(20,1),key='cpu-cooler-name'), g.Text("Price"),g.Input(size=(10,1),key='cpu-cooler-price')],
    [g.Text("Ram:")],
    [g.Input(size=(20,1),key='ram-name'), g.Text("Price"),g.Input(size=(10,1),key='ram-price')],
    [g.Text("MotherBoard:")],
    [g.Input(size=(20,1),key='motherboard-name'), g.Text("Price"),g.Input(size=(10,1),key='motherboard-price')],
    [g.Text("HDD:")],
    [g.Input(size=(20,1),key='hdd-name'), g.Text("Price"),g.Input(size=(10,1),key='hdd-price')],
    [g.Text("SSD:")],
    [g.Input(size=(20,1),key='ssd-name'), g.Text("Price"),g.Input(size=(10,1),key='ssd-price')],
    [g.Text("GPU:")],
    [g.Input(size=(20,1),key='gpu-name'), g.Text("Price"),g.Input(size=(10,1),key='gpu-price')],
    [g.Text("Case:")],
    [g.Input(size=(20,1),key='case-name'), g.Text("Price"),g.Input(size=(10,1),key='case-price')],
    [g.Text("Power Supply:")],
    [g.Input(size=(20,1),key='psu-name'), g.Text("Price",key='price'),g.Input(size=(10,1))],
    [g.Button('Save Build'), g.Button("Quit")]
]

    window = g.Window("PC BULDER - Data Entry", layout)

    while True:
        event, values = window.read()
        if event == g.WINDOW_CLOSED or event == 'Quit':
            break
        if event == 'Save Build':
            print("---------")
            print("saved")
            print("---------")
            g.popup(f"""
        The Build:
        ==========
        CPU: {values['cpu-name']}
        CPU Price : {values['cpu-price']}
        
        CPU Cooler : {values['cpu-cooler-name']}
        CPU Cooler Price: {values['cpu-cooler-price']}
        -
        Ram: {values['ram-name']}
        Ram Price: {values['ram-price']}
        -
        Mother Board: {values['motherboard-name']}
        Mother Board Price: {values['motherboard-price']}
        -
        HDD: {values['hdd-name']}
        HDD Price: {values['hdd-price']}
        -
        SSD: {values['ssd-name']}
        SSD Price: {values['ssd-price']}
        -
        Case: {values['case-price']}
        Case Price: {values['case-price']}
        -
        PSU: {values['psu-name']}
        ==========
        SAVED!!
        """)
    
    window.close()

main()
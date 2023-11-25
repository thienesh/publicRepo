import PySimpleGUI as sg

# Define the layout of the window
layout = [
    [sg.Text("Hello, PySimpleGUI!")],
    [sg.Button("Click Me")]
]

# Create the window
window = sg.Window("PySimpleGUI Example", layout)

while True:
    event, values = window.read()

    # Exit the program if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Handle button click event
    if event == "Click Me":
        sg.popup("Button Clicked!")

# Close the window when the loop exits
window.close()

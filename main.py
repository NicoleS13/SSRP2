def on_button_pressed_a():
    global Start
    if Start == False:
        Start = True
        radio.send_number(1)
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Start
    if Start == True:
        Start = False
        radio.send_string("stop")
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global x, y, z
    if name == "x":
        x = value
    elif name == "y":
        y = value
    elif name == "z":
        z = value
    if name == "Movement":
        basic.show_string("M=")
        basic.show_string("" + str((value)))
        basic.clear_screen()
    elif name == "Time":
        basic.show_string("T=")
        basic.show_string("" + str((value)))
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
radio.on_received_value(on_received_value)

z = 0
y = 0
x = 0
Start = False
radio.set_group(1)
Start = False
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    """)

def on_forever():
    if Start == True:
        serial.write_value("x", x)
        serial.write_value("y", y)
        serial.write_value("z", z)
basic.forever(on_forever)

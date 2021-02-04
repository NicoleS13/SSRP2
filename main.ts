input.onButtonPressed(Button.A, function () {
    if (Start == false) {
        Start = true
        radio.sendNumber(1)
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    if (Start == true) {
        Start = false
        radio.sendString("stop")
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "x") {
        x = value
    } else if (name == "y") {
        y = value
    } else if (name == "z") {
        z = value
    }
    if (name == "Movement") {
        basic.showString("M=")
        basic.showString("" + (value))
        basic.clearScreen()
    } else if (name == "Time") {
        basic.showString("T=")
        basic.showString("" + (value))
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
})
let z = 0
let y = 0
let x = 0
let Start = false
radio.setGroup(1)
Start = false
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    `)
basic.forever(function () {
    if (Start == true) {
        serial.writeValue("x", x)
        serial.writeValue("y", y)
        serial.writeValue("z", z)
    }
})

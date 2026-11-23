input.onButtonPressed(Button.A, function () {
    basic.showString("Hello!")
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("CIAO!")
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showString("TI VOGLIO TANTO BENE")
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # . . . #
        `)
    basic.showLeds(`
        . . . . .
        # # # . .
        # # # . .
        # . # . .
        # . # . .
        `)
    basic.showLeds(`
        . . . . .
        # . # . .
        # # # . .
        # . . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # . . . #
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.Heart)
})

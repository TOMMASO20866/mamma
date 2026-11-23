def on_button_pressed_a():
    basic.show_string("Hello!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("CIAO!")
    basic.show_icon(IconNames.HEART)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    basic.show_string("TI VOGLIO TANTO BENE")
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_ab():
    basic.show_leds("""
        . . . . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # . . . #
        """)
    basic.show_leds("""
        . . . . .
        # # # . .
        # # # . .
        # . # . .
        # . # . .
        """)
    basic.show_leds("""
        . . . . .
        # . # . .
        # # # . .
        # . . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)

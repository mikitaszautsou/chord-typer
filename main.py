from pynput import keyboard

# Define the vocabulary mapping
vocabulary = {
    'as': 'how ',
    'ad': 'to ',
    'af': 'do ',
    'aj': 'create ',
    'ak': 'simple ',
    'al': 'dart ',
    'a;': 'project ',
    'sd': 'test ',
    'sf': 'example ',
    'sg': 'main ',
    'sh': 'input'
    
}

# Keep track of the pressed keys
pressed_keys = []

def on_press(key):
    global pressed_keys

    try:
        if key.char is not None:
            # Append the pressed key to the list
            pressed_keys.append(key.char)
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl) if needed
        pass
    if len(pressed_keys) > 10:
        pressed_keys = pressed_keys[-10:]

    print('pressed keys', pressed_keys)
    # Convert the pressed keys to a string
    input_str = ''.join(pressed_keys)

    # Check if the input string matches any vocabulary entry
    for key, value in vocabulary.items():
        if input_str.endswith(key):
            # Remove the matched keys from the pressed keys list
            pressed_keys = pressed_keys[:-len(key)]

            # Simulate backspace to remove the original input
            for _ in range(len(key)):
                keyboard.Controller().press(keyboard.Key.backspace)
                keyboard.Controller().release(keyboard.Key.backspace)

            # Type the replacement string
            keyboard.Controller().type(value)

            break

def on_release(key):
    # Stop the listener when the 'esc' key is released
    if key == keyboard.Key.esc:
        return False

# Create a keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
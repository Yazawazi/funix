from funix.widget import slider


sunset = {
    "name": "sunset",
    "widgets": {
        "float": "inputbox",
        "str": "textarea",
        ("int", "float"): slider(100),
        "Literal": "radio"
    },
    "colors": {
        "background": {
            "default": "#ff9e1b"
        }
    }
}

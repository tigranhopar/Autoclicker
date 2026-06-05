# Autoclicker GUI

This project is a graphical user interface (GUI) for an autoclicker application. It allows users to automate mouse clicks at specified intervals or rates, with a clean and simple greyscale design.

## Project Structure

```
autoclicker-gui
├── src
│   ├── main.py          # Entry point for the application
│   ├── autoclicker.py   # Core functionality of the autoclicker
│   ├── ui.py            # User interface components and layout
│   ├── controller.py     # Manages interactions between UI and autoclicker logic
│   └── styles
│       └── grayscale.css # CSS styles for the application
├── requirements.txt      # Lists dependencies required for the project
└── README.md             # Documentation for the project
```

## Features

- Toggle the autoclicker on and off using a designated shortcut.
- Set clicking intervals with fields for hours, minutes, seconds, and milliseconds.
- Set clicking rates using a numeric input and a dropdown for selecting time units (milliseconds, seconds, minutes, hours).
- Full greyscale design for a minimalist aesthetic.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd autoclicker-gui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Use the provided buttons in the GUI to select shortcuts, quit the program, and toggle between interval and rate modes.
- Input the desired values in the respective fields to customize the autoclicking behavior.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
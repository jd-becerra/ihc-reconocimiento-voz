# python-voice-recognizer

## Human–Computer Interaction (HCI) Project: Voice-Controlled Grid Navigation

This project explores **voice-based interaction** as an alternative input method for controlling movement in a 2D grid. The user can move a character using **spoken commands in Spanish**, combining real-time speech recognition with a graphical interface.

The goal of the project is to demonstrate how **natural language input** can be integrated into interactive systems to improve accessibility, usability, and user experience.

---

## Project Overview

* **Voice recognition** using real-time microphone input
* **Grid-based movement system** controlled by spoken directions
* **Hybrid GUI** combining Tkinter and Pygame
* **Keyboard fallback** using arrow keys

This project was developed as part of an **HCI (Human–Computer Interaction)** course, focusing on multimodal interaction and user-centered design.

---

## Technologies Used

* **Python**
* **speech_recognition** (Google Speech API)
* **Pygame** (rendering and game loop)
* **Tkinter** (GUI controls and layout)
* **Threading** (non-blocking voice input)
* **Virtual environments (venv)**

---

## How It Works

1. The application displays a **grid** with a player positioned at the center.
2. The user can:

   * Move using **arrow keys**, or
   * Click a button to **enable voice input**.
     
3. When voice input is enabled:

   * The microphone listens asynchronously.
   * Spoken commands are recognized in Spanish.
   * Valid commands move the player in real time.

### Supported Voice Commands (in Spanish, since this was the language used in the course)

| Command    | Movement     |
| ---------- | ------------ |
| `norte`    | Up           |
| `sur`      | Down         |
| `este`     | Left         |
| `oeste`    | Right        |
| `noreste`  | Up + Left    |
| `noroeste` | Up + Right   |
| `sureste`  | Down + Left  |
| `suroeste` | Down + Right |

---

## Architecture & Design Decisions

### Voice Recognition (`voice_recognition.py`)

* Runs in a **separate thread** to avoid blocking the GUI.
* Uses timeout handling to prevent crashes when no speech is detected.
* Designed as a reusable class with a simple `toggle()` interface.

### GUI Layer (`gui.py`)

* Tkinter is used for:

  * Window management
  * Buttons
  * Voice command logging
* Pygame is embedded inside Tkinter using `SDL_WINDOWID`.
* Clear separation between:

  * Input handling
  * Rendering
  * Game logic

### Grid System (`grid.py`)

* Encapsulates:

  * Grid rendering
  * Player positioning
  * Boundary validation
* Player movement is constrained to valid grid cells.

---

## How to Run the Project

### 1. **Make sure you have Python and the pip dependency installed**.

### 2. **Install your virtual environment** with the following command:

```bash
python -m venv venv
```

### 3. **Initialize the virtual environment**. On Windows, use the following command:

```bash
.\venv\Scripts\activate
```

**NOTE**: If on Windows you get an error mentioning that scripts cannot be run on the system, enter the following command in a PowerShell terminal with administrator privileges:

```bash
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
```

Your terminal should display `(venv)` at the beginning of the path.

---

### 4. **Install the project**:

```bash
pip install -e .
```

*(Note the dot, it must be run exactly from the root of the directory)*

---

### 5. **Run the application**:

```bash
run_ihc_app
```

---

## Limitations

* Voice recognition depends on:

  * Internet connection
  * Microphone quality
* Commands must be spoken clearly and match predefined keywords.
* Currently supports **Spanish only**.

---

## Possible Improvements

* Support for multiple languages
* Dynamic command mapping
* Confidence-based command filtering
* Visual feedback for recognized commands
* Accessibility options (speech feedback, subtitles)
* Replace Google API with an offline speech model

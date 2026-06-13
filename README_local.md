# Railway CCTV Safety Line Detection System

An interactive, real-time computer vision system built with **Python**, **OpenCV**, **YOLOv8**, and **Pygame** to detect safety violations near railway platforms or hazardous areas.

The system overlays a safety line and overlays a translucent **Danger Zone (Red Zone)**. If a person crosses the line into the danger zone, the system plays an audio alert, captures a screenshot of the violation, and logs the event timestamp to a CSV file.

---

## Features

- **Real-Time Person Detection**: Powered by YOLOv8 (nano model) for fast CPU-friendly inference.
- **Dynamic Red Zone Masking**: Automatically calculates and highlights the forbidden area on one side of the safety line using cross-product orientation math.
- **Interactive Controls**: Position and rotate the safety line dynamically using keyboard controls while the video runs.
- **Audio Alerts**: Plays a warning sound effect (Pygame Mixer) immediately upon violation.
- **Automated Logging**:
  - Appends timestamped entries to `logs/violations.csv`.
  - Saves evidence screenshots to the `screenshots/` directory.

---

## Interactive Controls

When the video window is focused, use the following keyboard controls to calibrate the safety boundary:

| Key | Action |
| :---: | --- |
| **`W`** | Move safety line Up |
| **`S`** | Move safety line Down |
| **`A`** | Move safety line Left |
| **`D`** | Move safety line Right |
| **`E`** | Rotate safety line clockwise |
| **`R`** | Rotate safety line anti-clockwise |
| **`Z`** | Increase safety line thickness |
| **`T`** | Toggle object detection on/off |
| **`Q`** | Quit the application |

---

## Installation & Setup

### Prerequisites
- Python 3.11.x (or compatible Python 3.x version)

### Setup Steps
1. **Clone or navigate** to the project directory:
   ```bash
   cd railwaycctv
   ```

2. **Activate the Virtual Environment**:
   * **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If PyTorch gives issues in your environment, reinstall it using the CPU-only package source:*
   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   ```

---

## Project Structure

```text
railwaycctv/
│
├── .venv/                  # Python Virtual Environment
├── logs/
│   └── violations.csv      # Log file containing safety violation timestamps
├── screenshots/            # Evidence screenshots captured during violations
├── sounds/
│   └── alert.wav           # Sound file played when a person enters the red zone
├── videos/
│   └── demo.mp4            # Input CCTV camera video stream
│
├── config.py               # Configuration file (detection confidence threshold, etc.)
├── main.py                 # Core application script
├── requirements.txt        # Package dependencies list
├── yolov8n.pt              # YOLOv8 nano model weights
└── README.md               # Project documentation
```

---

## Running the Application

To run the application, make sure the virtual environment is activated and execute:

```bash
python main.py
```

The system will start up, load the YOLO weights and demo video, and open the interactive video screen.

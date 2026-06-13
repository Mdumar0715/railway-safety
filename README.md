# Railway CCTV Safety Line Detection System

## Overview

Railway CCTV Safety Line Detection System is a real-time computer vision application designed to improve passenger safety at railway platforms and restricted areas. Using YOLOv8 and OpenCV, the system continuously monitors CCTV footage and detects when a person crosses a predefined safety boundary into a hazardous zone.

When a safety violation occurs, the system instantly triggers an audio warning, captures evidence screenshots, and logs the incident with a timestamp for future analysis.

## Key Features

### Real-Time Person Detection

* Uses YOLOv8 Nano for fast and efficient human detection.
* Optimized for real-time performance on standard CPU systems.

### Intelligent Danger Zone Monitoring

* Creates a configurable safety line and danger zone.
* Automatically identifies when a person enters the restricted area.

### Instant Alert System

* Plays an audio warning whenever a violation is detected.
* Helps prevent accidents through immediate notification.

### Violation Logging & Evidence Collection

* Stores violation timestamps in a CSV log file.
* Captures screenshots of each incident for record keeping and review.

### Interactive Calibration Controls

* Move and rotate the safety boundary while the application is running.
* Allows quick adjustment for different camera angles and platform layouts.

## Technology Stack

* Python
* OpenCV
* YOLOv8
* Ultralytics
* Pygame
* NumPy

## Project Structure

```text
railwaycctv/
├── logs/
│   └── violations.csv
├── screenshots/
├── sounds/
│   └── alert.wav
├── videos/
│   └── demo.mp4
├── config.py
├── main.py
├── requirements.txt
├── yolov8n.pt
└── README.md
```

## Installation

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Controls

| Key | Function                |
| --- | ----------------------- |
| W   | Move Line Up            |
| S   | Move Line Down          |
| A   | Move Line Left          |
| D   | Move Line Right         |
| E   | Rotate Clockwise        |
| R   | Rotate Anti-Clockwise   |
| Z   | Increase Line Thickness |
| T   | Toggle Detection        |
| Q   | Quit Application        |

## Applications

* Railway Platform Safety Monitoring
* Restricted Area Surveillance
* Passenger Safety Enforcement
* Smart Transportation Systems

## Future Enhancements

* Multi-Camera Support
* Cloud-Based Incident Storage
* SMS/Email Alert Integration
* Live CCTV Streaming Support
* AI-Based Crowd Analysis

## Outcome

The system provides an automated railway safety monitoring solution that helps reduce accidents, improves surveillance efficiency, and enables rapid response to safety violations through AI-powered real-time detection.


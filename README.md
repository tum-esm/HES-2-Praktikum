# HES-2-Praktikum

## Messstation TUM N5 Dach

In diesem Praktikum arbeitet ihr mit realen Messdaten, die auf dem Dach des Gebäudes N5 an der Technischen Universität München aufgenommen wurden. Die verwendeten Sensoren befinden sich in wettergeschützten und temperaturstabilisierten Außenboxen. Dabei wird Luft über einen Schlauch von einem externen Lufteinlass kontinuierlich in das Messsystem gepumpt.

<img src="pictures/systems.jpeg" alt="Systems" width="300" height="200">
<img src="pictures/air_intakes.jpeg" alt="Systems" width="300" height="200">

## Lernziele

Verarbeitung von In-situ-$CO_2$-Sensordaten:

- Kalibrationskorrektur (**Calibration Correction**)
- Zeitliche Aggregation und Qualitätsmetriken (**Time Aggregation & Performance Metrics**)
- Sensitivitätsanalyse der $CO_2$-Sensoren (**Sensor Sensitivity**)
- Korrektur der Messwerte von feuchter auf trockene Luft (**Dilution Correction**)

## Vorbereitung zumn Praktikum

1.	Grundlagen verstehen

Bitte schaue dir zur Vorbereitung die beiden verlinkten Videos über das ideale [Ideal Gas Law](https://youtu.be/BxUS1K7xu30?si=f3rDpXa9sT9PRdz9) sowie den [Partialdruck](https://youtu.be/JbqtqCunYzA?si=UgNx84xJpQUcYKGu) an, um die theoretischen Grundlagen zu vertiefen. Bei Bedarf können in beiden Videos deutsche Untertitel aktiviert werden.

2.	Technische Vorbereitung (optional)

Falls du mit deinem eigenen Laptop arbeiten möchtest, klone bitte im Vorfeld das bereitgestellte Repository, richte die virtuelle Python-Umgebung ein und installiere die erforderlichen Libraries.

#### **Voraussetzungen**

- [Installiere VS Code](https://code.visualstudio.com/Download) + [Extension für Jupyter](https://www.youtube.com/watch?v=suAkMeWJ1yE)
- Python **3.13 or later**
- Poetry (`pip install poetry`)

#### **Einrichtung Virtuelle Umgebung + Installation Libraries**

```bash
python3.13 -m venv .venv  # Create virtual environment
source .venv/bin/activate  # Activate it
poetry install  # Install dependencies
```
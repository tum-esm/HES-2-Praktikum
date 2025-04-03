# HES-2-Praktikum

## Messstation TUM N5 Dach

Ihr arbeitet mit echten Daten, die auf dem Dach des N5 Gebäudes an der TUM gemessen wurden.

<img src="pictures/systems.jpeg" alt="Systems" width="300" height="200">
<img src="pictures/air_intakes.jpeg" alt="Systems" width="300" height="200">

## Lernziele

Postprocessing von In-Situ Sensordaten: 

- Calibration Correction, 
- Time Aggregation,
- Performance Metrics
- Sensor Sensitivität
- Dilution Correction 

## Vorbereitung zumn Praktikum

1. Schaue die zwei verlinkten Videos, um das [Ideal Gas Law](https://youtu.be/BxUS1K7xu30?si=f3rDpXa9sT9PRdz9) und den [Partialdruck](https://youtu.be/JbqtqCunYzA?si=UgNx84xJpQUcYKGu) grob zu verstehen. In beiden Videos können deutsche Untertitel aktiviert werden, falls notwendig.

2. Falls du deinen eigenen Laptop nutzen willst, klone dir das Repository und installiere die virtuelle Umgebung und die Python Libraries vorab.


### **Prerequisites**

- [Install VS Code](https://code.visualstudio.com/Download) + [Extension für Jupyter](https://www.youtube.com/watch?v=suAkMeWJ1yE)
- Python **3.13 or later**
- Poetry installed (`pip install poetry`)

### **Set up the virtual environment and install dependencies**

```bash
python3.13 -m venv .venv  # Create virtual environment
source .venv/bin/activate  # Activate it
poetry install  # Install dependencies
```
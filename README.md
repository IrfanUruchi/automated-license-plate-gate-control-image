# Automated License Plate Gate Control

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24434566.svg)](https://doi.org/10.5281/zenodo.24434566)

A CPU-based automatic license plate recognition (ALPR) system for
on-premises vehicle access control using Raspberry Pi and Arduino.

**Author:** Irfan Uruchi  
**Institution:** South East European University  
**Original project:** May 2025  
**Research publication:** November 22, 2026  
**ORCID:** [0009-0000-9036-8172](https://orcid.org/0009-0000-9036-8172)

---

## Overview

This project implements an embedded vehicle access-control system
combining YOLOv8n vehicle detection, EasyOCR text recognition,
local authorization, serial communication, and persistent event logging.

The Raspberry Pi handles image acquisition, inference, recognition,
and access decisions. An Arduino UNO R3 provides physical access-state
indications through USB serial communication.

The recognition pipeline operates locally using CPU inference,
without requiring a dedicated GPU or cloud-based recognition service.

## System Architecture

The recognition and authorization pipeline follows this sequence:

```text
Camera Input
     |
YOLOv8n Vehicle Detection
     |
Vehicle Region Extraction
     |
EasyOCR Text Recognition
     |
License Plate Authorization
     |
     +--- Arduino / Access-State Indication
     |
     +--- SQLite Event Logging
```

Authorized registration numbers are maintained in a local YAML
configuration file.

## Main Components

| Component | Technology |
|---|---|
| Edge computing | Raspberry Pi 4B |
| Embedded control | Arduino UNO R3 |
| Vehicle detection | YOLOv8n |
| Text recognition | EasyOCR |
| Authorization | YAML |
| Event storage | SQLite |
| Hardware communication | USB serial |
| Deployment | Docker |
| Programming languages | Python, C++ |

## Repository Structure

```text
app/
├── access.py
├── arduino_led.py
├── capture.py
├── db.py
├── detect.py
├── gpio_out.py
├── main.py
└── ocr.py

config/
└── whitelist.yaml

data/
└── access.db

models/
└── yolov8n.pt

Dockerfile
quick_test.py
README.md
```

The repository contains the application modules, configuration files,
model assets, inference utility, and Docker deployment configuration.

## Installation

### Requirements

- Raspberry Pi OS (64-bit)
- Python 3.11 for native execution
- Docker for containerized deployment
- Compatible USB or network camera
- Arduino UNO R3 for serial-based access-state indication
- Git LFS for retrieving model assets where applicable

### Native Installation

Clone the repository:

```bash
git clone https://github.com/IrfanUruchi/automated-license-plate-gate-control.git
cd automated-license-plate-gate-control
```

Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the dependencies using the repository's requirements file.

Retrieve model assets managed through Git LFS:

```bash
git lfs install
git lfs pull
```

Configure the camera source, authorization file, and hardware
communication settings before launching the application entry point
in `app/main.py`.

## Docker Deployment

The container image is available on Docker Hub:

[irfanuruchi/alpr-gate-pi](https://hub.docker.com/r/irfanuruchi/alpr-gate-pi)

Select an available image tag from Docker Hub.

```bash
docker pull irfanuruchi/alpr-gate-pi:<tag>
```

Example deployment using a locally connected USB camera:

```bash
docker run -d \
  --name alpr-gate-pi \
  --device /dev/video0:/dev/video0 \
  -v "$(pwd)/config:/app/config" \
  -v "$(pwd)/data:/app/data" \
  irfanuruchi/alpr-gate-pi:<tag>
```

Replace `<tag>` with the selected image tag.

Arduino serial devices must also be exposed to the container
when serial-based hardware control is enabled.

Network camera deployments require the corresponding camera
source configuration.

## Configuration

The local authorization list is stored in:

```text
config/whitelist.yaml
```

Configure the authorized registration numbers before starting
the application.

For network cameras, static IP addresses or DHCP reservations
are recommended to maintain a consistent camera endpoint.

Production authorization lists, captured registration numbers,
and operational access logs should remain outside public
version control.

## Model Assets

The recognition pipeline uses YOLOv8n for vehicle detection
and EasyOCR for text recognition.

The repository includes PyTorch model weights and a TorchScript
export for the detection stage.

The current implementation performs OCR on detected vehicle
regions rather than using a dedicated license plate detector.

## Testing and Evaluation

The `quick_test.py` utility provides a single-image inference
test for inspecting recognition output.

The associated research manuscript documents the physical
prototype, recognition pipeline, hardware integration,
processing latency, and event logging.

Individual detector inference times observed during the
prototype demonstration ranged from approximately
0.828 to 0.948 seconds.

These measurements represent detector inference rather than
complete end-to-end access-decision latency.

## Research Publication

**CPU-Based Automatic License Plate Recognition for On-Premises
Access Control Using Raspberry Pi and Arduino**

The research manuscript describes the system architecture,
implementation, experimental observations, hardware integration,
limitations, and future development directions.

- Author: Irfan Uruchi
- Publication date: November 22, 2026
- Publication type: Preprint
- Repository: Zenodo
- DOI: [10.5281/zenodo.24434566](https://doi.org/10.5281/zenodo.24434566)

[Read the full research paper](https://doi.org/10.5281/zenodo.24434566)

## Citation

If you use this research or its implementation, please cite
the associated preprint:

Uruchi, I. (2026). *CPU-Based Automatic License Plate Recognition
for On-Premises Access Control Using Raspberry Pi and Arduino*.
Zenodo. https://doi.org/10.5281/zenodo.24434566

```bibtex
@misc{uruchi2026alpr,
  author       = {Uruchi, Irfan},
  title        = {CPU-Based Automatic License Plate Recognition
                  for On-Premises Access Control Using
                  Raspberry Pi and Arduino},
  year         = {2026},
  month        = {nov},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.24434566},
  url          = {https://doi.org/10.5281/zenodo.24434566},
  note         = {Preprint}
}
```

Machine-readable citation metadata is provided in `CITATION.cff`.

## License

The original project source code is released under the MIT License.

The research manuscript is distributed under the Creative Commons
Attribution 4.0 International (CC BY 4.0) license.

Third-party models and dependencies remain subject to their
respective licenses.

## Author

**Irfan Uruchi**  
Computer Engineer

[GitHub](https://github.com/IrfanUruchi) |
[ORCID](https://orcid.org/0009-0000-9036-8172) |
[Research Publication](https://doi.org/10.5281/zenodo.24434566)

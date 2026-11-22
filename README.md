# Automated License Plate Gate Control

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24434566.svg)](https://doi.org/10.5281/zenodo.24434566)

A CPU-based automatic license plate recognition (ALPR) system for on-premises vehicle access control using Raspberry Pi and Arduino.

**Author:** Irfan Uruchi  
**Institution:** South East European University  
**Original project:** May 2025  
**Preprint publication:** November 22, 2026  
**ORCID:** [0009-0000-9036-8172](https://orcid.org/0009-0000-9036-8172)

---

## Overview

This project implements a local vehicle access-control system using computer vision, optical character recognition, and embedded hardware.

A Raspberry Pi 4B performs vehicle detection using YOLOv8n, extracts registration information using EasyOCR, and determines access authorization against a local whitelist. An Arduino UNO R3 receives access decisions through USB serial communication, while SQLite maintains persistent event records.

The recognition pipeline operates entirely on the CPU, without requiring a dedicated GPU or cloud-based recognition service.

## System Architecture

```text
Camera
  │
  ▼
Raspberry Pi 4B
  │
  ├── Image acquisition
  ├── YOLOv8n vehicle detection
  ├── Vehicle region extraction
  ├── EasyOCR text recognition
  └── Authorization decision
        │
        ├── USB Serial ──► Arduino UNO R3
        │                   └── Access-state indication
        │
        └── SQLite ──────► Persistent event records
```

The current implementation applies optical character recognition to detected vehicle regions rather than employing a separate license plate localization model.

## Hardware and Software

| Component | Technology |
|---|---|
| Edge computing | Raspberry Pi 4B |
| Microcontroller | Arduino UNO R3 |
| Vehicle detection | YOLOv8n |
| Optical character recognition | EasyOCR |
| Inference runtime | PyTorch / TorchScript |
| Authorization | YAML |
| Database | SQLite |
| Hardware communication | USB serial |
| Deployment | Docker |
| Languages | Python, C++ |

## Repository Structure

```text
automated-license-plate-gate-control-image/
├── smart-access-indicator/
│   ├── app/
│   │   ├── access.py
│   │   ├── arduino_led.py
│   │   ├── capture.py
│   │   ├── db.py
│   │   ├── detect.py
│   │   ├── gpio_out.py
│   │   ├── main.py
│   │   └── ocr.py
│   ├── config/
│   │   └── whitelist.yaml
│   ├── data/
│   │   └── access.db
│   ├── models/
│   │   └── yolov8n.pt
│   ├── Dockerfile
│   ├── quick_test.py
│   ├── requirements.txt
│   └── yolov8n.torchscript
└── README.md
```

### Application Modules

| Module | Responsibility |
|---|---|
| `access.py` | Registration authorization |
| `arduino_led.py` | Arduino serial communication |
| `capture.py` | Camera input and frame acquisition |
| `db.py` | SQLite event storage |
| `detect.py` | Vehicle detection |
| `gpio_out.py` | GPIO output handling |
| `main.py` | Application entry point |
| `ocr.py` | Optical character recognition |

## Installation

### Requirements

- Raspberry Pi OS (64-bit)
- Python 3.11 for native execution
- Docker for containerized execution
- Compatible USB or network camera
- Arduino UNO R3 for serial-based hardware control
- Git LFS where required for model assets

### Native Installation

Clone the repository and enter the application directory:

```bash
git clone https://github.com/IrfanUruchi/automated-license-plate-gate-control-image.git
cd automated-license-plate-gate-control-image/smart-access-indicator
```

Create the Python environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Retrieve any model assets stored through Git LFS:

```bash
git lfs install
git lfs pull
```

Configure the camera source, authorization list, and hardware communication settings before running the application through its entry point, `app/main.py`.

## Docker Deployment

The prebuilt container image is available on Docker Hub:

[irfanuruchi/alpr-gate-pi](https://hub.docker.com/r/irfanuruchi/alpr-gate-pi)

Select an available image tag:

```bash
docker pull irfanuruchi/alpr-gate-pi:<tag>
```

Run the following example from the `smart-access-indicator/` directory for a locally connected USB camera:

```bash
docker run -d \
  --name alpr-gate-pi \
  --device /dev/video0:/dev/video0 \
  -v "$(pwd)/config:/app/config" \
  -v "$(pwd)/data:/app/data" \
  irfanuruchi/alpr-gate-pi:<tag>
```

Replace `<tag>` with the appropriate published image tag.

Serial-based Arduino control requires the corresponding host serial device to be exposed to the container.

For network cameras, configure the appropriate camera endpoint in the application.

## Configuration

Application configuration and runtime assets are located within `smart-access-indicator/`.

| Path | Purpose |
|---|---|
| `config/whitelist.yaml` | Authorized vehicle registrations |
| `data/access.db` | Persistent access-event database |
| `models/yolov8n.pt` | PyTorch detection weights |
| `yolov8n.torchscript` | TorchScript detection model |

Network cameras should use stable IP addresses or DHCP reservations.

Real vehicle registrations, production authorization lists, and operational access records should not be committed to public version control.

## Evaluation

The `quick_test.py` utility provides single-image inference for inspecting recognition output.

The research manuscript documents the implemented single-lane prototype, including:

- CPU-based vehicle detection and text recognition.
- Local authorization and access decisions.
- Raspberry Pi and Arduino integration.
- Processing latency.
- Persistent SQLite event logging.

Individual detector inference times observed during the prototype demonstration ranged from approximately 0.828 to 0.948 seconds. These measurements represent detector inference time rather than complete end-to-end access-decision latency.

The manuscript discusses the experimental results, evaluation methodology, implementation limitations, and potential extensions to the system.

## Research Publication

### CPU-Based Automatic License Plate Recognition for On-Premises Access Control Using Raspberry Pi and Arduino

| Publication details | |
|---|---|
| Author | Irfan Uruchi |
| Publication type | Preprint |
| Publication date | November 22, 2026 |
| Publisher | Zenodo |
| License | CC BY 4.0 |
| DOI | [10.5281/zenodo.24434566](https://doi.org/10.5281/zenodo.24434566) |

The paper presents the system architecture, recognition pipeline, hardware implementation, experimental observations, and future research directions.

[Read the full research paper](https://doi.org/10.5281/zenodo.24434566)

## Citation

If you use this research or its implementation, please cite the associated preprint.

Uruchi, I. (2026). *CPU-Based Automatic License Plate Recognition for On-Premises Access Control Using Raspberry Pi and Arduino*. Zenodo. https://doi.org/10.5281/zenodo.24434566

### BibTeX

```bibtex
@misc{uruchi2026alpr,
  author    = {Uruchi, Irfan},
  title     = {CPU-Based Automatic License Plate Recognition for
               On-Premises Access Control Using Raspberry Pi and Arduino},
  year      = {2026},
  month     = nov,
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24434566},
  url       = {https://doi.org/10.5281/zenodo.24434566},
  note      = {Preprint}
}
```

Machine-readable citation metadata is provided in `CITATION.cff`.

## License

The original project source code is released under the MIT License.

The research manuscript is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

Third-party models and dependencies remain subject to their respective licenses.

## Author

**Irfan Uruchi**  
Computer Engineer

[GitHub](https://github.com/IrfanUruchi) ·
[ORCID](https://orcid.org/0009-0000-9036-8172) ·
[Research Publication](https://doi.org/10.5281/zenodo.24434566)

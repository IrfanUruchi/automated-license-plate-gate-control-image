# automated-license-plate-gate-control-image

**Edge-based ALPR pipeline for Raspberry Pi**, combining YOLOv8 Nano and EasyOCR in a Docker-ready package.

## 📂 Repository Structure

alpr-gate-pi-data/
├── app/    
│   ├── init.py
│   ├── access.py
│   ├── arduino_led.py
│   ├── capture.py
│   ├── db.py
│   ├── detect.py
│   ├── gpio_out.py   
│   ├── main.py             
│   └── ocr.py       
├── config          
│   └── whitelist.yaml 
├── data         
│   └── access.db
├── Dockerfile  
├── models         
│   └── yolov8n.pt
├── quick_test.py  
├── requriments.txt        
├── yolov8n.torchscript       
└── README.md     


## 🚀 Quickstart

### 1. Prerequests

- **Raspberry Pi OS (64-bit)**, Docker & Docker Buildx installed  
- Python 3.11 (if running natively)

### 2 One command install

You can either download the repo for all files or go via the Docker image for a one command installation process.

If you want to install with one Docker command [Link for Docker Image](https://hub.docker.com/r/irfanuruchi/alpr-gate-pi)


### 2.1 Clone & Install


Or you can download this repo
```bash

git clone https://github.com/irfanuruchi/smart-access-indicator.git
cd smart-access-indicator
```

Setup your environment (assuming you have Python installed

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Check first for updates
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Then get the model weight and everything (preferably to have also LFS but i think even without it will work): 
```
git lfs install
git lfs pull
```

Now you can run locally  with simple Python command to launch the main.py

### 2.2 Docker Usage

```bash
docker pull irfanuruchi/alpr-gate-pi:tagname
```

and then just run it with 

```bash
docker run -d \
  --device /dev/video0:/dev/video0 \
  -v $(pwd)/config:/app/config \
  irfanuruchi/alpr-gate-pi:tagname
```

Make sure you have a device connected first and then run the command

## Configuration

You can modify the config/whitelist.yaml file to the plates

## Models

PyTorch weights: models/yolov8n.pt

TorchScript export: models/yolov8n.torchscript

## Testing & Metrics

quick_test.py runs inference on a single image and prints detected plates with confidence scores.

Be sure to configure the files for your IP cameras and for better reliablity make the IP cameras static.

## License
This project is licensed under the MIT License.


Maintained by @irfanuruchi

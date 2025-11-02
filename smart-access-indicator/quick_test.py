#!/usr/bin/env python3
"""
quick_test.py  –  one-shot detector + OCR printout
Run:  python quick_test.py
Stop: Ctrl-C
"""

import cv2, time, easyocr
from ultralytics import YOLO

RTSP_URL = 'rtsp://172.20.10.13:8080/h264_pcm.sdp'   # ← change if needed
IMG_SZ   = 640
CONF_TH  = 0.15      # lower threshold so we see boxes even at a distance

def main():
    print("Loading YOLOv8 Nano …")
    model  = YOLO('models/yolov8n.pt')
    reader = easyocr.Reader(['en'], gpu=False)

    cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        raise RuntimeError("❌ Stream not available")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("⚠️ Lost RTSP frame, retrying")
            time.sleep(1)
            continue

        t0 = time.time()
        res = model(frame, imgsz=IMG_SZ, conf=CONF_TH)[0]
        print(f"YOLO boxes: {len(res.boxes)}  ({time.time()-t0:.2f} s)")

        for i, box in enumerate(res.boxes, 1):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            roi = frame[y1:y2, x1:x2]
            text = ''.join(reader.readtext(roi, detail=0)).strip().upper()
            print(f" • Box {i:02}: “{text}”")
        print("-" * 40)
        time.sleep(1)          # throttle output; remove if you want a stream

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")

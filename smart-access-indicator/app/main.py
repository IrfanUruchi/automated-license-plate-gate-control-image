# app/main.py
import time
from .db import log_event              

from .capture     import FrameGrabber
from .detect      import VehicleDetector
from .ocr         import plate_text
from .access      import AccessControl
from .gpio_out    import signal        

RTSP_URL = 'rtsp://172.20.10.13:8080/h264_pcm.sdp'


def run():
    grab = FrameGrabber(RTSP_URL, width=640, height=480)
    yolo = VehicleDetector(model_path='models/yolov8n.pt')
    gate = AccessControl()

    try:
        while True:
            frame = grab.read()
            t0 = time.time()

            for box in yolo.detect(frame):
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                crop  = frame[y1:y2, x1:x2]
                plate = plate_text(crop)
                print("DBG raw OCR →", repr(plate)) 
                if not plate:
                    continue

                status = 'GRANTED' if gate.allowed(plate) else 'DENIED'
                signal(status)                          
                log_event(plate, status)               

                fps = 1 / (time.time() - t0)
                print(f'{plate:<10} → {status}   {fps:.1f} fps')

    except KeyboardInterrupt:
        print('\nStopping…')
    finally:
        grab.release()
        signal('DENIED')          


if __name__ == '__main__':
    run()



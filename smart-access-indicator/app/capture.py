# app/capture.py
import cv2


class FrameGrabber:
    """Lightweight RTSP frame reader for Raspberry Pi."""
    def __init__(self, rtsp_url: str, width=640, height=480):
        self.cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open stream {rtsp_url}")

    def read(self):
        ok, frame = self.cap.read()
        if not ok:
            raise RuntimeError("⚠️  Lost RTSP stream")
        return frame

    def release(self):
        self.cap.release()

# app/ocr.py
import cv2
import easyocr

_reader = None           # loaded lazily, so main loop starts fast


def _get_reader():
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(['en'])    # loads English charset
    return _reader


def plate_text(bgr_roi):
    """
    Try to return a cleaned-up plate string from a BGR image patch.
    Returns '' if nothing plausible found.
    """
    gray = cv2.cvtColor(bgr_roi, cv2.COLOR_BGR2GRAY)

    # adaptive threshold helps at night / shadows
    thr = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV, 15, 7
    )

    # OCR
    result = _get_reader().readtext(thr, detail=0, paragraph=False)

    if not result:
        return ''

    txt = ''.join(result).upper().replace(' ', '')
    # very rough sanity filter: must contain ≥5 alphanumerics
    return txt if sum(c.isalnum() for c in txt) >= 5 else ''

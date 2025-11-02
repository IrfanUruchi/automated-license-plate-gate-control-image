import serial, os, time

DEV = os.getenv('ARDU_PORT', '/dev/ttyACM0')
ser = serial.Serial(DEV, 115200, timeout=1)

def show(state: str):
    """
    state ∈ {'SCANNING','GRANTED','DENIED'}
    """
    code = {'SCANNING': b'Y',
            'GRANTED' : b'G',
            'DENIED'  : b'R'}.get(state, b'R')
    try:
        ser.write(code)
    except serial.SerialException:
        pass          

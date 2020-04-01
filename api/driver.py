import glob
import sys
import subprocess
import serial


def install(package):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-U", package])


STREAM = None
SPEEDS = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']


def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    ports = []
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    for device in result:
        if ('serial' in device) or ('USB' in device):
            tmp = device;
            result.remove(device)
            result.insert(0, tmp)
            break
    return result


def startup(dev = '', speed = '9600'):
    """ Инцализация подключения к устройству.

    Параметры:
    dev:str -- порт устройства str
    string:str

    возвращает int (1 - успех, -1 - ошибка)

    """
    if dev is None or dev == '':
        ports = serial_ports()
        if len(ports) == 0:
            return -1
        else:
            dev = ports[0]
    global STREAM

    STREAM = serial.Serial(port=dev, baudrate=speed)
    return 1


def read_line():
    global STREAM
    return STREAM.readline().decode("utf-8")[:-1]


def get_port():
    global STREAM
    return STREAM._port


def close():
    global STREAM
    STREAM.close()
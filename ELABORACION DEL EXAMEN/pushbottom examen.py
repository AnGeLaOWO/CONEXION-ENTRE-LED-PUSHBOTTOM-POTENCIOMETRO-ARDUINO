import pyfirmata
import time

board = pyfirmata.Arduino('COM6')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[4].mode = pyfirmata.INPUT

pinLedPot = 11     # Pin del led que usarán para el potenciómetro
board.analog[0].enable_reporting()

for x in range(3):
    board.digital[pinLedPot].write(1)
    time.sleep(0.5)
    board.digital[pinLedPot].write(0)
    time.sleep(0.5)

analogPot = board.get_pin('a:0:i')     # En vez del 0 ponen el pin analógico del potenciometro
led = board.get_pin('d:11:p')      # En vez del 11 ponen el pin del led que se usará con el potenciómetro

while True:
    analog = analogPot.read()
    led.write(analog)
    sw = board.digital[4].read()
    if sw is True:
        board.digital[12].write(1)
    else:
        board.digital[12].write(0)
    time.sleep(0.1)
        

    

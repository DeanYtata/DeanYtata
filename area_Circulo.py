
from xml.etree.ElementTree import PI


def areacirculo():
    radio=float(input("ingrese el valor del radio: "))
    pi=3.1416
    print("el area del circulo es...", pi*radio**2) 
    
areacirculo()
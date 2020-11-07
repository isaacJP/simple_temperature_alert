from gpiozero import CPUTemperature
from time import sleep, strftime, time
import pygame

class Temp:
        def __init__(self):
                # Pygame library for load and play MP3 file
                pygame.mixer.init()
                pygame.mixer.music.load("beep-02.mp3")
                pygame.mixer.music.set_volume(1.0)
                
                self.cpu = CPUTemperature()

        def start(self):
                while True:
                        temp = self.cpu.temperature
                        # Alert temperature range in 60ºC
                        if temp >= 60:
                                pygame.mixer.music.play(loops=-1)
                        else:
                                pygame.mixer.music.stop()
                        sleep(2)


temp_monitor = Temp()
temp_monitr.start()

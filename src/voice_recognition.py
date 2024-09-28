import speech_recognition as sr
import threading
import time

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        try:
            self.microphone = sr.Microphone()
        except:
            self.microphone = None
        self.enabled = False
        self.output = ""

    def toggle(self):
        self.enabled = not self.enabled
        if self.enabled:
            threading.Thread(target=self.listen).start()

    def listen(self):
        while self.enabled:
            with self.microphone as source:
                try:
                    audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    self.output = self.recognizer.recognize_google(audio, language="es-ES")
                except sr.WaitTimeoutError:
                    # If no speech was detected within the timeout, continue without crashing
                    print("Timeout reached, no speech detected.")
                    continue      
                except sr.UnknownValueError:
                    self.output =  "ERROR: No se pudo reconocer el audio"
                    continue
                except sr.RequestError as e:
                    self.output = "ERROR: " + str(e)
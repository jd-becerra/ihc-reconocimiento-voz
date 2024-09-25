import speech_recognition as sr
import threading

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.enabled = False
        self.output = ""

    def toggle(self):
        self.enabled = not self.enabled
        if self.enabled:
            threading.Thread(target=self.listen).start()

    def listen(self):
        output = ""

        with self.microphone as source:
            print("Di algo:")
            audio = self.recognizer.listen(source)
            try:
                self.output = self.recognizer.recognize_google(audio, language="es-ES")
            except sr.UnknownValueError:
                self.output =  "ERROR: No se pudo reconocer el audio"
            except sr.RequestError as e:
                self.output = "ERROR: " + str(e)
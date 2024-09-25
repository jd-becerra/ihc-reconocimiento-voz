import speech_recognition as sr

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        output = ""

        with self.microphone as source:
            print("Di algo:")
            audio = self.recognizer.listen(source)
            try:
                output = self.recognizer.recognize_google(audio, language="es-ES")
                return output
            except sr.UnknownValueError:
                print("No se pudo reconocer el audio")
                return "ERROR: No se pudo reconocer el audio"
            except sr.RequestError as e:
                return "ERROR: " + str(e)
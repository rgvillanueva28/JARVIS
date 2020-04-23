import speech_recognition as sr

class VoiceRecognition():

    def __init__(self):
        self.voiceRecognizer = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            try:
                self.voiceRecognizer.adjust_for_ambient_noise(source)
                audio = self.voiceRecognizer.listen(source, timeout=2)
                text = self.voiceRecognizer.recognize_google(audio)
                return text
            except AttributeError as ex:
                return "Error. " + ex
            except sr.WaitTimeoutError as ex:
                return "Error. " + str(ex)
            except sr.UnknownValueError as ex:
                return "Error. Couldn't understand" + str(ex)
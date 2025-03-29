import speech_recognition as sr
from config.settings import settings


class AudioProcessor:
    def init(self):
        self.recognizer = sr.Recognizer()

    def audio_to_text(self, audio_data):
        """
        Конвертирует аудио данные в текст
        """
        try:
            # Используем Google Speech Recognition
            text = self.recognizer.recognize_google(audio_data, language="ru-RU")
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Speech Recognition service; {e}")
            return ""
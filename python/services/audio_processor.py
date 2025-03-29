import os

import speech_recognition as sr
from pydub import AudioSegment
from speech_recognition import AudioData


class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self._setup_recognizer()

    def _setup_recognizer(self):
        """Настройка параметров распознавания"""
        self.recognizer.energy_threshold = 400
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5

    def audio_to_text(self, audio_path, chunk_size=10000):
        """
        Конвертирует аудио файл в текст, разбивая его на части
        """
        if audio_path.endswith(".mp3"):
            audio_path = self.convert_mp3_to_wav(audio_path)

        audio = AudioSegment.from_wav(audio_path)
        text = ""

        # Разбиваем аудиофайл на части по chunk_size миллисекунд
        for i in range(0, len(audio), chunk_size):
            chunk = audio[max(0, i-2000):i + chunk_size]
            chunk.export("temp_chunk.wav", format="wav")

            with sr.AudioFile("temp_chunk.wav") as source:
                audio_data = self.recognizer.record(source)
                try:
                    # Используем Google Speech Recognition
                    temp  = self.recognizer.recognize_google(audio_data, language="ru-RU")
                    print(f"{i/1000}:{(i+chunk_size)/1000} - {temp}")
                    text += " " + temp
                except sr.UnknownValueError:
                    print("Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Speech Recognition service; {e}")

        # Удаляем временный файл
        os.remove("temp_chunk.wav")

        return text.strip()

    def convert_mp3_to_wav(self, mp3_path):
        """
        Конвертирует MP3 файл в WAV формат
        """
        audio = AudioSegment.from_mp3(mp3_path)
        wav_path = mp3_path.replace(".mp3", ".wav")
        audio.export(wav_path, format="wav")
        return wav_path
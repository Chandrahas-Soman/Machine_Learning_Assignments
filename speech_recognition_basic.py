# speech_recognition_version0
import cmu_sphinx

# reading an audio file
audio_URL = "some_URL/audio.wav"
transcriber = cmu_sphinx.Transcriber(audio_URL)

#printing it
for line in transcriber.transcript_stream():
	print line
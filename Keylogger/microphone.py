import sounddevice as sd
from scipy.io.wavfile import write

microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3

# Function to record microphone
def record_microphone(file_path):
    fs = 44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    with open(file_path + "/f_microphone.wav", "wb") as f:
        write(f, fs, myrecording)

import sounddevice as sd  # Import the module for audio recording and playback
from scipy.io.wavfile import write  # Import the module for writing WAV files

microphone_time = 10  # Duration of microphone recording in seconds
time_iteration = 15  # Time interval between microphone recordings in seconds
number_of_iterations_end = 3  # Number of microphone recording iterations

# Function to record microphone
def record_microphone(file_path):
    fs = 44100  # Sample rate for the audio recording (44100 Hz is the standard for most applications)
    seconds = microphone_time  # Duration of the recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)  # Start the recording using sounddevice module
    sd.wait()  # Wait for the recording to complete

    with open(file_path + "/f_microphone.wav", "wb") as f:
        write(f, fs, myrecording)  # Write the recorded audio data to a WAV file

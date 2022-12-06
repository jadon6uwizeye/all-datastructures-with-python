# a program under Python allowing to generate a son signal (the sampling frequency will be fixed at 44100𝐻𝑧).
# For the generation of a son over a given duration, you can generate a time vector with the command t = np.linspace(0, duration, duration * Fe). 𝐹𝑒 being the number of samples per second. A duration of one second (duration = 1s) is sufficient for the realization of this deliverable.
# choose about ten significant frequencies in the audible spectrum. For each of these frequencies:
# Save the audio signal in a file in (son.wav) format

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav  
import pyaudio

# generate a son signal (the sampling frequency will be fixed at 44100𝐻𝑧).
def generate_son(duration, frequency, amplitude, sampling_frequency):
    # Generate a time vector
    t = np.linspace(0, duration, duration * sampling_frequency)
    # Generate a son signal
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return y

# Main function
def main():
    # Generate son signals ten significant frequencies in the audible spectrum
    y1 = generate_son(1, 20, 1, 44100)
    y2 = generate_son(1, 2000, 1, 44100)
    y3 = generate_son(1, 4000, 1, 44100)   
    y4 = generate_son(1, 6000, 1, 44100)
    y5 = generate_son(1, 8000, 1, 44100)
    y6 = generate_son(1, 10000, 1, 44100)
    y7 = generate_son(1, 12000, 1, 44100)
    y8 = generate_son(1, 14000, 1, 44100)
    y9 = generate_son(1, 16000, 1, 44100)
    y10 = generate_son(1, 18000, 1, 44100)
    # Save the audio signal in a file in (son.wav) format
    wav.write('son1.wav', 44100, y1)
    wav.write('son2.wav', 44100, y2)
    wav.write('son3.wav', 44100, y3)
    wav.write('son4.wav', 44100, y4)
    wav.write('son5.wav', 44100, y5)
    wav.write('son6.wav', 44100, y6)
    wav.write('son7.wav', 44100, y7)
    wav.write('son8.wav', 44100, y8)
    wav.write('son9.wav', 44100, y9)
    wav.write('son10.wav', 44100, y10)


    # Play the audio signal using pyaudio
    # play_son(y3, 44100)

if __name__ == "__main__":
    main()

import pyaudio
import matplotlib.pyplot as plt
import numpy as np

N = 1024
rate = 44100
dt = 1/rate

def audiostart():
    audio = pyaudio.PyAudio()
    stream = audio.open( format = pyaudio.paInt16,
        rate = rate,
        channels = 1,
        input_device_index = 1,
        input = True,
        frames_per_buffer = N)
    return audio, stream

def audiostop(audio, stream):
    stream.stop_stream()
    stream.close()
    audio.terminate()

def read_plot_data(stream):
    data = stream.read(N)
    data  = np.frombuffer(data, dtype='int16')
    fft = np.fft.fft(data)
    freq = np.fft.fftfreq(N, d=dt)
    amp = np.abs(fft/(N/2))

    plt.plot(freq[1:int(N/2)], amp[1:int(N/2)])
    plt.draw()
    plt.pause(0.1)
    plt.cla()

if __name__ == '__main__':
    (audio,stream) = audiostart()
    while True:
        try:
            read_plot_data(stream)
        except KeyboardInterrupt:
            break
    audiostop(audio,stream)


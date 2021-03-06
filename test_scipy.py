import scipy.signal
import numpy as np
import utils

def stft(x, n_fft=2048, n_hopsize=1024, window='hann'):
    f, t, X = scipy.signal.stft(
        x, 
        nperseg=n_fft, 
        noverlap=n_fft - n_hopsize, 
        window=window,
        padded=True,
    )
    return X * (n_fft / 2)


def istft(X, rate=44100, n_fft=2048, n_hopsize=1024, window='hann'):
    t, audio = scipy.signal.istft(
        X / (n_fft / 2),
        rate, 
        nperseg=n_fft, 
        noverlap=n_fft - n_hopsize, 
        window=window,
        boundary=True
    )
    return audio


def spectrogram(X, power):
    return np.abs(X)**power


if __name__ == "__main__":
    s = utils.sine()
#    s = np.stack([s, s, s, s])
    X = stft(s)
    x = istft(X, rate=44100)
#    print(s)
#    print(x)
    print(utils.rms(s, x))

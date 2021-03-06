import librosa
import numpy as np
import utils

def stft(x, n_fft=2048, n_hopsize=1024, center=True, window='hann', dtype=np.complex64):
    return librosa.core.stft(x, n_fft=n_fft,
        hop_length=n_hopsize,
        center=center,
        window=window,
        dtype=dtype)


def istft(X, n_fft=2048, n_hopsize=1024, center=True, window='hann', dtype=np.float32):
    return librosa.core.istft(X,
        hop_length=n_hopsize,
        center=center,
        window=window,
        dtype=dtype)


def spectrogram(X, power):
    return np.abs(X)**power


if __name__ == "__main__":
    s = utils.sine()
#    s = np.stack([s, s, s, s])
    X = stft(s)
    x = istft(X)
#    print(s)
#    print(x)
    print(utils.rms(s, x))

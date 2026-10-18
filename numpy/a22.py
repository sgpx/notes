##Next Topic:## Learn about ##NumPy's Fourier Transform## and its applications in signal processing.

##Practical Challenge:## Write a function that takes a 1D NumPy array (representing a signal) and computes its Fast Fourier Transform (FFT) and the corresponding frequencies. Visualize both the original signal and its frequency spectrum using Matplotlib.

##What to Learn:## Familiarize yourself with `numpy.fft.fft()` for computing FFT and `numpy.fft.fftfreq()` for obtaining the frequencies. You can also learn basic plotting using Matplotlib to visualize your results.

import numpy as np
signal = [1, 2, 3, 4]
fft_result = np.fft.fft(signal)
print(fft_result)



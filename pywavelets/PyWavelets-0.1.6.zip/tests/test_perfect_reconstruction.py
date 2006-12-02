#!/usr/bin/env python

"""
Verify DWT perfect reconstruction.
"""
    
import math
import numpy
import pywt
from numpy import asarray, float64

def mse(ar1, ar2):
    """Mean squared error"""
    ar1 = asarray(ar1, dtype=float64)
    ar2 = asarray(ar2, dtype=float64)
    dif = ar1 - ar2
    dif *= dif
    return dif.sum()/len(ar1)

def rms(ar1, ar2):
    """Root mean squared error"""
    return math.sqrt(mse(ar1, ar2))

def test_perfect_reconstruction(families, wavelets, modes, epsilon):
    print "Testing perfect reconstruction".upper()
    for pmode, mmode in modes:
        for wavelet in wavelets:
            print "Wavelet: %-8s Mode: %s" % (wavelet, pmode),
        
            w = pywt.Wavelet(wavelet)
            data_size = range(2, 40) + [100, 200, 500, 1000, 2000, 10000, 50000, 100000]
            
            ok, over = 0, 0
            for N in data_size:
                data = numpy.random.random(N)
                
                # compute dwt coefficients
                pa, pd = pywt.dwt(data, wavelet, pmode)
                
                # compute reconstruction
                rec = pywt.idwt(pa, pd, wavelet, pmode)

                if len(data) % 2:
                    rec = rec[:len(data)]
                    
                rms_rec = rms(data, rec)
                if rms_rec > epsilon:
                    if not over:
                        print
                    print '[RMS_REC > EPSILON] for Mode: %s, Wavelet: %s, Length: %d, rms=%.3g' % (pmode, wavelet, len(data), rms_rec, )
                    over += 1
                else:
                    ok += 1
            if not over:
                print "- RMSE for all %d cases was under %s" % (len(data_size), epsilon)

if __name__ == '__main__':
    
    families = ('db', 'sym', 'coif', 'bior', 'rbio')
    wavelets = sum([pywt.wavelist(name) for name in families], [])
    # list of mode names in pywt and matalb
    modes = [('zpd', 'zpd'), ('cpd', 'sp0'), ('sym', 'sym'),
             ('ppd', 'ppd'), ('sp1', 'sp1'), ('per', 'per')] 
    # max RMSE
    epsilon = 1.0e-10
    
    test_perfect_reconstruction(families, wavelets, modes, epsilon)

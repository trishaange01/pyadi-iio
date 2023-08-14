# Copyright (C) 2019 Analog Devices, Inc.
#
# SPDX short identifier: ADIBSD

import time
import adi
# import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import spec

def test_pluto_plot():
    tone_freq = 3000000
    # Create radio
    sdr = adi.Pluto(uri="ip:192.168.2.1")

    # Configure properties
    sdr.rx_rf_bandwidth = 4000000
    sdr.rx_lo = 2000000000
    sdr.tx_lo = 2000000000
    sdr.tx_cyclic_buffer = True
    sdr.tx_hardwaregain_chan0 = -30
    sdr.gain_control_mode_chan0 = "slow_attack"

    # Read properties
    print("RX LO %s" % (sdr.rx_lo))

    # Create a sinewave waveform
    fs = int(sdr.sample_rate)

    # transmit a 3MHz tone
    sdr.dds_single_tone(tone_freq,0.99999)
    
    # Collect data
    x = sdr.rx()

    # estimate frequency
    ampl, freqs = spec.spec_est(x,fs,plot=True)
    indx = np.argmax(ampl)
    diff = np.abs(freqs[indx] - tone_freq)

    # test pluto
    s = "Peak: " + str(ampl[indx]) + " dBFS " + " @ " + str(freqs[indx]) + " Hz"
    print(s)
    assert (tone_freq * 0.01) > diff


test_pluto_plot()
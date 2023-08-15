import adi

adrv = adi.ad9375(uri="ip:10.116.110.35")

# DPD, CLGC, VSWR tracking enabled
adrv.tx_dpd_tracking_en_chan0 = 1
adrv.tx_dpd_tracking_en_chan1 = 1

adrv.tx_clgc_tracking_en_chan0 = 1
adrv.tx_clgc_tracking_en_chan1 = 1

adrv.tx_vswr_tracking_en_chan0 = 1
adrv.tx_vswr_tracking_en_chan1 = 1

# DPD, CLGC, VSWR tracking disabled
'''adrv.tx_dpd_tracking_en_chan0 = 0
adrv.tx_dpd_tracking_en_chan1 = 0

adrv.tx_clgc_tracking_en_chan0 = 0
adrv.tx_clgc_tracking_en_chan1 = 0

adrv.tx_vswr_tracking_en_chan0 = 0
adrv.tx_vswr_tracking_en_chan1 = 0'''

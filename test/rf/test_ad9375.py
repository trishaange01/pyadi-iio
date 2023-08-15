import adi

adrv = adi.ad9375(uri="ip:10.116.110.35")

# DPD, CLGC, VSWR tracking
# adrv.tx_dpd_tracking_en_chan0 = 1
# adrv.tx_dpd_tracking_en_chan1 = 1
# print("DPD tracking chan0: " + str(adrv.tx_dpd_tracking_en_chan0))
# print("DPD tracking chan1: " + str(adrv.tx_dpd_tracking_en_chan1))

# adrv.tx_clgc_tracking_en_chan0 = 1
# adrv.tx_clgc_tracking_en_chan1 = 1
# print("CLGC tracking chan0: " + str(adrv.tx_clgc_tracking_en_chan0))
# print("CLGC tracking chan1: " + str(adrv.tx_clgc_tracking_en_chan1))

# adrv.tx_vswr_tracking_en_chan0 = 1
# adrv.tx_vswr_tracking_en_chan1 = 1
# print("VSWR tracking chan0: " + str(adrv.tx_vswr_tracking_en_chan0))
# print("VSWR tracking chan1: " + str(adrv.tx_vswr_tracking_en_chan1))

# DPD actuator
# print(adrv.tx_dpd_actuator_en_chan0) #current chan0
# adrv.tx_dpd_actuator_en_chan0 = 0 # set new chan0
# print(adrv.tx_dpd_actuator_en_chan0) # new chan0

# print(adrv.tx_dpd_actuator_en_chan1) #current chan1
# adrv.tx_dpd_actuator_en_chan1 = 0 # set new chan1
# print(adrv.tx_dpd_actuator_en_chan1) # new chan1

# CLGC desired gain read and write
# print("CLGC desired gain chan0: " + str(adrv.tx_clgc_desired_gain_chan0)) # current chan0
adrv.tx_clgc_desired_gain_chan0 = -3000 # set new chan0
print("CLGC desired gain chan0 (new): " + str(adrv.tx_clgc_desired_gain_chan0)) # new chan0

# print("CLGC desired gain chan1: " + str(adrv.tx_clgc_desired_gain_chan1)) # current chan1
# adrv.tx_clgc_desired_gain_chan1 = -3000 # set new chan1
# print("CLGC desired gain chan1 (new): " + str(adrv.tx_clgc_desired_gain_chan1)) # new chan1



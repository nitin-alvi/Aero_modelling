import numpy as np
import math
#from pyatmos import coesa76
#coesa76_geom = coesa76([20])
#print(coesa76_geom)
#parameters 
ran = 1500*1000  #m
endu = 1*60*60 #s
V_cz = 65 #m/s
c_crz = 0.9/(60*60) #mg/Ns
c_loiter = 0.8/(60*60) #mg/Ns
w_pay = 90*4 #N
L_D_c = 15*0.866 #from graph raymer fig 3.7 page 41
L_D_e = 16
AR = 7
#weight fractions
#we_w0 = 0.65 #from graph raymer fig 3.1 page 30
w1_w0 = 0.970 #from graph raymer table 3.1 page 34
w2_w1 = 0.980 #from graph raymer table 3.1 page 34
w3_w2 = math.exp(-(ran*c_crz)/(V_cz*L_D_c)) #from Breguet equation for jet
w4_w3 = math.exp(-(endu*c_loiter)/(L_D_e)) #from endurance equation for jet
print("Weight fraction for range w3/w2 is:", w3_w2)
print("Weight fraction for endurance w4/w3 is:", w4_w3)
w_fuel_w0 = 1.06*(1 - (w1_w0*w2_w1*w3_w2*w4_w3))
print("Fuel weight fraction is:", w_fuel_w0)


#Estimate takeoff weight

A = 1.11 #empty weight equation  we_w0 = A*w0^C*kvs #kvs = 1.0 for wing with no sweep 
C = -0.09 #empty weight equation
tolerance = 0.0001
error = 1.0
iteration = 0
w0_guess = 1000
while error > tolerance:
    we_w0 = A*(w0_guess)**C
    w_0 = w_pay/(1- w_fuel_w0 - we_w0)
    if w_0 != w0_guess:
        error = abs(w_0 - w0_guess) / w0_guess
        w0_guess = (abs(w_0) + w0_guess)/2
        iteration += 1
print(f'Converged in {iteration} iterations the take off weight is:{w0_guess}')
print(f'Empty weight fraction is: {we_w0}')    
print(f'Fuel weight is: {w_fuel_w0*w0_guess}')
print(f'Payload weight fraction is: {w_pay/w0_guess}')   
   
    
    
   
    


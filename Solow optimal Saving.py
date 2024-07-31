# 
# 𝑦𝑡=𝑓(𝑘𝑡)=𝑘α𝑡 
# 𝑘𝑡+1=(1−𝑑)𝑘𝑡+𝑠𝑦𝑡
α=0.9,𝑑=0.1,s=s,𝑘1=0.1

# Generate
# generate : s = [0.01,0.02 ...] 500 ตัว ใช้ numpy
import numpy as np
s_rates = np.linspace(0,1,100) # เริ่มที่ 0 จบที่ 1 มี 100 ตัว
s_rates

# For each value of s_rates find consumption at t=500
# c500 is optimal consumption in RL

# For loop function calculate y[t] and k[t] for s=0 normal one!
s = 0; alpha = 0.9; d = 0.1
y = [0]*502; k = [0]*502; k[1] = 0.1
for t in range(1,501):
  y[t] = k[t]**alpha
  k[t+1] = (1-d)*k[t] + s*y[t]
# We got function y[t] and k[t] for t in range(1,502)
# !!!Not considered s rate!!!

# Generate consumption eauation | from theory C[t] = y[t] - sy[t]
c500 = y[500] - s*y[500]
c500

# For loop function calculate y[t] and k[t] for each s
c500 = []
for s in s_rates:
  alpha = 0.9; d = 0.1;
  y = [0]*502; k = [0]*502; k[1] = 0.1
  for t in range(1,501):
    y[t] = k[t]**alpha
    k[t+1] = (1-d)*k[t] + s*y[t]
  c500.append(y[500] - s*y[500]) # List of max C with different s

print(f'Optimal saving rate = {s_rates[np.argmax(c500)]}')
# From theory optimal S is give the highest consumption
# s_rates[np.argmax(c500)]
# np.argmax(c500) --> ให้ตำแหน่งของค่าที่มากที่สุดของ C500
# s_rates[ตำ่แหน่งของค่าที่มากที่สุดของ C500] --> s_rates เป็น List และค่าที่ Max consumption ให้ optimal Saving ด้วย
# ตำแหน่งที่ของค่าที่มากที่สุดใน c500 = ค่าของ s_rates ตำแหน่งนั้น

# As we know optimal saving rate = max consumption
# Can we see it in chart?
import matplotlib.pyplot as plt
plt.plot(s_rates, c500)
plt.title('Saving and long run consumption')
plt.xlabel('saving rate')
plt.ylabel('c500')
plt.show()

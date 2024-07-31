# Solow model
import matplotlib.pyplot as plt
s = 0.1 ; alpha = 0.9 ; d = 0.1 # กำหนดค่า
y = [0]*502 ; k = [0]*502 ; k[1] = 0.1 # เตรียมช่องสำหรับ List และ ตำแหน่งสุดท้ายที่ใช้ คือ 501 และมี t+1 ดังนั้นต้องเผื่อถึง 502
for t in range(1,501):
  y[t] = k[t]** alpha
  k[t+1] = (1-d)*k[t]+ s*y[t]
plt.plot(y[1:500]) # กราฟแปลก เลยกำหนดให้มันพล็อต 1:500
plt.show()
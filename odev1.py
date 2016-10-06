import random
import matplotlib.pyplot as plt

#mu ve sigma sayilarina atama;
mu1 = random.uniform(-5.0,5.0)
mu2 = random.uniform(-5.0,5.0)

sigma1 = random.uniform(0.5,1.5)
sigma2 = random.uniform(0.5,1.5)

#mu ve sigma sayilarinin testi;
print("mu1: "+str(mu1))
print("sigma1: "+str(sigma1))
print("mu2: "+str(mu2))
print("sigma2: "+str(sigma2))

#iki ayri dizi olusturma;
dizi1 = []
dizi2 = []

#dizilerin icini doldururken kendisine en yakin tam sayiya yuvarlama;
for i in range(0,10000):
    dizi1.append(int(round(random.gauss(mu1,sigma1),0)))
    dizi2.append(int(round(random.gauss(mu2,sigma2),0)))


#histogram olusturma;
histogram1 = {}
histogram2 = {}

for i in range(-20,20):
	histogram1[i]=0;
	histogram2[i]=0;

#histogramlari doldurma ;
for i in range (0,10000):
    histogram1[dizi1[i]] +=1
    histogram2[dizi2[i]] +=1


#histogramlarin normalize etme;
toplam1 = 0
toplam2 = 0

for i in range(-20,20):
    toplam1 += histogram1[i]
    toplam2 += histogram2[i]

for i in range (-20,20):
	histogram1[i] = float(float(histogram1[i])/float(toplam1))
	histogram2[i] = float(float(histogram2[i])/float(toplam2))

#uzaklik hesaplamasi;
min1 = min(dizi1)
max1 = max(dizi1)
min2 = min(dizi2)
max2 = max(dizi2)
uzaklik = 0

if(max1-min1)>(max2-min2):
        for i in range(min1,max1):
            uzaklik += abs(i-min2)*(histogram1[i])
            if histogram2[min2]>histogram1[i]:
                uzaklik+= histogram2[min2]-histogram1[i]
            min2+=1
else:
        for i in range(min2,max2):
            uzaklik += abs(i-min1)*(histogram2[i])
            if histogram1[min1]>histogram2[i]:
                uzaklik+= histogram1[min1]-histogram2[i]
            min1+=1

print("uzaklik ="+str(uzaklik))

#histogramlarin gorsellenmesi;
plt.bar(histogram1.keys(),histogram1.values(),0.5,color='r')
plt.bar(histogram2.keys(),histogram2.values(),0.5,color='b')
plt.show()

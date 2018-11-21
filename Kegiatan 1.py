x = {"Segitiga":"L =  0.5 * a * t" ,
     "Persegi":"L = s * * 2" ,
     "Persegi panjang":"L = p * l" ,
     "lingkaran":"L = pi * r * * 2" ,
     "Jajaran genjang":"L = a * t" }

print "|%-4s||%-17s||%-17s"%("No", "Nama Bangun", "Rumus Luas")
print "|%-4s||%-17s||%-17s"%("-"*4, "-"*7, "-"*17)
a = 1
for i in x:
     print"|%-4s||%-17s||%-17s"%(a, i, x[i])
     a += 1

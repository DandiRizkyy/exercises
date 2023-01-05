
#Membuat fungsi perkalian
def kuadrat(x):
    return x * x

#Mengkuadratkan setiap jumlah yang ada di dalam array dengan jumlah yang sama (semisal x=1 berati 1 * 1)
for i in range(10):
    print(f"Hasil dari kuadrat {i} adalah {kuadrat(i)}")
hitung = 0
sum = 0

print("=" * 55)
print("Program Hitung Bilangan habis dibagi 3 dan 5 [1-100]")
print("=" * 55)

for bil in range(1, 101):
    if bil % 3 == 0 and bil % 5 == 0:
        hitung += 1
        sum += bil
        print("Bilangan pada index ke-", bil-1,
              "habis dibagi 3 dan 5 adalah", bil)

print("=" * 55)
print("Banyak Bilangan yang habis dibagi 3 dan 5 adalah", hitung)
print("jumlah dari semua bilangan habis dibagi 3 dan 5 adalah", sum)
# Program membuat kalkulator sederhana

# Fungsi ini menambahkan angka
def tambah(x, y):
    return x + y

# Fungsi ini mengurangi angka
def pengurangan(x, y):
    return x - y

# Fungsi ini mengalikan angka
def perkalian(x, y):
    return x * y

# Fungsi ini membagikan angka
def pembagian(x, y):
    return x / y


print("Select operation.")
print("1.Tambah")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

while True:
    # ambil masukan dari User
    choice = input("Masukkan pilihan (1/2/3/4):")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Masukkan nomor pertama: "))
        num2 = float(input("Masukkan nomor kedua:"))

        if choice == '1':
            print(num1, "+", num2, "=", tambah(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", pengurangan(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", perkalian(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", pembagian(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Melakukan perhitungan selanjutnya? (Ya/Tidak):")
        if next_calculation == "Tidak":
          break
    
    else:
        print("Masukan Tidak Valid")
import etlap
import osszegzes

levesek = ["Nem kér semmit", "Húsleves", "Gyümölcsleves", "Bableves"]
levesar = [0,880,600,1200]
foetel = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]

def rendelesossz():
    print(" ")
    print(" ")
    etlap.lev()
    print("Válasszon levest! (0-tol 3-ig válasszon)")
    

    rendeles: int = int(input("írd be hogy hanyas számu levest kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    leves = levesek[rendeles]
    print (leves + "-t kér!")

    print(" ")
    print(" ")
    etlap.foet()
    print("Válasszon főételt! (0-től 3-ig válasszon)")
    list = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]

    rendeles1: int = int(input("írd be hogy hanyas számu ételt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    kaja = list[rendeles1]
    print (kaja + "-t kér!")

    print(" ")
    print(" ")
    etlap.drink()
    print("Válasszon italt! (0-től 3-ig válasszon)")
    itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]

    rendeles2: int = int(input("írd be hogy hanyas számu italt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    ital = itallap[rendeles2]
    print (ital + "-t kér!")

    print(" ")
    print(" ")
    etlap.dessert()
    print("Válasszon desszertet! (1-től 4-ig válasszon)")
    desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]

    rendeles3: int = int(input("írd be hogy hanyas számu ételt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    desszert = desszertek[rendeles3]
    print (desszert + "-t kér!")

    osszegzes.nyugta()







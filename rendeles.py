import etlap
import main
levesek = ["0 - Nem kér semmit", "1 - Húsleves", "2 - Gyümölcsleves", "3 - Bableves"]
levesar = [0,880,600,1200]
foetel = ["0 - Nem kér semmit", "1 - Tojásos nokedli", "2 - Rántott hús rizibizivel", "3 - Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["0 - Nem kér semmit", "1 - Coca Cola", "2 - Kőbányai", "3 - Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]

def rendeles():
    print("\n\n")
    etlap.lev()
    print("Válasszon levest! (0-tol 3-ig válasszon)")
    

    rendeles: int = int(input("írd be hogy hanyas számu levest kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    leves = levesek[rendeles]
    print (leves)


    print("Válasszon főételt! (0-től 3-ig válasszon)")
    list = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]

    rendeles1: int = int(input("írd be hogy hanyas számu ételt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    kaja = list[rendeles1]
    print (kaja)


    print("Válasszon italt! (0-től 3-ig válasszon)")
    itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]

    rendeles2: int = int(input("írd be hogy hanyas számu italt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    ital = itallap[rendeles2]
    print (ital)

    print("Válasszon desszertet! (1-től 4-ig válasszon)")
    desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]

    rendeles3: int = int(input("írd be hogy hanyas számu ételt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    desszert = desszertek[rendeles]
    print (desszert)







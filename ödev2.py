fgrades = list(range(10))
gradesmidterm=[40, 53, 59, 71, 80]
gradesfinali=[100, 25, 60, 92, 81]
names=[" Violet Grey", "Rylan Teel" , " Lula Albertson", " Lula Albertson", " Austyn Whittle"]
info = {"violet Grey":[40, 100], 
        "Rylan Teel":[53, 25],
        " Lula Albertson":[59, 60],
        " Lula Albertson":[71, 92],
        " Austyn Whittle":[80, 81]  }
sorted_g = sorted(info.items(), key=lambda x: x[1])
print("Tebrikler!", sorted_g )

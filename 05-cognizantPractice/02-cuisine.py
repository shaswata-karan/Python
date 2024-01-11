indian = ["Samosa", "Daal", "Naan"]
chinese = ["Chowmein", "ChilliChicken", "Manchurian"]
mughlai = ["Biriyani", "ChickenButterMasala", "MuttonRoganjosh"]
italian = ["Paasta", "Pizza", "Risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print("indian")
if dish in chinese:
    print("chinese")
if dish in mughlai:
    print("mughlai")
if dish in italian:
    print("italian")
else:
    print("unable to find", dish ,"from my little knowledge")
#1. Feladat: Készíts egy programot! A gép gondol egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot!

szam = int(input("Kérem adjon meg egy számot 1-10-ig!:"))

if szam == 4:
    print("Talált!")

if szam >= 10:
    print("Kissebb")
    
if szam <= 1:
    print("Nagyobb")
    

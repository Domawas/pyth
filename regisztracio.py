nev=str(input("Név:"))
email=(input("Email cím: "))
jelszo=(input("Jelszó: "))

if len(jelszo) >= len(6):
    print(f"Sikeres regisztráció {nev} ({email})")
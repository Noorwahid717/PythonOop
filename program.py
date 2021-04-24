perintah = ""
memulai = False
while True:
    perintah = input("> ").lower()
    if perintah == "mulai":
        if memulai:
            print("Program telah dijalankan.")
        else:
            memulai = True
            print("Program dimulai...")
    elif perintah == "berhenti":
        if not memulai:
            print("Program telah dihentikan.")
        else:
            memulai = False
            print("Menghentikan program...")
    elif perintah == "bantuan":
        print("""
mulai - untuk memulai program
berhenti - untuk menghentikan program
keluar - untuk keluar dari program
""")
    elif perintah == "keluar":
        break
    else:
        print("Maaf, saya tidak paham")

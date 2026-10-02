
# Dastur quyidagilarni bajarsin:

# 🏠 Xonalarni qo‘shish
# 🔎 Bo‘sh xonalarni ko‘rsatish
# 👤 Mijoz ma’lumotlarini kiritish
# 📅 Xona bron qilish
# ❌ Bronni bekor qilish
# 💵 Umumiy narxni hisoblash
# 🔢 Xona raqami bo‘yicha qidirish
# 📊 Eng ko‘p bron qilingan xonani aniqlash



xonalar = []

while True:

    print("1. Xona qo‘shish")
    print("2. Bo‘sh xonalarni ko‘rsatish")
    print("3. Mijoz ma’lumotlarini kiritish")
    print("4. Xona bron qilish")
    print("5. Bronni bekor qilish")
    print("6. Umumiy narxni hisoblash")
    print("7. Xona raqami bo‘yicha qidirish")
    print("8. Eng ko‘p bron qilingan xona")
    print("0. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        raqam = input("Xona raqami: ")
        narx = int(input("1 kunlik narxi: "))

        xonalar.append([raqam, narx, "bo'sh", "", 0, 0])

        print("Xona qo‘shildi!")

    elif tanlov == "2":
        print("\n===== BO‘SH XONALAR =====")

        for xona in xonalar:
            if xona[2] == "bo'sh":
                print(
                    "Xona:", xona[0],
                    "| Narxi:", xona[1],
                    "so‘m"
                )

    elif tanlov == "3":
        raqam = input("Xona raqami: ")

        topildi = False

        for xona in xonalar:
            if xona[0] == raqam:
                ism = input("Mijoz ismi: ")
                telefon = input("Telefon raqami: ")

                xona.append(ism)
                xona.append(telefon)

                print("Mijoz ma’lumotlari kiritildi!")
                topildi = True

        if topildi == False:
            print("Xona topilmadi!")


    elif tanlov == "4":
        raqam = input("Xona raqami: ")

        for xona in xonalar:
            if xona[0] == raqam:

                if xona[2] == "bo'sh":
                    mijoz = input("Mijoz ismi: ")
                    kun = int(input("Necha kun: "))

                    xona[2] = "band"
                    xona[3] = mijoz
                    xona[4] = kun
                    xona[5] += 1

                    print("Xona muvaffaqiyatli bron qilindi!")
                    print("Umumiy narx:", xona[1] * kun, "so‘m")

                else:
                    print("Bu xona band!")

    elif tanlov == "5":
        raqa = input("Xona raqami: ")

        for xona in xonalar:
            if xona[0] == raqam:

                if xona[2] == "band":
                    xona[2] = "bo'sh"
                    xona[3] = ""
                    xona[4] = 0

                    print("Bron bekor qilindi!")
                else:
                    print("Bu xona band emas!")

    elif tanlov == "6":
        raqam = input("Xona raqami: ")

        for xon in xonalar:
            if xona[0] == raqam:

                if xona[2] == "band":
                    jami = xona[1] * xona[4]

                    print("Mijoz:", xona[3])
                    print("Kun:", xona[4])
                    print("Umumiy narx:", jami, "so‘m")
                else:
                    print("Xona band emas!")

    elif tanlov == "7":
        raqam = input("Xona raqamini kiriting: ")

        topildi = False

        for xona in xonalar:
            if xona[0] == raqam:
                print("\nXona topildi!")
                print("Xona raqami:", xona[0])
                print("Narxi:", xona[1], "so‘m")
                print("Holati:", xona[2])
                print("Mijoz:", xona[3])

                topildi = True

        if topildi == False:
            print("Xona topilmadi!")

    elif tanlov == "8":
        if len(xonalar) == 0:
            print("Xonalar yo‘q!")
        else:
            eng_kop = xonalar[0]

            for xona in xonalar:
                if xona[5] > eng_kop[5]:
                    eng_kop = xona

            print("\n===== ENG KO‘P BRON QILINGAN XONA =====")
            print("Xona:", eng_kop[0])
            print("Bronlar soni:", eng_kop[5])

    elif tanlov == "0":
        print("Dastur tugadi!")
        break

    else:
        print("Noto‘g‘ri tanlov!")

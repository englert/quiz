import random
import os

def generate_binary_number(bits):
    """Generál egy véletlenszerű bináris számot a megadott bitméret szerint."""
    return bin(random.randint(0, 2**bits - 1))

def generate_question(conversion_type, question_number):
    match conversion_type:
        case 'hex2dec':
            hex_value = hex(random.randint(0, 4095))
            question = f"# hex2dec: {question_number}. {hex_value} ="
            return question, int(hex_value, 16)
        case 'hex2bin':
            hex_value = hex(random.randint(0, 4095))
            question = f"# hex2bin: {question_number}. {hex_value} = 0b"
            return question, bin(int(hex_value, 16))[2:]
        case 'hex2oct':
            hex_value = hex(random.randint(0, 4095))
            question = f"# hex2oct: {question_number}. {hex_value} = 0o"
            return question, oct(int(hex_value, 16))[2:]
        case 'oct2dec':
            oct_value = oct(random.randint(0, 4095))
            question = f"# oct2dec: {question_number}. {oct_value} ="
            return question, int(oct_value, 8)
        case 'oct2bin':
            oct_value = oct(random.randint(0, 4095))
            question = f"# oct2bin: {question_number}. {oct_value} = 0b"
            return question, bin(int(oct_value, 8))[2:]
        case 'oct2hex':
            oct_value = oct(random.randint(0, 4095))
            question = f"# oct2hex: {question_number}. {oct_value} = 0x"
            return question, hex(int(oct_value, 8))[2:]
        case 'bin2dec':
            bits = random.choice([5, 6, 7, 8, 9])  # Véletlenszerű bitméret (5-9 bit)
            bin_value = generate_binary_number(bits)
            question = f"# bin2dec: {question_number}. {bin_value} ="
            return question, int(bin_value, 2)
        case 'bin2hex':
            bits = random.choice([5, 6, 7, 8, 9])  # Véletlenszerű bitméret (5-9 bit)
            bin_value = generate_binary_number(bits)
            question = f"# bin2hex: {question_number}. {bin_value} = 0x"
            return question, hex(int(bin_value, 2))[2:]
        case 'bin2oct':
            bits = random.choice([5, 6, 7, 8, 9])  # Véletlenszerű bitméret (5-9 bit)
            bin_value = generate_binary_number(bits)
            question = f"# bin2oct: {question_number}. {bin_value} = 0o"
            return question, oct(int(bin_value, 2))[2:]
        case _:
            raise ValueError(f"Ismeretlen konverzió típus: {conversion_type}")

def generate_quiz(num_blocks):
    """Generál egy quiz.txt fájlt a megadott számú blokkal."""
    # Ellenőrizzük, hogy a fájl már létezik-e
    if os.path.exists("quiz.txt"):
        print("A 'quiz.txt' fájl már létezik. A generálás kihagyva.")
        return

    conversions = ['hex2dec', 'hex2bin', 'hex2oct', 'oct2dec', 'oct2bin', 'oct2hex', 'bin2dec', 'bin2hex', 'bin2oct']
    questions = []

    for block in range(1, num_blocks + 1):
        for i, conv in enumerate(conversions, start=1):
            question_number = (block - 1) * 9 + i  # A kérdés sorszáma (1-től kezdve)
            question, _ = generate_question(conv, question_number)
            questions.append(question)

    # Az aktuális könyvtár elérési útjának meghatározása
    current_directory = os.getcwd()
    full_path = os.path.join(current_directory, "quiz.txt")

    # Fájl írása UTF-8 kódolással
    with open("quiz.txt", "w", encoding="utf-8") as file:
        file.write(f"# Full path: {full_path}\n")  # Full path sor
        file.write("# Végezd el a következő átalakításokat!\n\n")
        for q in questions:
            file.write(q + "\n")

    print("A 'quiz.txt' fájl sikeresen generálva.")

def check_solutions():
    """Ellenőrzi a quiz.txt fájlban lévő megoldásokat."""
    if not os.path.exists("quiz.txt"):
        print("A 'quiz.txt' fájl nem létezik. Kérem, először generálja a fájlt.")
        return

    # Fájl olvasása UTF-8 kódolással
    with open("quiz.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Kérdések és válaszok kinyerése
    questions = []
    answers = []
    for line in lines:
        if line.startswith("#") and "=" in line:
            parts = line.strip().split("=")
            questions.append(parts[0].strip())
            answers.append(parts[1].strip())

    # Ellenőrizzük a megoldásokat
    correct_count = 0
    for i, (question, answer) in enumerate(zip(questions, answers)):
        # Kinyerjük a konverzió típusát és az értéket
        try:
            # A konverzió típusa a '#' és az első ':' között van
            conversion_type = question.split(":")[0].replace("#", "").strip()
            # Az érték a ':' után van, de az egyenlőségjel előtt
            value_part = question.split(":")[1].split("=")[0].strip()
            # Az értékből kinyerjük csak a számot (pl. '1. 0x152' -> '0x152')
            value = value_part.split()[-1].strip()
        except IndexError:
            print(f"Hiba a kérdés feldolgozásában: {question}")
            continue

        # Kiszámítjuk a helyes megoldást
        match conversion_type:
            case "hex2dec":
                correct_answer = str(int(value, 16))
            case "hex2bin":
                correct_answer = bin(int(value, 16))[2:]
            case "hex2oct":
                correct_answer = oct(int(value, 16))[2:]
            case "oct2dec":
                correct_answer = str(int(value, 8))
            case "oct2bin":
                correct_answer = bin(int(value, 8))[2:]
            case "oct2hex":
                correct_answer = hex(int(value, 8))[2:]
            case "bin2dec":
                correct_answer = str(int(value, 2))
            case "bin2hex":
                correct_answer = hex(int(value, 2))[2:]
            case "bin2oct":
                correct_answer = oct(int(value, 2))[2:]
            case _:
                print(f"Ismeretlen konverzió típus: {conversion_type}")
                continue

        # Összehasonlítjuk a megoldást
        if answer == correct_answer:
            print(f"\033[92m{i + 1}. kérdés: Helyes! ({question} = {answer})\033[0m")  # Zöld szín
            correct_count += 1
        else:
            print(f"\033[91m{i + 1}. kérdés: Hibás! ({question} = {answer})\033[0m")  # Piros szín

    print(f"\nÖsszesen {correct_count} helyes válasz a {len(questions)} kérdésből.")

# Példa: 2 blokk generálása (2 * 9 = 18 feladat)
generate_quiz(num_blocks=2)

# Példa: Megoldások ellenőrzése
check_solutions()
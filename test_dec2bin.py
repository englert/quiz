import random
import os
import hashlib

def dec_to_bin(dec_num):
    return bin(int(dec_num))[2:]  # Bináris szám, a '0b' prefix nélkül

def generate_dec_number(length):
    """Generál egy decimális számot a megadott hosszal."""
    dec_digits = "0123456789"
    return ''.join(random.choice(dec_digits) for _ in range(length))

def generate_quiz(num_questions=30):
    questions = []
    for i in range(num_questions):
        length = random.choice([2, 3, 4])  # Véletlenszerűen 2-4 karakter hosszú decimális szám
        dec_num = generate_dec_number(length)
        questions.append((i + 1, dec_num, dec_to_bin(dec_num)))  # (sorszám, decimális szám, bináris válasz)
    return questions

def calculate_checksum(content):
    """Kiszámolja a tartalom SHA-256 checksum-ját."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def save_quiz_to_file(questions, filename='quiz.txt'):
    content = ""
    for i, dec_num, _ in questions:
        content += f"{i}. {dec_num} = \n"
    
    # Hozzáadjuk a teljes elérési utat a tartalomhoz
    full_path = os.path.abspath(__file__)
    content += f"Full path: {full_path}\n"
    
    # Kiszámoljuk a checksum-ot (csak a decimális számokra és az elérési útvonalra)
    checksum_content = ""
    for _, dec_num, _ in questions:
        checksum_content += dec_num + "\n"
    checksum_content += full_path + "\n"
    
    checksum = calculate_checksum(checksum_content)
    content += f"Checksum: {checksum}\n"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

pwd = os.getcwd()

if not os.path.exists('quiz.txt'):
    quiz_questions = generate_quiz()
    save_quiz_to_file(quiz_questions)

def load_quiz(filename='quiz.txt'):
    """
    Beolvassa a quiz.txt fájlt, és visszaadja a decimális számokat és a diák által megadott válaszokat.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    questions = []
    checksum_content = ""
    for line in lines:
        if not line.strip():  # Üres sorok kihagyása
            continue
        
        # Feladat sor feldolgozása (pl. "1. 123 = 1111011")
        if line.startswith("Checksum:") or line.startswith("Full path:"):
            continue
        
        parts = line.split("=")
        question_part = parts[0].strip()  # "1. 123"
        student_answer = parts[1].strip() if len(parts) > 1 else ""  # Diák válasza
        
        # Decimális szám kinyerése
        dec_num = question_part.split(".")[1].strip()
        checksum_content += dec_num + "\n"
        
        questions.append((dec_num, student_answer))
    
    # Beolvassuk az elérési utat
    full_path_line = [line for line in lines if line.startswith("Full path:")]
    if full_path_line:
        full_path = full_path_line[0].split(":")[1].strip()
        checksum_content += full_path + "\n"
    
    # Beolvassuk a checksum-ot
    checksum_line = [line for line in lines if line.startswith("Checksum:")]
    if checksum_line:
        stored_checksum = checksum_line[0].split(":")[1].strip()
    else:
        stored_checksum = None
    
    # Újraszámoljuk a checksum-ot
    calculated_checksum = calculate_checksum(checksum_content)
    
    # Ellenőrizzük a checksum-ot
    if stored_checksum != calculated_checksum:
        raise ValueError("Checksum mismatch! A fájl tartalma megváltozott!")
    
    return questions

# Beolvassuk a kérdéseket és válaszokat
questions = load_quiz()

# Manuálisan definiáljuk a 30 tesztfüggvényt
def test_question_1():
    dec_num, student_answer = questions[0]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_2():
    dec_num, student_answer = questions[1]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_3():
    dec_num, student_answer = questions[2]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

# Folytasd a tesztfüggvények definiálását...
def test_question_4():
    dec_num, student_answer = questions[3]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_5():
    dec_num, student_answer = questions[4]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_6():
    dec_num, student_answer = questions[5]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_7():
    dec_num, student_answer = questions[6]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_8():
    dec_num, student_answer = questions[7]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_9():
    dec_num, student_answer = questions[8]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_10():
    dec_num, student_answer = questions[9]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_11():
    dec_num, student_answer = questions[10]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_12():
    dec_num, student_answer = questions[11]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_13():
    dec_num, student_answer = questions[12]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_14():
    dec_num, student_answer = questions[13]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_15():
    dec_num, student_answer = questions[14]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_16():
    dec_num, student_answer = questions[15]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_17():
    dec_num, student_answer = questions[16]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_18():
    dec_num, student_answer = questions[17]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_19():
    dec_num, student_answer = questions[18]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_20():
    dec_num, student_answer = questions[19]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_21():
    dec_num, student_answer = questions[20]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_22():
    dec_num, student_answer = questions[21]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_23():
    dec_num, student_answer = questions[22]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_24():
    dec_num, student_answer = questions[23]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_25():
    dec_num, student_answer = questions[24]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_26():
    dec_num, student_answer = questions[25]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_27():
    dec_num, student_answer = questions[26]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_28():
    dec_num, student_answer = questions[27]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_29():
    dec_num, student_answer = questions[28]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"

def test_question_30():
    dec_num, student_answer = questions[29]
    correct_answer = dec_to_bin(dec_num)
    assert student_answer == correct_answer, "Hibás válasz!"
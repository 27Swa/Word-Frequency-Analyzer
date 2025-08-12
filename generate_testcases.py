import random

def generate_test(wrd,n,fp):
    data = list()
    for __ in range(n):
        l = " ".join(random.choices(wrd,k= random.randint(10,25)))
        data.append(l)
    
    with open(fp,"w",encoding='utf-8') as f:
        f.write("\n".join(data))

if __name__ == '__main__':

    # Define lists wtih some words, punctuations, numbers to generate testcases from  
    w1 = [  "Hi","apple",   "ball", "cat", "dog", "eat", "fast", "go", "happy",
    "ice", "jump", "kind","frog", "father", "dress","brother" ,"bus",
    "laugh", "man", "name", "open", "pen", "quiet", "run", "sit", "talk",
    "umbrella", "visit", "water", "xray", "yes", "zoo", "book", "chair",
    "dance", "egg", "fire", "girl", "house", "in", "job", "keep", "love",
    "mother", "no", "out", "pig", "queen", "red", "sun", "toy", "under", "van",
    "wind", "yard", "zero", "bag", "coin", "door", "friend", "hello", "light",
    "hard", "like", "shirt", "tree", "uncle", "hug", "phone", "window", "moon"
    "hat","aunt","game","crying", "car","hands","teacher", "school","clock",
    "bird","road","river","shelf","write","wall","photo","watch","sleeping",
    "milk","ring","pencil","shirt","snow","strong","legs","soup","flower","floor",
    "box","doorbell"]

    num = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
        "25", "30", "35", "40", "45", "50", "55", "60", "65", "70",
        "75", "80", "85", "90", "95", "100", "150", "200", "250", "300",
        "350", "400", "450", "500", "550", "600", "650", "700", "750", "800",
        "850", "900", "950", "1000", "1500", "2000", "2500", "3000", "3500", "4000",
        "4500", "5000", "6000", "7000", "8000", "9000", "10000", "15000", "20000", "25000",
        "30000", "35000", "40000", "45000", "50000", "60000", "70000", "80000", "90000", "100000"]

    punc = [ ".", ",", "!", "?", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", 
    "'", '"', "…", "/", "\\", "@", "#", "$", "%", "&", "*", "+", "=", "<", ">", "|", "~", "`"]

    ara = [ "كتاب", "مدرسة", "طالب", "معلم", "مدينة", "سيارة", "شمس", "قمر", "بحر", "سماء",
    "زهرة", "حديقة", "باب", "نافذة", "كرسي", "طاولة", "هاتف", "كمبيوتر", "قلم", "دفتر",
    "مكتب", "طريق", "شارع", "قطار", "طيارة", "مطار", "بيت", "غرفة", "مطبخ", "حديقة",
    "مستشفى", "صيدلية", "خبز", "ماء", "شاي", "قهوة", "سكر", "ملح", "لحم", "سمك",
    "فاكهة", "تفاح", "موز", "برتقال", "عنب", "بطيخ", "كمثرى", "توت", "ليمون", "فراولة"]

    ara_punc = [ "،", "؛", "؟", "«", "»", "ـ", "…"]
    sm = ["Hi","apple","ball","350", "400","."]

    m = w1 + num + punc
    l = m + ara_punc 
    a = ara + ara_punc
    mm = a + m

    # Generating test files  
    # sample
    generate_test(sm,3,"Test cases/1.txt")
    # 1. Small testcase
    generate_test(w1,50,"Test cases/2.txt")
    # 2. Medium testcase
    generate_test(m,150,"Test cases/3.txt")
    # 3. Large testcase
    generate_test(l,300,"Test cases/4.txt")
    # 4. Arabic testcase
    generate_test(a,300,"Test cases/5.txt")
    # 5. Mix data english,arabic
    generate_test(mm,2000,"Test cases/6.txt")

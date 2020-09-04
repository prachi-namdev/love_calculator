import random
class Love:
    def __init__(self):
        self.total_vowel1 = 0
        self.total_vowel2 = 0
        self.love = 0
        self.consonant1 = 0
        self.consonant2 = 0

    def vow_con(self):
        print("*****************************")
        print("*   Love Match Calculator   *")
        print("*****************************")
        name1 = input("Enter your name \n")
        name2 = input("Enter your partner Name \n")
        for i in ['a', 'e', 'i', 'o', 'u']:
            self.total_vowel1 += name1.count(i)
        for i in ['a', 'e', 'i', 'o', 'u']:
            self.total_vowel2 += name2.count(i)
        if self.total_vowel1 == self.total_vowel2:
            self.love += random.randint(10, 30)
        CONSONANTS = 'bcdfghjklmnprstvwxyz'
        self.consonant1 = len([letter for letter in name1 if letter.lower() in CONSONANTS])
        self.consonant2 = len([letter for letter in name2 if letter.lower() in CONSONANTS])

        if self.consonant1 == self.consonant2:
            self.love += random.randint(20, 40)
        l1 = name1
        l2 = name2
        split1 = l1.split()
        split2 = l2.split()
        fl1 = [word[0] for word in split1]
        fl2 = [word[0] for word in split2]

        if fl1 == fl2:
            self.love += random.randint(10, 30)

        if len(name1) == len(name2):
            self.love += random.randint(1, 10)
            self.love += random.randint(10, 50)
        if self.love > 100:
            self.love = 100
        print(name1, "and", name2, "have a", self.love, "% relationship.")
        if (self.love > 90) or (self.love == 90):
            print("They have an unbreakable relationship that will last forever.")
        if (self.love < 49) or (self.love == 49):
            print("They have a weak relationship that could have been a  'match made in heaven'.")


c = Love()
c.vow_con()

'''

Friends, this is a surprise party for Female Person You Know:.
we are hear to celebrate her Noun #1. All of her most
Adjective #1:.friends are here, including me, her devoted and
faithful Noun #2:. I must say that she doesn't look a day over
Number #1. Naturally, we have some Adjective #2.presents
for her. Male Person You Know:.bought her a beautiful copper
Noun #3.that she can wear on her lovely Part of the Body:.
And our hostess got her a dozen Plural Noun #1:.that she can hang
in her Noun #4:. And we had the bakery send up a huge
Adjective #3:.Noun #5.with Number #2.candles on it.
We all want to wish her a very Adjective #4:.birthday and
many happy Plural Noun #2. Now, let's all sing together: "Happy
Noun #6-day to you!"


A Charming Story with a Happy Ending

Once upon a Noun #1, there were three little pigs. The
first little pig was very Adjective #1:,.and he built a house for
himself out of Plural Noun #1:. The second little pig was
Adjective #2, and he built a house out of Plural Noun #2. But
the third little pig was very Adjective #3:, and he built his house
out of genuine Plural Noun #3. Well one day, a mean old wolf
came along and saw the houses. "Exclamation:!" he said. "I'll
Verb #1:.and I'll Verb #2.and I'll blow your house
down." And he blew down the first little pig's Noun #2:.and
the second little pig's Plural Noun #4. The two little pigs ran
to the third pig's house. Thereupon, the wolf began blowing, but he
couldn't blow down the third little pig's Noun #3.house. so he
Past Tense Verb:.off into the forest, and the three little Adjective #4:
pigs moved to Chicago and went into the sausage business.

'''
import time
print("Mad Libs starting now........")
time.sleep(2)

Adjective1=input("Input Adjective 1\n")
Adjective2=input("Input Adjective 2\n")
Adjective3=input("Input Adjective 3\n")
Adjective4=input("Input Adjective 4\n")
Exclamation=input("Input an Exclamation!\n")
Noun1=input("Input Noun 1\n")
Noun2=input("Input Noun 2\n")
Noun3=input("Input Noun 3\n")
Past_Tense_Verb=input("Input a Past Tense Verb\n")

PNoun1=input("Input Plural Noun 1\n")
PNoun2=input("Input Plural Noun 2\n")
PNoun3=input("Input Plural Noun 3\n")
PNoun4=input("Input Plural Noun 4\n")

Verb1=input("Input Verb 1\n")
Verb2=input("Input Verb 2\n")

print("Word Gathering Completed :)")

print("Creating your story......")

for i in range(5):
    time.sleep(1)
    print(".")


print("Once upon a time, there were three little pigs.")
time.sleep(1)
print("The first little pig was very {} ,".format(Adjective1))
time.sleep(1)
print("and he built a house for himself out of {}.".format(PNoun1))
time.sleep(1)
print("The second little pig was {}, and he built a house out of {}.".format(Adjective2,PNoun2))
time.sleep(2)
print("But the third little pig was very {}, and he built his house out of genuine {}.".format(Adjective3,Noun3))
time.sleep(1)
print("Well one day, a mean old wolf came along and saw the houses.{}! ".format(Exclamation))
time.sleep(1)
print("he said. I'll {} .and I'll {} " .format(Verb1,Verb2))
time.sleep(1)
print("and I'll blow your house down.")
time.sleep(2)
print("And he blew down the first little pig's {} ".format(Noun2))
time.sleep(1)
print("and the second little pig's {}" .format(PNoun4))
time.sleep(3)
print('''The two little pigs ran
to the third pig's house. Thereupon, the wolf began blowing, but he
couldn't blow down the third little pig's {} house.'''.format(Noun3))
time.sleep(1)

print('''so he
{} off into the forest, and the three little {}
pigs moved to Chicago and went into the sausage business.'''.format(Past_Tense_Verb,Adjective4))


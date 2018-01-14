#list of consonants & vowels

#consonant=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
#vowel=('a','e','i','o','u')

consonant=('b','g','d','t','f','c','h','m','n','p','h','r','l','s','g','k','sh')
vowel=('a','e','i','o','u')

import random

def run():
        #asks for length of name to generate
        length=int(input("Enter length of name to generate: "))
        name=[]

        count=0 #sets length counter to 0

        while (count < length):
                choice=random.randint(1,2)
                if (count == length - 1) and (name[count-1] in consonant):
                        name.insert(count, random.choice(vowel))     
                else:
                        if (choice==1): #consonant
                                if (not name) or (name[count-1] in vowel) or ((name[count-1] in consonant) and \
                                                                              (name[count-2] in vowel)):
                                        name.insert(count, random.choice(consonant))
                                else: name.insert(count, random.choice(vowel))
                        else: #vowel
                                if (not name) or (name[count-1] in consonant):
                                        name.insert(count, random.choice(vowel))
                                else: name.insert(count, random.choice(consonant))
                #print("Index " + str(count) + ": " + "".join(name))
                count = count + 1
        print("Final name generated: " + "".join(name).upper())
        print()
        run() #recursive
run()

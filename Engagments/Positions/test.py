# def puppies(name, age):
#     print(f"Welcome to the puppy world {name}, who is {age} years old!")
#     print("Puppies are the best! They are so cute and cuddly. You will have a great time with them!")

# def kittens(name, age):
#     print(f"Welcome to the kitten world {name}, who is {age} years old!")
#     print("Kittens are the best! They are so cute and cuddly. You will have a great time with them!")



# name = input("Whats your name\n>")
# age = input("Whats your age\n>")
# game = input("Do you like puppies or kittens?\n>")


# if game == "puppies":
#     puppies(name, age)
# elif game == "kittens":
#     kittens(name, age)  
# else:
    # print("what da frick u mean")

# n = 21
#     if n > 20:
#         print(n)
#          print("Done") 

# temperatures = open('d:\\temps.txt', 'r', encoding='utf-8')
# values = [float(line.strip()) for line in temperatures if line.strip()]
# avgtmp = sum(values) / len(values)
# temperatures.close()
# print(f'{avgtmp:.1f}')
# Problem 1
sentence = "The nickname of students at BYU is Cougars."
t = sentence.replace("BYU", "BYUH").replace("Cougar", "Seasider")


# Problem 2
sentence = "The nickname of students at BYU is Cougars."
c = sentence.count("s")


# Problem 3
name = "put your name here"
upName = name.upper()


# Problem 4
sentence = " The brown dog. "
stripped = sentence.rstrip()


# Problem 5
sentence = "The purple cow."
pos = sentence.find("purple")


# Problem 6
sentence = "The purple cow."
color = sentence[4:10]


# Problem 7
sentence = "The purple cow."
remainder = sentence[4:]


# Problem 8
word = "wisdom"
backwards = word[::-1]


# Problem 9
with open('c:\\CS101\\BoM.txt', 'r', encoding='utf-8') as file:
    bom = file.read()

samCount = bom.count("Sam")


# Problem 10
almaStart = 538993
helamanStart = 1004127

alma = bom[almaStart:helamanStart]

chapterCount = alma.count("Alma Chapter")
almaCount = alma.count("Alma") - chapterCount


# Problem 11
firstPos = bom.find("Mosiah")
secondPos = bom.find("Mosiah", firstPos + 1)





        

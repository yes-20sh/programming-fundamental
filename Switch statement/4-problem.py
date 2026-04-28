'''
Write a program to input vowels and print any word starting from that letter using switch case.
You can print any word, provided the starting letter should be the input as provided by the user.
Assumption: all inputs are in lower case.

'''

vowel = input("Enter the vowel : ")

match vowel:
    case "a" | "A":
        print("Apple")
    case "e" | "E":
        print("Eat")
    case "i" | "I":
        print("Ice")
    case "o" | "O":
        print("Orange")
    case "u" | "U":
        print("Umbrella")

from emoji_translate import Translator
print("Welcome to emoji translator")

emo = Translator(exact_match_only=False, randomize=True)
choice=0
print("Enter a Choice \n 1 for translate sentence into emosentence \n 2 for translate emosentence into sentnce \n 3 for Add positive mood emojis to sentences \n 4 for Add negative mood emojis to sentences \n 5 for Add neutral mood emojis to sentences \n 0 for exit ")

while choice is not None:
    try :
        choice = int(input("Your choice:"))
    except :
        print("Please Enter a valid choice 🥴")
        continue
    if choice==1 :
        sentence=input("Enter text to convert")
        print("Your translated emosentence is: "+ emo.emojify(sentence))
    elif choice==2 :
        sentence = input("Enter a emojis to convert")
        print("Your translated sentence is: " + emo.demojify(sentence))
    elif choice == 3:
        sentence = input("Enter your sentence")
        print("Your translated sentence is: " + emo.add_positive_emojis(sentence, num=1))
    elif choice == 4:
        sentence = input("Enter your sentence")
        print("Your translated sentence is: " + emo.add_negative_emojis(sentence, num=2))
    elif choice == 5:
        sentence = input("Enter your sentence")
        print("Your translated sentence is: " + emo.add_neutral_emojis(sentence, num=3))
    elif choice > 5:
        print("Invalid choice try again🙁 ")
    else :
        print("Thanks for using translator!")
        break






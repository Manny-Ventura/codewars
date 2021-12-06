#https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!

#Here's the deal:

    #It must start with a hashtag (#).
    #All words must have their first letter capitalized.
    #If the final result is longer than 140 chars it must return false.
    #If the input or the result is an empty string it must return false.


def generate_hashtag(s):
    splits = s.split(" ")
    final_string = "#"
    if splits == None or s == "" or len(s) > 140:
        return False
    else:
        for split in splits:
            letter_index = 0
            while letter_index < len(split):
                current_letter = split[letter_index]
                if letter_index == 0:
                    final_string += current_letter.upper()
                else:
                    final_string += current_letter.lower()
                letter_index += 1
    return final_string
generate_hashtag("CodeWars is nice")
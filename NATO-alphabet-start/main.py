incorrect=True
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alphabet=pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict={row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

while  incorrect:
    word=input("Enter a word: ").upper()
    Word_split=list(word)

    try:
        result=[nato_dict[letter] for letter in Word_split]
    except:
        print("please enter on letters : ")
        pass
    else:
        incorrect = False
        print(result)

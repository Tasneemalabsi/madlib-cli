import re

print("""
         welcome to madlib game
        
          please read the file then follow the instruction to complete the game
 """)

my_file = ""
path2 = 'assets/madlib.txt'


def read_template(path):
    "this function takes a path of file as an argument and read this file if the path works correctly, it returns a string which is the text in this file and returns an error (FileNotFoundError)if the file's path is not valid"
    try:
        with open(path) as file:
            my_file = file.read()
            return(my_file)

    except:
        raise FileNotFoundError
read_template(path2)
print(read_template(path2))        


def parse_template(text):
    """
this function takes a string as an argument and follows a pattern to parse this string and take the words that matches this pattern from the string, then append these words to a list
it returns the parsed text and the tuple of the words

    """
    arr = []
    #find the pattern that should followed to cut the string
    pattern = '\{[a-zA-Z0-9\' -]*\}'
    new_text = re.sub(pattern, "{}", text)

    #iterate over the text and append the resulting words to an array
    while "}" in text:
        index1 = text.index("{")
        index2 = text.index("}")
        word = text[index1+1:index2]
        text = text[index2+1:]
        arr.append(word)
    #convert the array to tuple to pass the test
    tupled_words = tuple(arr)
    return(new_text, tupled_words)



parsed_file, arr = parse_template(read_template(path2))

arr2 = []
# iterate over the array of words to take the user input for everyone of them
for i in range(len(arr)):
    print(f"Enter a/an {arr[i]}")
    user_response = input()
    arr2.append(user_response)
tupled_text2=tuple(arr2)
    

def merge(parsed_text,user_input):
    """
    this function takes the tuple of the user response and merge it with the parsed text
    Arguments: a string which is the resulting parsed text from the parse function and the array of user input
     """
    final_results=parsed_text.format(*user_input)
    return(final_results)

#save the resulting file with the response from the user merged with the parsed text into a written text
with open("assets/edited.txt", "w") as f:

        f.write(merge(parsed_file,tupled_text2))
        

parse_template(read_template(path2))
merge(parsed_file,tupled_text2)
print(merge(parsed_file,tupled_text2))


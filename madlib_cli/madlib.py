import re


my_file = ""
path2 = 'assets/madlib.txt'


def read_template(path):
    "This function takes a path of file as an argument and read this file if the path works correctly, it returns a string which is the text in this file and returns an error (FileNotFoundError)if the file's path is not valid"
    try:
        with open(path) as file:
            my_file = file.read()
            return(my_file)

    except:
        raise FileNotFoundError


def parse_template(text):
    """
    This function takes a string as an argument and follows a pattern to parse this string and take the words that matches this pattern from the string, then append these words to a list
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


def take_input(tupled_words):
    '''Iterate over the array of words to take the user input for each one of them'''
    arr = []
    for i in range(len(tupled_words)):
        print(f"Enter a/an {tupled_words[i]}")
        user_response = input()
        arr.append(user_response)
    tupled_values=tuple(arr)
    return tupled_values
    

def merge(parsed_text,user_input):
    """
    this function takes the tuple of the user response and merge it with the parsed text
    Arguments: a string which is the resulting parsed text from the parse function and the array of user input
     """
    final_results=parsed_text.format(*user_input)
    return(final_results)

def write_the_file (saved_file):
    """
    this function saves the resulting file with the response from the user merged with the parsed text into a written text

    """
    with open("assets/edited.txt", "w") as f:

        written_file=f.write(saved_file)
    return written_file    



if __name__ == "__main__":
    print("""
                                      welcome to madlib game
        
          please read the file then follow the instruction and add your response to each one to complete the game
    """)
    template_str = read_template(path2)

    parsed_file, tupled_words = parse_template(template_str)
    tupled_text = take_input(tupled_words)

    final_results = merge(parsed_file,tupled_text)
    print(final_results)
    write_the_file(final_results)
    
    
    


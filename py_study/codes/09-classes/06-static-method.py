class StringUtils:
    
    # pass 를 쓰더라도 써주는 걸 권장 !! 
    def __init__(self):
        pass
    
    @staticmethod
    def reverse_word(string):
        return string[::-1]

    @staticmethod
    def capitalize_word(string):
        return string.capitalize()

text = 'hello, world'
reverse_text = StringUtils.reverse_word(text)
print(reverse_text) # dlrow ,olleh

capitalize_text = StringUtils.capitalize_word(text)
print(capitalize_text) # Hello, world

def main():
    book_path = "books/frankenstein.txt"
    text = bookRead(book_path)
    num_words = countWords(text)
    chars = countChar(text)
    getReport(num_words,chars,book_path)
    


def bookRead(path):
    with open(path)as f:
        return f.read()

def countWords(text):
    words = text.split()
    return len(words)

def countChar(text):
    chars = {}

    for char in text:
        if(char.isalpha()):
            lChar = char.lower()
            if(lChar in chars):
                chars[lChar]+=1
            else:
                chars[lChar]=1
    
    return chars


def getReport(num_words,chars,book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the doc.")

    charList = list(chars)
    charList.sort()
    for key in charList:
        print(f"The {key} character was found {chars[key]} times.")

    print('-----Report End-----')

main()

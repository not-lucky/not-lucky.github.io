bad_words = ['artist']

with open(r"/content/d-fi/rando.txt") as oldfile, open(r"/content/d-fi/deezer.txt", 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
            

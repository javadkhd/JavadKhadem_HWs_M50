# bla = "bla bla bla\nbla bla bla bla\nbla bla bla\nbla bla bla bla bla"


# with open("text_file_for_maktab.txt", "w") as f:
    # f.write(bla)

 
with open("text_file_for_maktab.txt", "r") as f:
    lines_text = f.readlines()

words = list()
[ words.extend(line.split()) for line in lines_text ]
all_characters = "".join(words)

print(f"number of lines : {len(lines_text)}")
print(f"number of words : {len(words)}")
print(f"number of characters without space : {len(all_characters)}")

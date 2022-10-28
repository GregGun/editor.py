name = input("Bitte geben Sie den Namen des Textdokuments an: ")
fileWriter = open(name, "wt")


while True:
    if fileWriter.write(input("Bitte Text einfügen: ") + "\n").isempty():
        
else:
    fileWriter.close()


#.isempty() um den input zu prüfen
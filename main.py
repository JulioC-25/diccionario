meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL':'una respuesta a una broma',
            'SHEESH':'ligera desaprobación',
            'CREEPY':'aterrador, siniestro',
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    if word == "CRINGE":
        print ("CRINGE: Algo excepcionalmente raro o embarazoso")
    elif word == "LOL":
        print ("LOL: Una respuesta común a algo gracioso",)
    elif word == "ROFL":
        print ("ROFL: una respuesta a una broma",)
    elif word == "SHEESH":
        print ("SHEESH: ligera desaprobación",)
    elif word == "CREEPY":
        print ("CREEPY: aterrador, siniestro",)
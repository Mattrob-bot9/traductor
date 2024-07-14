meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"una cara de risa",
            "CREEPY":"algo aterrador que da miedo",
            "BOOMER":"Persona que se aferra mucho al pasado",
            "PA":"para",
            "TROLlEAR": "hacer una broma"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Todavía no tenemos esta palabra... Pero estamos trabajando en ella.")

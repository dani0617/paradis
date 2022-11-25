def main_ahorcado():
    palabra = "palabra"
    guess = ["_"]*len(palabra)
    w = 0
    tries = 5
    while True:
        t = input()
        flag = True 
        for i,p in enumerate(palabra):
            if p == t:
                flag = True
                guess[i] = p 
                if not flag:
                    w+=1
                    if w==tries:
                        print("ahorcado")
                        break
                    print("".join(guess))
                    if "".join(guess) == palabra or t == palabra:
                        print("ganador")
                        break
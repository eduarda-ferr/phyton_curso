import time
dado=input("Insira seu nome completo: ").strip()
print("analisando os dados... aguarde")
time.sleep(3)

print(f"- Seu nome possui cerca de {len(dado) -dado.count(' ')} letras;")
print(f"- Escrita Maiúscula: {dado.upper()};")
print(f"- Escrita Minúscula: {dado.lower()};")
#print(f"- E seu primeiro nome tem {dado.find(' ')}letras.")
separa= dado.split()
print(f"- E seu primeiro é {separa[0]}, e tem {len(separa[0])} letras.")


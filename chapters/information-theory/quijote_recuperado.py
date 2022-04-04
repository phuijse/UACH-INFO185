# Leemos el dendograma de la primera linea y el texto codificado de la segunda linea


# Convertimos el texto codificado en un string de bits

import ast
with open("../quijote_comprimido.bin", "rb") as f:
    dendograma = ast.literal_eval(f.readline().decode())
    texto_codificado = f.readlines()
    texto_codificado = [valor for k in range(len(texto_codificado)) for valor in texto_codificado[k]]
    texto_codificado = ["{0:08b}".format(valor) for valor in texto_codificado]
    texto_codificado = ''.join(texto_codificado)

print(texto_codificado[:1000])

# Para decodifir necesitamos el dendograma inverso

dendograma_inverso =  {codigo: simbolo for simbolo, codigo in dendograma.items()}
print(dendograma_inverso)

# Vamos comparando bit a bit hasta recuperar el texto original

codigo = ""
texto = ""
for bit in texto_codificado:
    codigo += bit
    if codigo in dendograma_inverso:
        texto += dendograma_inverso[codigo]
        codigo = ""
print(texto)



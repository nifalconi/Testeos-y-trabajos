
# Ejercicio 1
def file_to_bytes(path):
    # rb = read binary
    with open(path, 'rb') as file:
        return bytearray(file.read())


# Ejercicio 2
def to_int(databytes):
    size = len(databytes)
    return sum(databytes[i] << (i * 8) for i in range(size))


# Ejercicio 3
def metadata(data):
    metadata = {}
    metadata['Tamano'] = to_int(data[2:6])
    metadata['Ancho'] = to_int(data[18:22])
    metadata['Alto'] = to_int(data[22:25])
    metadata['Inicio'] = to_int(data[10:14])
    return metadata


# Ejercicio 4
def get_padding(pixel_width):
    res = pixel_width % 4
    if res == 0:
        return 0
    return 4 - res


# Ejercicio 5
def remove_green(source, output):
    data = file_to_bytes(source)
    meta = metadata(data)

    width = 3 * meta['Ancho']
    padded_width = width + get_padding(width)
    height = meta['Alto']
    start = meta['Inicio']

    print("Alto: " + str(height))
    print("Ancho: " + str(width))

    for j in range(0, height):
        for i in range(0, width, 3):
            position = start + j * padded_width + i
            # R G B
            # 0 1 2
            data[position + 1] = 0

    # ¿Qué pasaría si la imagen fuera gigante? (mayor a la capacidad RAM)
    #
    # Una mejor solución es ir escribiendo de a poco
    # durante la iteración.
    with open(output, 'wb') as out:
        out.write(data)
        
        
def grey_measure(rgb):
    average = (sum(a for a in rgb)//3)
    letters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzvunxrjft/\|()1{}[]?-_+~<>i!lI;:, "
    #print(rgb, average, letters[average//4])
    return(letters[average//4])
        
        
def ascii_webeo(source):
    data = file_to_bytes(source)
    meta = metadata(data)

    width = 3 * meta['Ancho']
    padded_width = width + get_padding(width)
    height = meta['Alto']
    start = meta['Inicio']

    #print("Alto: " + str(height))
    #print("Ancho: " + str(width))
    ima_ascii = ""
    
    for j in range(0, height):
        for i in range(0, width, 3):
            position = start + j * padded_width + i
            # R G B
            # 0 1 2
            try:
                get_rgb =[data[position], data[position + 1], data[position + 2]]
                ima_ascii = ima_ascii + grey_measure(get_rgb)+ ""
            except IndexError:
                ima_ascii = ima_ascii + "X"+ ""
                
            #print(get_rgb)
        #ima_ascii = ima_ascii[::-1]
            
        ima_ascii = ima_ascii + "\n"
        
    
    ima_ascii = ima_ascii[::-1]
    
    #print(ima_ascii)

    # ¿Qué pasaría si la imagen fuera gigante? (mayor a la capacidad RAM)
    #
    # Una mejor solución es ir escribiendo de a poco
    # durante la iteración.
    with open("foto.txt", 'w') as out:
        out.write(ima_ascii)
        
ascii_webeo("yo.bmp")
    
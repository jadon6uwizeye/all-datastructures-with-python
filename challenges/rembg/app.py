from rembg import remove

try:
        input_path = 'image_1.png'
        output_path = 'output.png'

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)

except Exception as e:
    print(e)

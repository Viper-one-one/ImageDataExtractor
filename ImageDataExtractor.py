from PIL import Image

def extract_image_data(image_path):
    try:
        with Image.open(image_path).convert("L") as image:
            img = image.resize((128, 64))
            pixels = list(img.getdata())
            #hex_values = [hex(p) for p in pixels]
            bitmap = ' ,'.join([f"0x{p:02X}" for p in pixels])
            print(f"unsigned char image[] = {{ {bitmap} }};")
    except Exception as e:
        print(f"Error extracting image data: {e}")
        return None

def __main__():
    user_input = ""
    print("Welcome to the Image Data Extractor!")
    while user_input != "exit":
        user_input = input("Enter command: ").strip().lower()
        match user_input:
            case "exit":
                print("Exiting the program.")
                break
            case "help":
                print("Available commands: exit, help, extract <image_path>")
            case _ if user_input.startswith("extract "):
                image_path = user_input.split(" ", 1)[1]
                data = extract_image_data(image_path)
                if data:
                    print(f"Image Data: {data}")
            case _:
                print("Unknown command. Type 'help' for available commands.")

if __name__ == "__main__":
    __main__()
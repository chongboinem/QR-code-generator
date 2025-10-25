import qrcode

def get_color_input(prompt, default_value):
    # string input for colour
    user_input = input(f"{prompt} (default: {default_value}): ").strip()
    return user_input if user_input else default_value

def generate_custom_qr():
    # allow users to customize the appearance of the QR code.

    print("\n hie :3 \n you can now generate your own QR Code !! <3 \n ")

    # user can type in the website link 
    website_link = input("enter the website link or text you want to encode: ").strip()
    if not website_link:
        print("oh no ! your link cannot be empty :( aborting...")
        return

    # QR code customization
    
    # the version is automatically calculated by the qrcode library
    version = None 
    
    # size is fixed 
    box_size = 5 # default pixel size of each box
    border = 5   # default thickness of the white border

    # for color; must be hex code or a valid color name
    fill_color = get_color_input("enter fill color (e.g. black, #964B00)", "black")
    back_color = get_color_input("enter background color (e.g. white, #FAFAFA)", "white")

    # to name the output file 
    output_filename = input("enter the output filename you want :D  ").strip()
    if not output_filename.endswith('.png'):
        output_filename += '.png'
    
    print("generating your qr code !! :3")

    try:
        # to initialize QR Code object with custom parameters
        qr = qrcode.QRCode(
            version=version, # version is None so it allows for automatic sizing
            error_correction=qrcode.constants.ERROR_CORRECT_H, # high correction level
            box_size=box_size,
            border=border
        )
        
        # adding data (the link/text)
        qr.add_data(website_link)
        qr.make(fit=True) # ensures that the code fits the data

        # create the image with custom colors
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # saves the image
        img.save(output_filename)
        
        print(f"\n done !! QR Code has been generated and will be saved as: {output_filename}")
        print(f"details: ")
        print(f"link/text: {website_link}")
        print(f"colors: fill={fill_color}, background={back_color}")

    except Exception as e:
        print(f"\n an error occurred during generation :< : {e}")
        print("please check your color names or input values.")


if __name__ == "__main__":
    generate_custom_qr()
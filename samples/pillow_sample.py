from PIL import Image

# Open an image file
with Image.open('oranges.jpg') as img:
    # Display the original image
    img.show()

    # Resize the image
    resized_img = img.resize((200, 200))

    # Display the resized image
    resized_img.show()

    # Save the resized image
    resized_img.save('resized_oranges.jpg')
from PIL import Image


def convert_to_black_and_white(image_path, output_path, resize_factor=1):
    """
    Converts a color image to black and white and optionally resizes it.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output black and white image.
        resize_factor (float): Factor to resize the image. Default is 1 (no resizing).
    """
    # Open the image
    color_image = Image.open(image_path).convert("RGBA")  # Ensure RGBA for transparency

    # Handle transparency
    background = Image.new(
        "RGBA", color_image.size, (255, 255, 255, 255)
    )  # White background
    image_with_background = Image.alpha_composite(background, color_image)

    # Convert to grayscale (black and white)
    bw_image = image_with_background.convert("L")  # "L" mode for grayscale

    # Resize the image if a resize factor is provided
    if resize_factor != 1:
        new_size = (
            int(bw_image.width * resize_factor),
            int(bw_image.height * resize_factor),
        )
        bw_image = bw_image.resize(
            new_size, Image.Resampling.LANCZOS
        )  # Smooth resizing

    # Save the black and white image
    bw_image.save(output_path)
    print(f"Black and white image saved to {output_path}")


# Example usage
convert_to_black_and_white(
    "viper.png", "viperbw.png", resize_factor=0.5
)  # Resizes to 50%

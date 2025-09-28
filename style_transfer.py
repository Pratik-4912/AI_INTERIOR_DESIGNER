from PIL import Image, ImageEnhance

def apply_color_theme(image, theme="modern"):
    """
    Apply color/theme transformation to a PIL image.
    """
    enhancer = ImageEnhance.Color(image)
    if theme == "modern":
        return enhancer.enhance(1.5)  # boost colors
    elif theme == "minimalist":
        return enhancer.enhance(0.7)  # desaturate
    elif theme == "bohemian":
        # boost saturation slightly and apply warm tone
        img = enhancer.enhance(1.3)
        # optional: convert to warmer tone by slightly increasing red channel
        r, g, b = img.split()
        r = r.point(lambda i: min(255, i * 1.1))
        img = Image.merge("RGB", (r, g, b))
        return img
    else:
        return image  # default no change

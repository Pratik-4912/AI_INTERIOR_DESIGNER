import streamlit as st
from PIL import Image
from utils.detection import detect_room_objects
from utils.style_transfer import apply_color_theme
from utils.furniture_api import get_furniture_images
import random
import tempfile

# Streamlit page config
st.set_page_config(page_title="AI Virtual Interior Designer", page_icon="🏠", layout="wide")
st.title("🏠 AI Virtual Interior Designer")
st.write("Upload a room photo and get AI-powered furniture & color suggestions!")

# Upload room image
uploaded_file = st.file_uploader("Upload a room image", type=["jpg", "png"])
if uploaded_file is not None:
    # Save temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    temp_file.close()
    
    # Load image
    image = Image.open(temp_file.name)
    st.image(image, caption="Uploaded Room", use_column_width=True)

    # Detect room objects
    with st.spinner("Detecting furniture and room layout..."):
        try:
            detected_objects = detect_room_objects(temp_file.name)
            st.write("Detected Objects:", detected_objects)
        except Exception as e:
            st.error(f"Error detecting objects: {e}")
            detected_objects = []

    # Apply multiple color/theme suggestions
    themes = ["modern", "minimalist", "bohemian"]
    st.subheader("🎨 Color/Theme Suggestions:")
    for theme_name in themes:
        try:
            themed_image = apply_color_theme(image, theme=theme_name)
            st.write(f"**Theme:** {theme_name.capitalize()}")
            st.image(themed_image, caption=f"{theme_name.capitalize()} Theme", use_column_width=True)
        except Exception as e:
            st.error(f"Error applying {theme_name} theme: {e}")

    # Dynamic furniture suggestions
    with st.spinner("Fetching furniture recommendations..."):
        if detected_objects:
            for obj in detected_objects:
                try:
                    images = get_furniture_images(category=obj, count=10)
                    images = random.sample(images, min(len(images), 5))
                    
                    st.subheader(f"{obj.capitalize()} Suggestions:")
                    for img_url in images:
                        st.image(img_url, width=200)
                except Exception as e:
                    st.error(f"Error fetching {obj} images: {e}")
        else:
            # fallback if no objects detected
            try:
                images = get_furniture_images(category="sofa", count=10)
                images = random.sample(images, min(len(images), 5))
                st.subheader("Furniture Suggestions:")
                for img_url in images:
                    st.image(img_url, width=200)
            except Exception as e:
                st.error(f"Error fetching furniture images: {e}")

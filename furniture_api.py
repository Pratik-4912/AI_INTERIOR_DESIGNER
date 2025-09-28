import requests

def get_furniture_images(category="sofa", count=5):
    access_key = "CsEQ8wbbe2i63QrNP0uLYBkmT-oJXkeqVDPt8TrXLLQ"  # Free tier
    url = f"https://api.unsplash.com/search/photos?query={category}&per_page={count}&client_id={access_key}"
    response = requests.get(url).json()
    images = [item['urls']['small'] for item in response['results']]
    return images

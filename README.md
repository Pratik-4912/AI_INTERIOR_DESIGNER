## 🏠 AI Interior Designer

An **AI-powered virtual interior designer** that helps users visualize and decorate their rooms instantly!
Upload a photo of your room — the app automatically detects furniture, suggests modern color themes, and recommends matching furniture items using AI.

### 🚀 Features

* 🧠 **AI Object Detection** – Detects existing furniture and room layout from an uploaded image.
* 🎨 **Smart Color Themes** – Automatically generates modern, minimalist, and bohemian style previews.
* 🛋️ **Furniture Recommendations** – Fetches real furniture images (via Unsplash API) for better design inspiration.
* ⚡ **Dynamic Suggestions** – Different rooms give unique furniture and theme results.
* 🖼️ **Streamlit UI** – Interactive and user-friendly design interface.

### 🧰 Tech Stack

* **Frontend:** Streamlit
* **AI/ML:** OpenCV / Image Detection API
* **Image Enhancements:** Pillow (PIL)
* **API Integration:** Unsplash API for furniture images

### 💡 How It Works

1. Upload your room image.
2. The system analyzes your furniture and layout.
3. AI generates multiple design themes and furniture ideas.
4. Explore suggestions and get inspired instantly!

### 🔑 Setup Instructions

1. Clone this repository

   ```bash
   git clone https://github.com/yourusername/ai-virtual-interior-designer.git
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Get your **Unsplash API key** from [unsplash.com/developers](https://unsplash.com/developers)
   Add it in `utils/furniture_api.py`
4. Run the app

   ```bash
   streamlit run app.py
   ```

### 📸 Example Output

* Upload room → Get detected furniture list
* View modern, minimalist, and bohemian color versions
* Get top 5 furniture suggestions for your detected items

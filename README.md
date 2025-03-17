# Prompt Optimizer

A web application that helps users optimize their prompts for better AI responses. The application uses Google's Gemini AI model to transform simple prompts into well-structured ones with clear specifications for text and image generation.

## Features

- **Text Prompt Optimization**: Transform basic text prompts into well-structured, effective AI instructions with clear persona, task, context, and format specifications
- **Image Prompt Optimization**: Create optimized image prompts with subject, context, emotion, style, and camera settings
- **Style Selection**: Choose from various style categories for image prompts
- **Multilingual Support**: Switch between English and Vietnamese interfaces
- **User-friendly Interface**: Clean, responsive design built with Tailwind CSS
- **Copy Functionality**: Easily copy optimized prompts to clipboard
- **Responsive Design**: Works on desktop and mobile devices

## Webdemo

[Prompt Optimizer v3.0 - Hosted by Render](https://prompt-optimizer-ag5j.onrender.com)

## Example

- **Text prompt**:  
  **Before:**  
  `Help me write a blog post about climate change`  
  **After:**  
  `As a climate science communicator, write a 500-word blog post that informs the general public about the effects of climate change, focusing on rising sea levels and increased frequency of extreme weather events. The blog post should include a brief explanation of the causes of climate change and suggest actions individuals can take to reduce their carbon footprint. Format the blog post with a clear title, introduction, body paragraphs with headings, and a concluding call to action.`

- **Image prompt**:  
  **Before:**  
  `Draw a mountain landscape at sunset`  
  **After:**  
  `Draw a breathtaking mountain landscape bathed in the warm, golden light of a sunset. The scene evokes a sense of tranquility and awe, with detailed textures and vibrant colors enhancing the natural beauty. Rendered in a realistic style with 4K resolution, the image captures the serene and majestic atmosphere of the mountains. Shot with a wide-angle lens to emphasize the vastness and grandeur of the scenery.`

## Technology Stack

- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **AI**: Google's Gemini 2.0 Flash model via Google's Generative AI SDK

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (you can get one for free from [Google AI Studio](https://aistudio.google.com/apikey))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abcxyz91/prompt-optimizer.git
   cd prompt-optimizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   FLASK_SECRET_KEY=your_secret_key_here
   ```

## Running the Application

1. Make sure your virtual environment is activated.

2. Start the Flask development server:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
prompt-optimizer/
├── app.py                # Main Flask application
├── helpers.py            # Helper functions for the application
├── translations.py       # Translation dictionaries for multilingual support
├── static/
│   ├── css/
│   │   └── styles.css    # Custom CSS styles
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── favicon.ico       # Website favicon
├── templates/
│   ├── base.html         # Base template with common elements
│   ├── index.html        # Text prompt optimization page
│   ├── image.html        # Image prompt optimization page
│   └── partials/
│       ├── header.html   # Header with navigation
│       └── footer.html   # Footer partial
├── .env                  # Environment variables (not tracked in git)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Application Routes

- `/` - Home route for text prompt optimization
- `/image` - Route for image prompt optimization
- `/reset` - Route to reset the user input & response
- `/change_language/<language>` - Route to switch between languages

## Language Support

The application supports:
- Vietnamese (Default)
- English

You can switch between languages using the language toggle in the header.

## Style Categories for Image Prompts

The application offers several style categories for image prompts:
- Realistic
- Cinematic
- Anime
- Digital Art
- Oil Painting
- Watercolor
- Sketch
- Cartoon

You can modify these options by updating the `STYLES` list in `app.py`.

## Deployment

This application can be deployed to various platforms like Heroku, AWS, or Google Cloud Platform. Make sure to set the environment variables in your deployment environment.

## Acknowledgements

- Google Generative AI for providing the Gemini model
- Tailwind CSS for the design framework

## Contact

[Contact me on github](https://github.com/abcxyz91)
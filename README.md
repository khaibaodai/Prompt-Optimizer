# Prompt Optimizer

A web application that helps users optimize their prompts for better AI responses. The application uses Google's Gemini AI model to transform simple prompts into well-structured ones with clear persona, task, context, and format specifications.

## Features

- **Prompt Optimization**: Transform basic prompts into well-structured, effective AI instructions
- **User-friendly Interface**: Clean, responsive design built with Tailwind CSS
- **Copy Functionality**: Easily copy optimized prompts to clipboard
- **Responsive Design**: Works on desktop and mobile devices

## Webdemo

[To be updated later]

## Technology Stack

- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **AI**: Google's Gemini 2.0 Flash model via Google's Generative AI SDK

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key

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
├── static/
│   ├── css/
│   │   └── styles.css    # Custom CSS styles
│   └── js/
│       └── script.js     # JavaScript functionality
├── templates/
│   ├── base.html         # Base template with common elements
│   ├── index.html        # Main application page
│   └── partials/
│       ├── header.html   # Header partial
│       └── footer.html   # Footer partial
├── .env                  # Environment variables (not tracked in git)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Customizing the System Prompt

You can customize how the AI optimizes prompts by modifying the `SYSTEM_INSTRUCTION` variable in `app.py`.

## Deployment

This application can be deployed to various platforms like Heroku, AWS, or Google Cloud Platform. Make sure to set the environment variables in your deployment environment.

## Acknowledgements

- Google Generative AI for providing the Gemini model
- Tailwind CSS for the design framework

## Contact

[[Contact me on github](https://github.com/abcxyz91)]
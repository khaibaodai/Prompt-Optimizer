from google import genai
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, render_template, flash, redirect, url_for, session
import os
import sys
import uuid
from helpers import get_response, validate_environment

# Validate required environment variables
if not validate_environment():
    sys.exit(1)

# Find and load environment variables
_ = load_dotenv(find_dotenv())

# Create a Flask app
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))

# Setup style categories for image prompts
STYLES = ["Realistic", "Cinematic", "Anime", "Digital Art", "Oil Painting", "Watercolor", "Sketch", "Cartoon"]

# Define the home route for a simple text prompt
@app.route("/", methods=["GET", "POST"])
def home():
    """Initialize the chat session and handle user input."""
    if "chat_id" not in session:
        session["chat_id"] = str(uuid.uuid4())

    response = None
    user_input = ""
    
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if not user_input:
            flash("Please enter a prompt", "danger")
            return redirect(url_for("home"))
        
        if len(user_input) > 500:
            flash("Prompt is too long. Please keep it under 500 characters.", "danger")
            return render_template("index.html", user_input=user_input)
        
        prompt = f"""
        You are a helpful AI assistant that specializes in optimizing user's prompts for the best results.
        You must always ensure that the optimized prompt is clear, concise, and well-structured.

        The optimized prompt should include the following 4 areas:
        1. Persona: Clearly define the user's persona or role.
        2. Task: Describe the specific task or goal that the user wants to achieve.
        3. Context: Provide relevant context or background information for the task.
        4. Format: Specify the format or structure of the expected response.

        If user's prompt is unclear or incomplete, you can generate an optimized prompt as an example.
        Below is the user's prompt:
        <user_prompt>
        {user_input}
        </user_prompt>
        """
        try:
            response = get_response(prompt)
            flash("AI response generated successfully", "success")
            return render_template("index.html", user_input=user_input, response=response)
        except ValueError as e:
            flash(f"Config error: {e}", "danger")
        except genai.APIException as e:
            flash(f"Gemini API error: {e}", "danger")
        except Exception as e:
            flash(f"Unexpected error: {e}", "danger")
    return render_template("index.html")

# Define the image prompt route
@app.route("/image", methods=["GET", "POST"])
def image_prompt():
    """Initialize the chat session and handle user input."""
    if "chat_id" not in session:
        session["chat_id"] = str(uuid.uuid4())

    if request.method == "POST":     
        user_input = request.form.get("user_input", "").strip()
        if not user_input:
            flash("Please enter an image description", "danger")
            return redirect(url_for("image_prompt"))
        
        if len(user_input) > 500:
            flash("Image description is too long. Please keep it under 500 characters.", "danger")
            return render_template("image.html", user_input=user_input, STYLES=STYLES)
        
        style = request.form.get("style")
        if not request.form.get("style"):
            flash("Please select a style category", "danger")
            return redirect(url_for("image_prompt"))
        
        prompt = f"""
        You are a helpful AI assistant that specializes in optimizing user's prompts to generate better image.
        You must always ensure that the optimized description is clear, concise, and well-structured.

        The optimized description should include the following 5 areas:
        1. Subject: Clearly describe the main subject of the image.
        2. Context: Provide relevant context or background information for the image.
        3. Emotion: Capture the emotional tone or mood of the image such as natural, dramatic, cold etc.
        4. Style: Specify the style of the image such as painting, photograph, sketches etc.
        5. Camera settings: Specify the camera settings used to capture the image such as close-up, wide-angle, etc.

        If the image is unclear or ambiguous, you can generate an optimized description as an example in a single paragraph.
        Below is the image description:
        <image_description>
        {user_input} in 4K resolution, high-quality, beautiful with {style} style.
        </image_description>
        """
        try:
            response = get_response(prompt)
            flash("AI response generated successfully", "success")
            return render_template("image.html", user_input=user_input, response=response, STYLES=STYLES)
        except ValueError as e:
            flash(f"Config error: {e}", "danger")
        except genai.APIException as e:
            flash(f"Gemini API error: {e}", "danger")
        except Exception as e:
            flash(f"Unexpected error: {e}", "danger")
    return render_template("image.html", STYLES=STYLES)

# Define the reset session route
@app.route("/reset_session", methods=["POST"])
def reset_session():
    """Reset the session and clear all session data."""
    session.clear()
    flash("Session has been reset", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

from google import genai
from google.genai import types
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, render_template, flash, redirect, url_for, session
import os
import uuid

# Find and load environment variables
_ = load_dotenv(find_dotenv())

# Create a Flask app
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))

# Set up model and system prompt
MODEL = "gemini-2.0-flash"
SYSTEM_INSTRUCTION = """
You are a helpful AI assistant that specializes in optimize prompts for the best results.
You must always ensure that the optimized prompt is clear, concise, and well-structured.

The optimized prompt should include the following 4 areas:
1. Persona: Clearly define the user's persona or role.
2. Task: Describe the specific task or goal that the user wants to achieve.
3. Context: Provide relevant context or background information for the task.
4. Format: Specify the format or structure of the expected response.

If user's prompt is unclear or incomplete, you can generate an optimized prompt as an example.
Your response will be the optimized prompt only.
"""

def get_response(prompt):
    """Create a new chat session for multiple users."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables")
        
        client = genai.Client(api_key = api_key)

        return client.models.generate_content(
            model = MODEL,
            contents=prompt,
            config = types.GenerateContentConfig(
                system_instruction = SYSTEM_INSTRUCTION,
                max_output_tokens = 500,
                temperature = 0.5
            )
        )
    except Exception as e:
        print(f"Error creating chat session: {e}")

# Define the home route
@app.route("/", methods=["GET", "POST"])
def home():
    """Initialize the chat session and handle user input."""
    if "chat_id" not in session:
        session["chat_id"] = str(uuid.uuid4())
    
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            response = get_response(user_input)
            flash("AI response generated successfully", "success")
            return render_template("index.html", user_input=user_input, response=response)
        except Exception as e:
            flash(f"Error processing prompt: {e}", "danger")
    return render_template("index.html")

# Add a route to reset the chat session
@app.route("/reset", methods=["POST"])
def reset_session():
    session.pop('chat_id', None)
    flash("Session resetted", "info")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

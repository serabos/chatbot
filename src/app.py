from flask import Flask, request, jsonify
from llama3_api import query_llama3
from stable_diffusion_api import generate_image

app = Flask(__name__)

@app.route("/")
def home():
    """
    Root endpoint to verify the server is running.
    """
    return "Welcome to the Flask API! Use the /chat endpoint to interact."


@app.route("/chat", methods=["POST"])
def chat():
    """
    Chat endpoint to handle user input and route it to Llama3 or Stable Diffusion.

    Returns:
        JSON: A response containing either text or an image path.
    """
    user_input = request.json.get("prompt")
    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400


    if any(keyword in user_input.lower() for keyword in ["draw", "image", "generate"]):
        # Handle image generation
        image_path = generate_image(user_input)
        return jsonify({"type": "image", "path": image_path})
    else:
        # Handle text-based chat
        response_text = query_llama3(user_input)
        return jsonify({"type": "text", "response": response_text})

if __name__ == "__main__":
    app.run(port=5000)

import requests
import base64

def generate_image(prompt):
    """
    Generates an image using Stable Diffusion WebUI API.

    Args:
        prompt (str): The text prompt for image generation.

    Returns:
        str: Path to the generated image file.
    """
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"  # Default Stable Diffusion WebUI endpoint
    
    payload = {
        "prompt": prompt,
        "steps": 30,  # Number of steps for image generation
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        image_base64 = response.json().get("images")[0]
        image_path = "output.png"
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image_base64))
        return image_path
    except requests.exceptions.RequestException as e:
        return f"Error generating image: {e}"

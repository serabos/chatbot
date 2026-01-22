import requests

def send_prompt(prompt):
    """
    Sends a prompt to the Flask backend and prints the response.

    Args:
        prompt (str): The user input to send to the backend.
    """
    url = "http://127.0.0.1:5000/chat"  # The Flask backend endpoint
       
    payload = {"prompt": prompt}
    
    response = requests.post(url, json=payload)
    
    # Handle the response
    if response.status_code == 200:
        data = response.json()
        
        if data["type"] == "text":
            print("Response from Llama3:", data["response"])
        elif data["type"] == "image":
            print("Generated Image saved at:", data["path"])
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter a prompt for the chatbot: ")
    send_prompt(user_input)

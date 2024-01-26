# Flask Blog Project

This Flask project is used to manage a simple blog site. Users can register, login, logout, add, update, and delete posts. Additionally, users can add comments to posts.

## Getting Started

To run the application, follow the steps below:

1. **Create a Virtual Environment:**
   
        python -m venv venv

  Activate the Virtual Environment:
   
        Windows:
           venv\Scripts\activate

        Linux or macOS:
          source venv/bin/activate

2.**Create a config file:**

       cd micro-blog 
       cat > config.json
        "MONGO_URI": "your_mongo_uri"
        "SECRET_KEY": "your_secret_key"
        ctrl+d //save and close the file
e
3.**Install Dependencies:**

        pip install -r requirements.txt   

4.**Run the Application:**

        python index.py 
        (python3 index.py)
        

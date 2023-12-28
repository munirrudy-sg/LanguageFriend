# LanguageFriend

Welcome to the LanguageFriend app! This guide will walk you through the setup process to get the application up and running on your local machine.

## Prerequisites

Before you start, make sure you have the following installed:

- **Python**: Flask is built with Python. Download and install Python from [python.org](https://www.python.org/).
- **Flask**: If Flask isn't installed, you can install it using pip with `pip install Flask`.
- **Git LFS**: For the large files, you'll need Git LFS. Follow the setup instructions on the [Git LFS website](https://git-lfs.com/) or use your system's package manager.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/inf2002/inf2002-team19-2023.git
   ```

2. Change to the project directory:
   ```bash
   cd inf2002-team19-2023
   ```

3. Initialize and pull files with Git LFS:
   ```bash
   git lfs install
   git lfs pull
   ```

4. Set up and activate the virtual environment:
   - **Linux/Mac**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the LanguageFriend app locally:

1. In the project directory with the virtual environment activated, set the `FLASK_APP` environment variable to `app.py`:
   - **Linux/Mac**:
     ```bash
     export FLASK_APP=app.py
     ```
   - **Windows**:
     ```bash
     set FLASK_APP=app.py
     ```

2. Run the Flask server:
   ```bash
   flask run
   ```
   The server will start, and the CLI will show the URL where the app is hosted, typically `http://127.0.0.1:5000` or `http://localhost:5000`.

3. In your web browser, go to the provided URL. The login page should appear.

4. Use the following credentials to log in:
   - **Username**: inf2002
   - **Password**: 2002

5. After logging in, you can access the main features like "Conversation", "Scenarios", and "Settings".

## Demo

To see the LanguageFriend app in action, check out our demo video:
- [LanguageFriend Demo on YouTube](https://youtu.be/vptRdD3QK44?si=04TwyIxVXFekCUvL)

You can also find the demo video and other important documents such as the gAI declaration in the "Deliverables" folder.

## Additional Information

You can also navigate to additional pages by entering the paths `/about`, `/contact`, `/transcript`, and more in your browser. The routes are defined in the `app.py` file.

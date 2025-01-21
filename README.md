<img src="logo.png" alt="Alt text" width="500" height="200">

# KreedaAI: Exercise Form Analysis

KreedaAI is a web application that uses AI to analyze exercise form from images or video frames. It provides structured feedback, including form correctness, detected issues, recommended corrections, and potential risks.

## Installation and Setup

### Prerequisites

- Python 3.8 or later.
- Install the required Python libraries:
    
    ```bash
    pip install streamlit google-generativeai pillow moviepy 
    ```
    
- A valid Gemini AI API key. Obtain one from the Gemini AI Platform.

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/HiteshNP/IISC.git
```

### Configure Environment Variables

Set up the Gemini API key as an environment variable:

```bash
GEMINI_API_KEY='your_api_key_here'
```
## Running the App

1. Navigate to the project directory.
2. Run the Streamlit application:
    
```bash
streamlit run app.py
```
    
3. Open your browser to the URL provided in the terminal (typically `http://localhost:8501`).

---

## Usage

1. **Upload Media**:
    - Upload an image or video of the exercise you want to analyze.
2. **Specify Exercise (Optional)**:
    - Indicate whether you know the exercise being performed.
    - If yes, enter the exercise name.
3. **Analyze Form**:
    - Click the **Analyze Form** button to receive feedback.
4. **View Results**:
    - Review the structured analysis, which includes:
        - Form correctness.
        - Detected issues.
        - Recommended corrections.
        - Risk assessment.

---

## File Structure

```bash
kreedaai/
|-- app.py               
|-- logo.png              
|-- .env                
```

---

## Example Output
![Screenshot 2025-01-22 001545](https://github.com/user-attachments/assets/fe9d028a-ef9c-44f9-98ad-f1e2b09ee403)

![Screenshot 2025-01-21 234250](https://github.com/user-attachments/assets/fa626262-62a0-495a-8ad7-7c85dada9299)

![Screenshot 2025-01-21 234217](https://github.com/user-attachments/assets/78882fbc-bd92-4e69-b590-a76358f102fb)

## Contributing

We welcome contributions to improve KreedaAI. To contribute:

1. Fork the repository.
2. Create a feature branch:
    
    ```bash
    git checkout -b feature-name
    ```
    
3. Commit your changes:
    
    ```bash
    git commit -m "Add feature name"  
    ```
    
4. Push to the branch:
    
    ```bash
    git push origin feature-name
    ```
    
5. Open a pull request.

---

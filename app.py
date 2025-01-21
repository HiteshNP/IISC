import streamlit as st
import google.generativeai as genai
import PIL.Image
from pathlib import Path
import os
from moviepy.editor import VideoFileClip

# Configure the Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

def analyze_exercise(image, exercise_name=None):
    """Analyze exercise form using Gemini API"""
    if exercise_name:
        prompt = f"""You are an expert fitness trainer. Analyze this image/video frame of someone performing a {exercise_name}.
        1. Is the form correct? Give a yes/no answer.
        2. What specific form issues do you notice, if any?
        3. What corrections should be made?
        4. What are the potential risks of incorrect form?
        
        Format your response as:
        Form Correct: [Yes/No]

        Issues Detected: [List specific issues]

        Recommended Corrections: [List corrections]
        
        Risk Assessment: [List potential risks]
        """
    else:
        prompt = """You are an expert fitness trainer. Please:
        1. Identify what exercise is being performed in this image/video frame
        2. Is the form correct? Give a yes/no answer.
        3. What specific form issues do you notice, if any?
        4. What corrections should be made?
        5. What are the potential risks of incorrect form?
        
        Format your response as:
        Exercise Identified: [Name of exercise]

        Form Correct: [Yes/No]

        Issues Detected: [List specific issues]

        Recommended Corrections: [List corrections]

        Risk Assessment: [List potential risks]
        """
    
    response = model.generate_content([prompt, image])
    return response.text

def extract_frame(video_path, frame_time=1.0):
    """Extract a frame from video for analysis"""
    clip = VideoFileClip(video_path)
    frame = clip.get_frame(frame_time)
    clip.close()
    return PIL.Image.fromarray(frame)

def main():
    st.set_page_config(page_title="KreedaAI - Exercise Form Analysis", layout="centered")
    
    # Header
    st.markdown("""
    <style>
        .header {
            text-align: center;
            font-size: 40px;
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
        }
        .subheader {
            text-align: center;
            font-size: 20px;
            color: #757575;
            font-family: 'Arial', sans-serif;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #757575;
            font-family: 'Arial', sans-serif;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
        }
        .upload {
            margin-top: 20px;
        }
        .markdown-text {
            font-family: 'Arial', sans-serif;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Logo (Paste the path of your image here)
    import base64

    logo_path = "logo.png"
    with open(logo_path, "rb") as image_file:
        logo_base64 = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='200'/>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("<div class='subheader'>AI-Powered Exercise Form Analysis</div>", unsafe_allow_html=True)

    # File upload
    uploaded_file = st.file_uploader("Upload an image or video of your exercise", type=['png', 'jpg', 'jpeg', 'mp4', 'mov'])
    
    if uploaded_file:
        # Create a temporary file to save the uploaded content
        temp_path = Path("temp") / uploaded_file.name
        temp_path.parent.mkdir(exist_ok=True)
        
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getvalue())
            
        # Process based on file type
        file_type = uploaded_file.type.split('/')[0]
        
        if file_type == "image":
            image = PIL.Image.open(temp_path)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        elif file_type == "video":
            st.video(temp_path)
            image = extract_frame(str(temp_path))
            st.image(image, caption="Extracted Frame for Analysis", use_container_width=True)
            
        # Exercise identification
        exercise_known = st.radio("Do you know which exercise you're performing?", ["Yes", "No"], key="exercise_known")
        
        exercise_name = None
        if exercise_known == "Yes":
            exercise_name = st.text_input("Enter the name of the exercise:", key="exercise_name")
            
        if st.button("Analyze Form", key="analyze_button"):
            with st.spinner("Analyzing exercise form..."):
                analysis = analyze_exercise(image, exercise_name)
                
            st.markdown("### Analysis Results")
            st.markdown(f"<div class='markdown-text'>{analysis}</div>", unsafe_allow_html=True)
            
        # Cleanup
        os.remove(temp_path)
            
    # Footer
    st.markdown("<div class='footer'>KreedaAI helps you perfect your exercise form with AI-powered analysis</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

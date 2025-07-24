import gradio as gr
import os
import time
from dotenv import load_dotenv

load_dotenv()
if not os.environ.get("MISTRAL_API_KEY"):
    raise EnvironmentError("MISTRAL_API_KEY not found")

from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.05,
    max_retries=2,
)

def generate_plan(weight, height, activity, age, goal, sleep_hours, progress=gr.Progress()):
    
    # Step 1: Input validation and preparation
    progress(0.1, desc="📋 Validating input parameters...")
    time.sleep(0.5)  # Small delay to make progress visible
    
    # Basic input validation
    if not all([weight > 0, height > 0, age > 0, sleep_hours >= 0]):
        progress(1.0, desc="❌ Invalid input parameters")
        return "**Error:** Please ensure all numeric values are valid and positive."
    
    progress(0.2, desc="📊 Calculating BMI and metabolic data...")
    time.sleep(0.5)
    
    # Calculate BMI for context
    bmi = weight / ((height/100) ** 2)
    
    progress(0.4, desc="🤖 Preparing AI prompt...")
    time.sleep(0.3)
    
    messages = [
        ("system", """You are a veteran nutritionist who always responds in formatted **Markdown**. 
        Provide a comprehensive diet plan with:
        - Daily calorie targets
        - Meal timings and portion sizes
        - Macro/micronutrient breakdowns
        - Food recommendations (no whey protein)
        - Hydration guidelines
        - Any relevant health considerations
        
        Format your response with clear headers, bullet points, and tables where appropriate."""),
        ("human", f"""
        Please create a personalized diet plan for:
        - Weight: {weight} kg
        - Height: {height} cm (BMI: {bmi:.1f})
        - Activity Level: {activity}
        - Age: {age} years
        - Fitness Goal: {goal}
        - Sleep Duration: {sleep_hours} hours/day
        
        Provide a detailed diet plan with specific recommendations.
        """)
    ]
    
    progress(0.6, desc="🔄 Sending request to AI model...")
    time.sleep(0.2)
    
    try:
        # Make the API call
        response = llm.invoke(messages)
        progress(0.8, desc="📝 Processing AI response...")
        time.sleep(0.3)
        
        # Extract content
        content = response.content
        
        progress(0.95, desc="✨ Finalizing diet plan...")
        time.sleep(0.2)
        
        progress(1.0, desc="✅ Diet plan generated successfully!")
        
        return content
        
    except Exception as e:
        progress(1.0, desc="❌ Error occurred")
        return f"**Error:** Failed to generate diet plan. Please try again.\n\n*Error details: {str(e)}*"

# Create the Gradio interface
with gr.Blocks(title=" Diet Plan Generator") as iface:
    gr.Markdown("""
    # Personalized Diet Plan Generator
    
    Enter your personal information below to receive a **comprehensive, AI-generated diet plan** 
    tailored to your specific needs and goals.
    
    *All plans are formatted in Markdown with detailed macro/micronutrient breakdowns.*
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Physical Stats")
            weight = gr.Slider(
                minimum=30, 
                maximum=200, 
                step=0.5, 
                value=70, 
                label="Weight (kg)"
            )
            height = gr.Slider(
                minimum=100, 
                maximum=280, 
                step=0.5, 
                value=170, 
                label="Height (cm)"
            )
            age = gr.Slider(
                minimum=16, 
                maximum=80, 
                step=1, 
                value=30, 
                label="Age (years)"
            )
            
        with gr.Column(scale=1):
            gr.Markdown("### 🏃‍♂️ Lifestyle")
            activity = gr.Dropdown(
                choices=[
                    "Sedentary (office job, no exercise)",
                    "Light (light exercise 1-3 days/week)",
                    "Moderate (exercise 3-5 days/week)",
                    "Active (hard exercise 6-7 days/week)",
                    "Very Active (physical job + exercise)",
                    "Extra Active (athlete/very intense training)"
                ],
                value="Moderate (exercise 3-5 days/week)",
                label="Activity Level"
            )
            sleep_hours = gr.Slider(
                minimum=4, 
                maximum=12, 
                step=0.5, 
                value=8, 
                label="Sleep Hours per Day"
            )
            goal = gr.Textbox(
                lines=3,
                placeholder="e.g., Lose 10kg in 3 months, Build muscle mass, Maintain current weight, Improve energy levels...",
                label="Fitness/Health Goal",
                value="Maintain healthy weight and improve energy levels"
            )
    
    with gr.Row():
        generate_btn = gr.Button("🎯 Generate My Diet Plan", variant="primary", size="lg")
        clear_btn = gr.Button("Clear", variant="secondary")
    
    with gr.Row():
        output = gr.Markdown(
            label="Your Personalized Diet Plan",
            value="*Your diet plan will appear here after generation...*"
        )
    

    generate_btn.click(
        fn=generate_plan,
        inputs=[weight, height, activity, age, goal, sleep_hours],
        outputs=output,
        show_progress=True  # This enables the progress bar
    )
    
    clear_btn.click(
        lambda: "*Your diet plan will appear here after generation...*",
        outputs=output
    )

# Launch the interface
if __name__ == "__main__":
    iface.queue(max_size=10).launch(
        inline=True,
        share=True,
        show_error=True
    )

# 🥗 AI Diet Plan Generator

A simple AI-powered web app that generates personalized diet plans based on user physical and lifestyle data.

🚀 **Live Demo**: [Hugging Face Space](https://huggingface.co/spaces/jobannagra/diet_plan)

---

## 📌 Features

* Generates diet plans tailored to individual physical and lifestyle stats
* Uses **Mistral-7B v0.3** LLM for natural language generation
* Lightweight and intuitive frontend with **Gradio**
* Seamlessly integrated with **LangChain** for API calls

---

## 🧠 Tech Stack

| Layer     | Technology                                                |
| --------- | --------------------------------------------------------- |
| Frontend  | [Gradio](https://gradio.app) (using `app_row` for layout) |
| Backend   | [LangChain](https://www.langchain.com/) for calling LLM   |
| LLM Model | Mistral-7B v0.3 (via API)                                 |
| Hosting   | [Hugging Face Spaces](https://huggingface.co/spaces)      |

---

## 📁 Project Structure

```bash
diet_plan/
├── app.py           # Basic implementation to test functionality
├── app_row.py       # Main Gradio UI using row layout
├── mod.ipynb        # Jupyter notebook used for initial testing of the model and API
├── README.md        # You're here!
```

---

## 🔧 Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://huggingface.co/spaces/jobannagra/diet_plan
   cd diet_plan
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app_row.py
   ```

---

## 📋 Notes

* `app.py` is a minimal version to ensure the pipeline works end-to-end
* `app_row.py` is the enhanced version using Gradio's row-based layout
* `mod.ipynb` was used during prototyping to verify model and API response

---

## 🤖 Model Info

* **Model**: Mistral-7B v0.3
* **Accessed via**: LangChain API wrappers
* **Purpose**: Generate coherent and customized diet plans

---


## 📬 Contact

Created by **[jobannagra](https://huggingface.co/jobannagra)**
Feel free to reach out for suggestions or collaborations!

---

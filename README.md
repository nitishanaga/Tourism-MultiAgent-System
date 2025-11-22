# 🌍 Tourism Multi-Agent System (FastAPI)

## 🌟 Project Overview

This is a multi-agent AI system developed using **FastAPI** that functions as a comprehensive tourism and travel assistant. The application is designed to orchestrate three distinct agents to provide users with accurate, real-time weather forecasts and personalized tourist attraction recommendations for any city worldwide.

### Architecture

The application strictly adheres to the **Parent-Child Agent Model** required by the assignment:

* **Parent Agent (`ParentAgent`):** Acts as the primary orchestrator, handling user intent detection, location extraction, and combining the results from the child agents.
* **Child Agent 1 (`WeatherAgent`):** Fetches real-time weather data.
* **Child Agent 2 (`PlacesAgent`):** Finds local tourist attractions.

---

## 🔗 Submission Details and Links

| Component | Status | Link |
| :--- | :--- | :--- |
| **Public Repository** | ✅ Complete | [**INSERT YOUR GITHUB REPO LINK HERE**] |
| **Live Deployment** | ✅ Deployed | [**INSERT YOUR DEPLOYED APPLICATION LINK HERE**] |
| **Dependencies** | ✅ Detailed | See `requirements.txt` |

---

## 💡 Summary of Approach and Key Decisions

### API Usage & Data Sourcing

We implemented the required API sources for external data:
* **Weather:** Uses the **Open-Meteo API**.
* **Places:** Uses a reliable two-step approach: **Nominatim API** for precise coordinate lookup, followed by **Overpass API** queries to find tourist nodes/ways near those coordinates.

### Logic and Intent Control (Critical Decisions)

1.  **Strict Intent Separation:** The final logic ensures the system only returns what the user explicitly asks for. A query for "weather" will **not** automatically return a list of places. This avoids unnecessary processing and ambiguity.
2.  **Robust Location Extraction:** The `ParentAgent` uses specific regular expressions to reliably extract the target city (e.g., "Tokyo," "Bangalore") from conversational sentences (e.g., "what is the weather in tokyo").
3.  **UI/UX:** The front-end was styled with a high-contrast **Dark Theme** to provide a professional, visually appealing interface.

---

## ⚙️ Local Setup and Running Instructions

### Prerequisites

* Python 3.9+
* `pip` (Python package installer)

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL]
    cd Tourism-MultiAgent-System
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate # macOS/Linux
    ```

3.  **Install Detailed Dependencies:**
    The `requirements.txt` file (generated via `pip freeze`) contains all necessary package versions.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    uvicorn app:app --reload
    ```
    The application will be accessible at: `http://127.0.0.1:8000`

---

## 🧪 Testing and Examples

The system handles three types of queries as required:

| Scenario | Input Example | Expected Agent Calls | Output Format |
| :--- | :--- | :--- | :--- |
| **Weather Only** | `What is the temperature in Sydney?` | `WeatherAgent` only. | "In Sydney it's currently X°C..." |
| **Places Only** | `Plan my trip to Sydney.` | `PlacesAgent` only. | "In Sydney these are the places you can go, [List]" |
| **Combined** | `I'm going to Tokyo, what is the climate and where can I visit?` | Both Agents. | "In Tokyo it's currently X°C... And these are the places you can go: [List]" |

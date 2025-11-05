# 🗣️ LiveKit Voice Assistant

This is a real-time voice assistant built using **LiveKit Agents for Python**. It uses an **OpenAI Realtime Model** pipeline with LiveKit's **noise cancellation** plugin to provide a low-latency, conversational experience.

You can interact with this agent via your terminal, the LiveKit Agents Playground, or any application using LiveKit Client SDKs.

## 🚀 Quick Setup

Follow these steps to get the voice assistant running on your local machine.

### 1. Requirements

* **Python** (>= 3.9)
* **uv** package manager (recommended by LiveKit)
* **LiveKit Cloud Account** (for API keys and server URL)
* **OpenAI Platform Account** (for the `OPENAI_API_KEY`)
* **LiveKit CLI** (for authentication and deployment)

### 2. LiveKit CLI & Authentication

If you haven't already, install the LiveKit CLI and link it to your LiveKit Cloud project:

1.  **Install LiveKit CLI:**
    ```bash
    # For macOS/Linux (Homebrew)
    brew install livekit/livekit/livekit-cli
    ```
2.  **Authenticate with Cloud:**
    ```bash
    lk cloud auth
    ```
    This opens a browser window to link your GitHub project to the CLI.

### 3. Project Initialization

Assuming your project directory is the current working directory:

1.  **Install Dependencies:**
    We are installing `livekit-agents` with the `openai` plugin, and the `noise-cancellation` plugin, along with `python-dotenv` to load secrets.
    ```bash
    uv add "livekit-agents[openai]~=1.2" "livekit-plugins-noise-cancellation~=0.2" "python-dotenv"
    ```

2.  **Set Environment Variables:**
    First, retrieve your LiveKit credentials:
    ```bash
    lk app env -w
    ```
    This command creates the necessary **`.env.local`** file. You must then **manually add your OpenAI API Key** to that file:

    ```ini
    # .env.local
    LIVEKIT_API_KEY=<Your LiveKit API Key>
    LIVEKIT_API_SECRET=<Your LiveKit API Secret>
    LIVEKIT_URL=wss://<your-project-url>.livekit.cloud
    OPENAI_API_KEY=<Your OpenAI API Key>
    ```

3.  **Download Model Files:**
    The noise cancellation plugin requires local model files.
    ```bash
    uv run agent.py download-files
    ```

## 🎙️ Running the Agent

You can run the agent in two primary modes:

### A. Console Mode (Terminal Test)

Run the agent locally within your terminal. It listens for your speech and responds directly in the console.

```bash
uv run agent.py console
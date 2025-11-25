# 🗣️ Realtime-Voice-AI-Agent (LiveKit)

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
    uv run main.py download-files
    ```

## 🎙️ Running the Agent

You can run the agent in two primary modes:

### A. Console Mode (Terminal Test)

Run the agent locally within your terminal. It listens for your speech and responds directly in the console.

```bash
python main.py console
```
or 

```bash
uv run main.py console
```

### B. Dev Mode

This mode starts your agent in dev mode to connect it to LiveKit and make it available from anywhere on the internet:

```bash
python main.py dev
```
or 

```bash
uv run main.py dev
```

## 🚀 Part 2: Local Hosting (React Frontend) Setup

This part uses the official LiveKit Agent Starter for React to create a modern web client. [Official Live Agent Starter](https://github.com/livekit-examples/agent-starter-react)


### 2.1. Frontend Initialization

1.  **Clone the React Starter:**
    Run this command in a **separate directory** (outside your Python agent project) to create the Next.js frontend project.
    ```bash
    lk app create --template agent-starter-react
    ```
2.  **Install Node.js Packages:**
    Navigate into the newly created React project directory (e.g., `agent-starter-react`) and install dependencies using `pnpm`.
    ```bash
    pnpm install
    ```

### 2.2. Frontend Configuration

1.  **Set LiveKit Credentials (`.env.local`):**
    Create a `.env.local` file in the **root of the React project directory** and add your LiveKit credentials. These credentials are used by the frontend to connect to the LiveKit server.

    ```ini
    # .env.local (in the React project folder)
    LIVEKIT_API_KEY=<Your LiveKit API Key>
    LIVEKIT_API_SECRET=<Your LiveKit API Secret>
    LIVEKIT_URL=https://your-livekit-server-url
    ```
    > **Note:** Use the **`https://` (non-websocket)** format for the `LIVEKIT_URL` in this frontend configuration.

### 2.3. Running the Frontend

Start the Next.js development server:

```bash
pnpm dev
```

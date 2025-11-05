from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation, silero, deepgram
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv(".env")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant.
            "Keep your answers short and conversational, like you are speaking "
            "in a real-time audio chat.
            """,
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt= deepgram.STT(model="nova-3"),
        llm= "openai/gpt-4.1-mini",
        tts= "cartesia/sonic-3:9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",

        vad= silero.VAD.load(),

        turn_detection= MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
"""RunPod handler → accepts {input: {b64audio}} JSON, returns transcript."""
import base64, io, runpod
from fastapi.testclient import TestClient
import app as asr_app
client = TestClient(asr_app.app)

def handler(event):
    b64 = event["input"].get("b64audio")
    if not b64:
        return {"error": "Missing b64audio"}
    audio = base64.b64decode(b64)
    resp  = client.post("/transcribe", files={"file": ("mic.wav", io.BytesIO(audio), "audio/wav")})
    return resp.json()

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
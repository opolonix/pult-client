from fastapi import FastAPI, Request

import uvicorn
import pyautogui

app = FastAPI()

@app.get("/keyboard")
async def keyboard(key: str) -> dict:
    keys = key.split('+')
    pyautogui.hotkey(keys)
    return {"ok": True}

@app.get("/mouseMove")
async def mouse_move(x: float, y: float) -> dict:
    
    start_x, start_y = pyautogui.position()
    end_x, end_y = start_x+x, start_y+y

    steps = 100

    step_x = (end_x - start_x) / steps
    step_y = (end_y - start_y) / steps

    for i in range(steps + 1):
        pyautogui.moveTo(start_x + i * step_x, start_y + i * step_y, _pause=False)

    return {"ok": True}

@app.get("/mouseClick")
async def mouse_click() -> dict:
    pyautogui.click()

    return {"ok": True}

@app.get("/deviceName")
async def device_name() -> str:
    import config
    return config.DEVICE_NAME

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7743, reload=True)

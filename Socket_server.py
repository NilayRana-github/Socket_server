import asyncio
import websockets

async def receive_values(websocket, path):
    # Sample values
    TC = (8.9, 5.6, 7.3)
    TAP = (2, 3, 4)
    MC = (9, 7, 8)
    LC = (1, 2, 1)
    MM = (-1, 2, 3)
    LM = (9, 9, 4)
    AC = (6, 3, 3)

    values = [TC, TAP, MC, LC, MM, LM, AC]  # All values to send
    
    for val in values:
        await websocket.send(str(val))
        await asyncio.sleep(1)  # Add a delay if needed

async def start_server():
    server = await websockets.serve(receive_values, '127.0.0.1', 8080)
    print("Server started...")
    await server.wait_closed()

asyncio.get_event_loop().run_until_complete(start_server())
asyncio.get_event_loop().run_forever()

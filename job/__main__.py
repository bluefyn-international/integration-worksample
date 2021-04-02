import asyncio

import worker

if __name__ == "__main__":
    worker.init()
    asyncio.get_event_loop().run_forever()

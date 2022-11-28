
import asyncio


async def common_task(idx: int):
    print(f"common_task - start: {idx}")
    await asyncio.sleep(2)
    print(f"common_task - end: {idx}")


async def main():
    print("-- main ---")
    tasks = []
    for i in range(10):
        tasks.append(
            asyncio.create_task(common_task(i))
        )

    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

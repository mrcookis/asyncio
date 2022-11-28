
import asyncio


def standard_method():
    print("standard_method")


async def task():
    print(f"task - start")

    await asyncio.sleep(1)
    standard_method()

    print(f"task - end")


async def main():
    print("-- main ---")

    await task()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())


import asyncio
import pathlib


async def list_directory(curr_path: pathlib.Path, task_id: int):
    tabs = "".join(['\t'] * task_id)
    for item in curr_path.iterdir():
        if item.is_dir():
            await list_directory(item, task_id)
            await asyncio.sleep(0)
        else:
            print(f"common_task-item: {tabs}{item.name}")


async def listdir_task(task_id: int):
    print(f"common_task - start: {task_id}")

    await list_directory(pathlib.Path(), task_id)

    print(f"common_task - end: {task_id}")


async def main():
    tasks = []
    for i in range(3):
        tasks.append(
            asyncio.create_task(listdir_task(i))
        )

    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
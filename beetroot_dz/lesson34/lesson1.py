import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('....world')
    return "yes"

async def main1():
    return "Yes"

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
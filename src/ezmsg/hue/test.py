import asyncio
from hue import Bridge, Light

# Create a light object with the light id (number), Bridge IP and user
light = Light(3, ip="192.168.10.2", user="67kKmg011mCvtRVbzb4UoKjlGaL7bhAjdsKkX7bY")

# from an async function
async def main():
  await Bridge.discover()

  while True:
    print('on')
    await light.power_on()
    await asyncio.sleep(1.0)
    print('off')
    await light.power_off()
    await asyncio.sleep(1.0)

# or from a sync context
if __name__ == '__main__':
  asyncio.run(main())
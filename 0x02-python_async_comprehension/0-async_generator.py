#!/usr/bin/env python3
'''
coroutine called async_generator
that takes no arguments.
'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Waits for a random delay between 0 and max_delay."""
    for i in range(10):
        await asyncio.sleep(1)  # wait for 1 second
        yield random.uniform(0, 10)  # yield a random number between 0 and 10

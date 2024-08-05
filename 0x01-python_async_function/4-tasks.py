#!/usr/bin/env python3
""" Aysncio tasks creation """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Executes func n times and returns ASC delays
    """
    tsks = [task_wait_random(max_delay) for t in range(n)]

    wait_times = await asyncio.gather(*tsks)
    return sorted(wait_times)

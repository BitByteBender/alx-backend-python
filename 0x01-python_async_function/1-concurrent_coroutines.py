#!/usr/bin/env python3
""" Multiple coroutinesat the same time with async """
import asyncio
import heapq
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Calls wait_random multiple times with max delay
    """
    tsk = [wait_random(max_delay) for t in range(n)]
    delays = await asyncio.gather(*tsk)

    heapq.heapify(delays)
    sorter = [heapq.heappop(delays) for h in range(len(delays))]
    return sorter

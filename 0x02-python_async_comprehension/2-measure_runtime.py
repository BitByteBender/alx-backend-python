#!/usr/bin/env python3
""" Measuring runtime """
import asyncio
import time
from importlib import import_module


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
         Measures the total runtime of exec async comprehension four times
         in parallel
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for r in range(4)))
    end = time.perf_counter()
    return end - start

#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List
from importlib import import_module


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Collects 10 random nums using an async comprehension
    """
    return [n async for n in async_generator()]

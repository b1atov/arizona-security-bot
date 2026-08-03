import redis.asyncio as aioredis
import os
import secrets
import math

client = aioredis.Redis(
    host=os.getenv("redis_host", "localhost"),
    port=int(os.getenv("redis_port", 6379)),
    password=os.getenv("redis_password", None),
    db=0,
    decode_responses=True,
)

async def generate_code(userId):
    key = f"code_cooldown:{userId}"

    if not await client.set(name=key, value="", ex=600, nx=True):
        ttl_seconds = await client.ttl(key)
        ttl_minutes = max(1, math.ceil(ttl_seconds / 60)) if ttl_seconds > 0 else 1
        return None, ttl_minutes

    while True:
        code = f"{secrets.randbelow(1_000_000):06d}"
        code_key = f"active_code:{code}"

        if await client.set(name=code_key, value=userId, ex=600, nx=True):
            await client.set(name=key, value=code, ex=600)
            return code, 0

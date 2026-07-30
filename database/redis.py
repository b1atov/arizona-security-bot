import aioredis
import os
import random

client = aioredis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD", None),
    db=0,
    decode_responses=True,
)

async def generate_code(userId):
    key = f"code_cooldown:{userId}"

    ttl_seconds = await client.ttl(key)

    if ttl_seconds > 0:
        ttl_minutes = round(ttl_seconds / 60, 1)
        return None, ttl_minutes

    while True:
        code = f"{random.randint(0, 999999):06d}"
        code_key = f"active_code:{code}"

        code_exists = await client.exists(code_key)

        if not code_exists:
            async with client.pipeline(transaction=True) as pipe:
                pipe.set(name=key, value=code, ex=600)
                pipe.set(name=code_key, value=userId, ex=600)
                await pipe.execute()
            break

    return code, 0
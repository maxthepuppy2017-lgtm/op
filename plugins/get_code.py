try:
    from telethon.sessions import StringSession
    import asyncio, re, json
    from kvsqlite.sync import Client as uu
    from telethon.tl.types import KeyboardButtonUrl
    from telethon.tl.types import KeyboardButton
    from telethon import TelegramClient, events, functions, types, Button
    import time, datetime
    from datetime import timedelta
    from telethon.errors import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        PhoneCodeInvalidError,
        PhoneCodeExpiredError,
        SessionPasswordNeededError,
        PasswordHashInvalidError
    )
    from plugins.messages import *
    from pyrogram import Client, enums
except:
    os.system("pip install telethon")
    try:
        from telethon.sessions import StringSession
        import asyncio, re, json
        from kvsqlite.sync import Client as uu
        from telethon.tl.types import KeyboardButtonUrl
        from telethon.tl.types import KeyboardButton
        from telethon import TelegramClient, events, functions, types, Button
        import time, datetime
        from datetime import timedelta
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            SessionPasswordNeededError,
            PasswordHashInvalidError
        )
        from plugins import *
        from pyrogram import Client, enums
    except Exception as errors:
        print('An Erorr with: ' + str(errors))
        exit(0)
        
API_ID = "1724716"
API_HASH = "00b2d8f59c12c1b9a4bc63b70b461b2f"

async def get_code(session):
    X = TelegramClient(StringSession(session), api_id=API_ID, api_hash=API_HASH)
    try:
        await X.connect()
        async for x in X.iter_messages(777000, limit=1):
            code_match = re.search(r'\b(\d{5})\b', x.text)
            if code_match:
                code = code_match.group(1)
                return code
            else:
                return "لم يتم العثور"
    except Exception  as a:
        return "لم يتم العثور"

async def change_password(session, old_password, new_password):
    c = Client('::memory::', in_memory=True, api_hash='00b2d8f59c12c1b9a4bc63b70b461b2f', api_id=1724716,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    try:
        await c.change_cloud_password(old_password, new_password)
        await c.stop()
        return True
    except:
        return False
    
async def enable_password(session, new_password):
    c = Client('::memory::', in_memory=True, api_hash='00b2d8f59c12c1b9a4bc63b70b461b2f', api_id=1724716,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    try:
        await c.enable_cloud_password(new_password)
        await c.stop()
        return True
    except:
        return False
    
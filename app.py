import asyncio, time, pytz
from datetime import datetime, timedelta
from pyrogram import Client, filters


API_ID = 38880719  
API_HASH = "9d82bc38c60067d3ffed54959051177c"


app = Client("sniper_bot", api_id=API_ID, api_hash=API_HASH)
tz = pytz.timezone("Asia/Kolkata")

@app.on_message(filters.command("BD", prefixes="/") & filters.me)
async def sniper_msg(client, message):
    try:
        args = message.text.split()
        if len(args) < 5:
            return 
            
        target = args[1]
        ampm = args[-1].upper()
        time_str = args[-2]
        msg_text = " ".join(args[2:-2])

        now = datetime.now(tz)
     
        t = datetime.strptime(f"{time_str} {ampm}", "%I:%M %p").time()
        target_dt = now.replace(hour=t.hour, minute=t.minute, second=0, microsecond=0)
        
        if target_dt < now:
            target_dt += timedelta(days=1)
            
        target_ts = target_dt.timestamp()

        
        async def fire():
            
            sleep_time = target_ts - time.time() - 0.5
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)
            
            
            while time.time() < target_ts:
                pass 
            
           
            await client.send_message(target, msg_text)
        
        asyncio.create_task(fire())
        await message.reply("⚡ Scheduled")
        
    except Exception:
        pass 

if __name__ == "__main__":
    app.run()

"""CoronaVirus LookUp
Syntax: .covid <country>"""
from covid import Covid
covid = Covid(source="worldometers")
from datetime import datetime
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern="covid (.*)"))
async def _(event):
    await event.edit("**🔎 Recupero informazioni...**")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    deaths = covid.get_total_deaths()
    if country_data:
        output_text =  f"**✅ Confermati**   :   {country_data['confirmed']}\n"
        output_text += f"**🦠 Casi attivi**     :   {country_data['active']}\n"
        output_text += f"**☠ Morti**              :   {country_data['deaths']}\n"
        output_text += f"**🏥 Ricoverati**     :   {country_data['recovered']}\n\n"        
        output_text += f"**》    STATISTICA MONDIALE    《**\n\n"                
        output_text += f"**✅ Confermati**   :   {covid.get_total_confirmed_cases()}\n"
        output_text += f"**🦠 Casi attivi**     :   {covid.get_total_active_cases()}\n"
        output_text += f"**☠ Morti**              :   {covid.get_total_deaths()}\n"
        output_text += f"**🏥 Ricoverati**     :   {covid.get_total_recovered()}\n\n"
        output_text += ("**🔄 AGGIORNAMENTO**:  "f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%H:%M')} **[GMT]**\n")
    else:
        output_text = "**Invalid Country name**"
    await event.edit(f"**ℹ️ CORONAVIRUS Info in {country}**:\n\n{output_text}")

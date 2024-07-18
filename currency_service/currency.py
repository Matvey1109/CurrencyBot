import xml.etree.ElementTree as ET

import aiohttp

from currency_service.cache import r


async def fetch_xml(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def update_currency_rates():
    url = "https://cbr.ru/scripts/XML_daily.asp"
    xml_content = await fetch_xml(url)
    root = ET.fromstring(xml_content)

    for valute in root.findall("Valute"):
        char_code = valute.find("CharCode").text
        value = valute.find("Value").text

        key = f"currency:{char_code}"
        r.set(key, value)

    r.close()


async def exchange_currency(
    base_currency: str, target_currency: str, amount: float
) -> str:
    base_currency_value = r.get(f"currency:{base_currency}")
    target_currency_value = r.get(f"currency:{target_currency}")

    r.close()

    if base_currency_value is None:
        return f"Cannot find exchange rate for {base_currency}."

    base_currency_value = float(base_currency_value.decode().replace(",", "."))

    if target_currency == "RUB":
        converted_amount = amount * base_currency_value
        return f"{amount} {base_currency} = {converted_amount} {target_currency}"
    elif target_currency_value is None:
        return f"Cannot find exchange rate for {target_currency}."

    target_currency_value = float(target_currency_value.decode().replace(",", "."))
    converted_amount = amount * (base_currency_value / target_currency_value)
    return f"{amount} {base_currency} = {converted_amount} {target_currency}"


async def get_all_currencies() -> list[str]:
    keys = r.keys("currency:*")
    currencies = []

    for key in keys:
        currency = key.decode().split(":")[1]
        value = r.get(key).decode()
        currencies.append(f"{currency} - {value}")

    r.close()

    return currencies

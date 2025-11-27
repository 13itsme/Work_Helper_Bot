import httpx


async def convert_currency(amount: int, from_currency: str = "USD", to_currency: str = "EUR"):
    """Converting currency using API"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.exchangerate-api.com/v4/latest/USD"
        )
        data = response.json()

        if 'rates' in data and to_currency in data['rates']:
            rate = data['rates'][to_currency]
            return amount * rate
        else:
            return None
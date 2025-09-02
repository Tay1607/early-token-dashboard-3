import requests

def get_pairs():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"Fejl ved hentning af data: {e}")
        return []

    pairs = []
    for pair in data.get("pairs", []):
        pairs.append({
            "pairAddress": pair.get("pairAddress"),
            "baseToken": (pair.get("baseToken") or {}).get("symbol"),
            "quoteToken": (pair.get("quoteToken") or {}).get("symbol"),
            "priceUsd": pair.get("priceUsd"),
            "liquidityUsd": (pair.get("liquidity") or {}).get("usd"),
            "volume24h": (pair.get("volume") or {}).get("h24"),
            "txCount24h": (pair.get("txCount") or {}).get("h24")
        })
    return pairs

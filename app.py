import streamlit as st
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... import pandas as pd
... from utils import get_pairs
... 
... st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
... st.title("🚀 Early Token Dashboard")
... 
... @st.cache_data(ttl=300)
... def fetch_pairs():
...     return get_pairs()
... 
... if "pairs" not in st.session_state:
...     st.session_state.pairs = fetch_pairs()
... 
... if st.button("🔄 Opdater data"):
...     st.session_state.pairs = fetch_pairs()
...     st.success("Data opdateret")
... 
... pairs = st.session_state.pairs
... 
... if not pairs:
...     st.warning("Ingen data hentet endnu.")
... else:
...     df = pd.DataFrame(pairs)
...     df = df.rename(columns={
...         "pairAddress": "Pair",
...         "baseToken": "Base",
...         "quoteToken": "Quote",
...         "priceUsd": "Price (USD)",
...         "liquidityUsd": "Liquidity (USD)",
...         "volume24h": "Volume 24h",
...         "txCount24h": "Tx Count 24h"
...     })
...     st.dataframe(df, use_container_width=True)
...     st.metric("Antal par", len(df))

results/live_expand — LIVE_EXPAND A0/A1/A1k on JoinQuant permission-window expand bars
See: 智库/金融股票/假设-A-涨停可成交性.md
DEFAULT fill = next_open (summary_LIVE_EXPAND_next_open.csv).
next_close is ROBUSTNESS only — do not mix into one NAV number.
Main input = daily_expand_window.parquet (full bars). seal_event_subset is event slice only.
Seal-aware dummy makes A1 blocked_* reflect close-seal events; not an alpha signal.
NOT for investment decisions. No live trading. No stock picks.
Does not overwrite results/live_sample/ or results/fake/.

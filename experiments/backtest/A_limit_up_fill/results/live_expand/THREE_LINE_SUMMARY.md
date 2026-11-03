# LIVE_EXPAND three-line summary (NOT advice)

1. Data: `daily_expand_window.parquet` n_codes=25 window=2025-07-28..2026-07-31 (inside 2025-07-26..2026-08-02); rows=6150; limit_event close_seal_up=10 close_seal_down=4; seal_signal_days=17.
2. next_open LIVE_EXPAND_IS: A0_ret=0.681725 A1_ret=-0.065082 A1k_ret=0.681725 gap_A1-A0=-0.746807; A1_blocked_buys=5 (one_word=0, close_seal=5); A1_blocked_sells=2 (close_seal=2). holdout A0_ret=0.361058 A1_ret=-0.060279 A1_blocked_buys=4 A1_blocked_sells=1.
3. Caveat: seal-aware dummy forces targets into known close-seal sessions so blocked reflects limit_event; NOT a product fillability conclusion; NOT stock advice; no live trading.

as_of=2026-11-03T15:24:43+08:00

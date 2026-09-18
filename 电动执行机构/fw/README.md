# EA10 固件

状态机在 `ea10_fsm.c`，与 `../07_固件最小集.md`、`../sim/fsm.py` 一致。

接到 STM32G474 时：5 ms 调 `ea10_fsm_tick`，把 `k_open/k_close` 送到接触器驱动，把四路继电器接到 `opened/closed/run/fault_relay`。HAL、SPI、LCD 在工程里另建，不要改状态机规则。

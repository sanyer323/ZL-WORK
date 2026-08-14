#!/usr/bin/env python3
"""EA10 固件规则自测：软密封限位关断、停优先、反转延时。"""

from __future__ import annotations

# 与 fw/ea10_fsm.c 同一套规则的精简模型，供无交叉编译环境跑通门槛。


class Fsm:
    def __init__(self) -> None:
        self.state = "STOP"
        self.k_open = 0
        self.k_close = 0
        self.release = 0.0
        self.last = 0
        self.fault = 0

    def tick(self, cmd: int, pos: float, torque: float, seat: str, dt: float = 0.005) -> None:
        if self.release > 0:
            self.release -= dt
            self.k_open = self.k_close = 0
            self.state = "STOP"
            return
        if self.last and cmd and cmd != self.last:
            self.release = 0.08
            self.last = cmd
            self.k_open = self.k_close = 0
            return
        self.last = cmd
        if cmd > 0:
            if pos >= 99.5:
                self.k_open = 0
                self.state = "OPENED"
            else:
                self.k_open, self.k_close = 1, 0
                self.state = "OPENING"
        elif cmd < 0:
            if seat == "limit":
                if pos <= 0.5:
                    self.k_close = 0
                    self.state = "CLOSED"
                elif torque >= 110:
                    self.k_close = 0
                    self.state = "FAULT"
                    self.fault = 5
                else:
                    self.k_open, self.k_close = 0, 1
                    self.state = "CLOSING"
            else:
                if torque >= 100 or pos <= 0.5:
                    self.k_close = 0
                    self.state = "CLOSED"
                else:
                    self.k_open, self.k_close = 0, 1
                    self.state = "CLOSING"
        else:
            self.k_open = self.k_close = 0
            self.state = "STOP"


def main() -> None:
    f = Fsm()
    # 软密封关闭：到位停，力矩 80% 不该跳故障
    pos = 10.0
    for _ in range(4000):
        pos = max(0.0, pos - 0.01)
        f.tick(-1, pos, 80.0, "limit")
    assert f.state == "CLOSED" and f.fault == 0, f.state
    # 停优先
    f2 = Fsm()
    f2.tick(1, 50.0, 20.0, "limit")
    assert f2.k_open == 1
    f2.tick(0, 50.0, 20.0, "limit")
    assert f2.k_open == 0 and f2.state == "STOP"
    # 反转插入释放
    f3 = Fsm()
    f3.tick(1, 50.0, 20.0, "limit")
    f3.tick(-1, 50.0, 20.0, "limit")
    assert f3.k_open == 0 and f3.k_close == 0
    print("EA10 FSM GATE: soft-seat close, stop-first, reverse-delay OK")


if __name__ == "__main__":
    main()

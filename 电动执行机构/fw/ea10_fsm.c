/* EA10 最小状态机。与 sim/fsm.py 规则一致。 */
#include "ea10_fsm.h"

static float s_release;
static float s_jam;
static float s_hammer;
static int s_last_cmd;
static int s_need_reset;

void ea10_fsm_init(ea10_out_t *o) {
    s_release = 0.f;
    s_jam = 0.f;
    s_hammer = 0.f;
    s_last_cmd = 0;
    s_need_reset = 0;
    o->state = EA10_STOP;
    o->k_open = o->k_close = 0;
    o->fault_code = EA10_OK;
    o->opened = o->closed = o->run = o->fault_relay = 0;
}

void ea10_fsm_reset(void) { s_need_reset = 0; }

static void coils(ea10_out_t *o, int open, int close) {
    if (open && close) {
        open = close = 0;
    }
    o->k_open = open;
    o->k_close = close;
}

void ea10_fsm_tick(const ea10_in_t *in, ea10_out_t *o, float dt_s) {
    int cmd = in->cmd_open;
    if (in->mode == EA10_OFF) {
        cmd = 0;
    }

    if (!in->handwheel_ok || !in->therm_ok || !in->phase_ok || !in->pos_ok) {
        coils(o, 0, 0);
        o->state = EA10_FAULT;
        o->fault_code = !in->phase_ok ? EA10_FAULT_PHASE :
                        !in->therm_ok ? EA10_FAULT_THERM :
                        !in->pos_ok ? EA10_FAULT_POS : EA10_FAULT_JAM;
        o->run = 0;
        o->fault_relay = 1;
        s_need_reset = 1;
        o->opened = in->pos_pct >= 99.5f;
        o->closed = in->pos_pct <= 0.5f;
        return;
    }

    if (s_need_reset) {
        coils(o, 0, 0);
        o->run = 0;
        o->fault_relay = 1;
        if (cmd == 0 && in->mode != EA10_REMOTE) {
            /* wait explicit stop; remote stop also clears via cmd=0 in OFF */
        }
        if (cmd == 0) {
            s_need_reset = 0;
            o->state = EA10_STOP;
            o->fault_code = EA10_OK;
            o->fault_relay = 0;
        }
        o->opened = in->pos_pct >= 99.5f;
        o->closed = in->pos_pct <= 0.5f;
        return;
    }

    if (s_last_cmd != 0 && cmd != 0 && cmd != s_last_cmd) {
        s_release = 0.08f;
    }
    s_last_cmd = cmd;
    if (s_release > 0.f) {
        s_release -= dt_s;
        coils(o, 0, 0);
        o->state = EA10_STOP;
        o->run = 0;
        o->opened = in->pos_pct >= 99.5f;
        o->closed = in->pos_pct <= 0.5f;
        o->fault_relay = 0;
        return;
    }

    float tlim = in->t_set_pct > 1.f ? in->t_set_pct : 100.f;
    int near_closed = in->pos_pct < 5.f;
    int bypass = (cmd > 0 && near_closed);

    if (cmd > 0) {
        if (in->pos_pct >= 99.5f) {
            coils(o, 0, 0);
            o->state = EA10_OPENED;
        } else {
            if (s_hammer < 0.014f) {
                s_hammer += dt_s;
            }
            if (!bypass && in->torque_ok && in->torque_pct > tlim * 1.05f && s_hammer >= 0.014f) {
                coils(o, 0, 0);
                o->state = EA10_FAULT;
                o->fault_code = EA10_FAULT_TORQUE;
                s_need_reset = 1;
            } else if (bypass && in->torque_ok && in->torque_pct > 150.f) {
                s_jam += dt_s;
                if (s_jam > 0.4f) {
                    coils(o, 0, 0);
                    o->state = EA10_FAULT;
                    o->fault_code = EA10_FAULT_JAM;
                    s_need_reset = 1;
                } else {
                    coils(o, 1, 0);
                    o->state = EA10_OPENING;
                }
            } else {
                s_jam = 0.f;
                coils(o, 1, 0);
                o->state = EA10_OPENING;
            }
        }
    } else if (cmd < 0) {
        s_hammer = 0.f;
        int limit_hit = in->pos_pct <= 0.5f;
        int t_hit = in->torque_ok && in->torque_pct >= tlim;
        if (in->close_seat == EA10_SEAT_LIMIT) {
            if (limit_hit) {
                coils(o, 0, 0);
                o->state = EA10_CLOSED;
            } else if (t_hit && in->torque_pct >= 110.f) {
                coils(o, 0, 0);
                o->state = EA10_FAULT;
                o->fault_code = EA10_FAULT_TORQUE;
                s_need_reset = 1;
            } else {
                coils(o, 0, 1);
                o->state = EA10_CLOSING;
            }
        } else {
            if (t_hit) {
                coils(o, 0, 0);
                o->state = EA10_CLOSED;
            } else if (limit_hit) {
                coils(o, 0, 0);
                o->state = EA10_CLOSED;
            } else {
                coils(o, 0, 1);
                o->state = EA10_CLOSING;
            }
        }
    } else {
        s_hammer = 0.f;
        s_jam = 0.f;
        coils(o, 0, 0);
        if (in->pos_pct >= 99.5f) {
            o->state = EA10_OPENED;
        } else if (in->pos_pct <= 0.5f) {
            o->state = EA10_CLOSED;
        } else {
            o->state = EA10_STOP;
        }
    }

    o->run = o->k_open || o->k_close;
    o->opened = in->pos_pct >= 99.5f;
    o->closed = (o->state == EA10_CLOSED) || in->pos_pct <= 0.5f;
    o->fault_relay = (o->state == EA10_FAULT);
    if (o->state != EA10_FAULT) {
        o->fault_code = in->torque_ok ? EA10_OK : EA10_WARN_TORQUE;
    }
}

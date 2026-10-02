#ifndef EA10_FSM_H
#define EA10_FSM_H

#include <stdint.h>

typedef enum {
    EA10_STOP = 0,
    EA10_OPENING,
    EA10_CLOSING,
    EA10_OPENED,
    EA10_CLOSED,
    EA10_FAULT
} ea10_state_t;

typedef enum { EA10_OFF = 0, EA10_LOCAL, EA10_REMOTE } ea10_mode_t;
typedef enum { EA10_SEAT_LIMIT = 0, EA10_SEAT_TORQUE } ea10_close_seat_t;

enum {
    EA10_OK = 0,
    EA10_FAULT_PHASE = 1,
    EA10_FAULT_THERM = 2,
    EA10_FAULT_POS = 3,
    EA10_FAULT_JAM = 4,
    EA10_FAULT_TORQUE = 5,
    EA10_WARN_TORQUE = 6
};

typedef struct {
    ea10_mode_t mode;
    int cmd_open;   /* 1=open, -1=close, 0=stop */
    int handwheel_ok; /* 1=motor allowed */
    int therm_ok;
    int phase_ok;
    int pos_ok;
    int torque_ok;
    float pos_pct;     /* 0 closed .. 100 open */
    float torque_pct;  /* % of rated */
    ea10_close_seat_t close_seat;
    float t_set_pct;   /* torque trip, default 100 */
} ea10_in_t;

typedef struct {
    ea10_state_t state;
    int k_open;
    int k_close;
    int fault_code;
    int opened;
    int closed;
    int run;
    int fault_relay;
} ea10_out_t;

void ea10_fsm_init(ea10_out_t *o);
void ea10_fsm_tick(const ea10_in_t *in, ea10_out_t *o, float dt_s);
void ea10_fsm_reset(void);

#endif

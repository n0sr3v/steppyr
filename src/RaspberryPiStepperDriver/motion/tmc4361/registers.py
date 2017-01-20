"""
registers for TMC4361
"""

TMC4361_GENERAL_CONFIG_REGISTER = 0x0
TMC4361_REFERENCE_CONFIG_REGISTER = 0x01
TMC4361_START_CONFIG_REGISTER = 0x2
TMC4361_INPUT_FILTER_REGISTER = 0x3
TMC4361_SPIOUT_CONF_REGISTER = 0x04
TMC4361_ENCODER_INPUT_CONFIG_REGISTER = 0x07
TMC4361_STEP_CONF_REGISTER = 0x0A
TMC4361_EVENT_CLEAR_CONF_REGISTER = 0x0c
TMC4361_INTERRUPT_CONFIG_REGISTER = 0x0d
TMC4361_EVENTS_REGISTER = 0x0e
TMC4361_STATUS_REGISTER = 0x0f
TMC4361_START_OUT_ADD_REGISTER = 0x11
TMC4361_GEAR_RATIO_REGISTER = 0x12
TMC4361_START_DELAY_REGISTER = 0x13
TMC4361_RAMP_MODE_REGISTER = 0x20
TMC4361_X_ACTUAL_REGISTER = 0x21
TMC4361_V_ACTUAL_REGISTER = 0x22
TMC4361_A_ACTUAL_REGISTER = 0x23
TMC4361_V_MAX_REGISTER = 0x24
TMC4361_V_START_REGISTER = 0x25
TMC4361_V_STOP_REGISTER = 0x26
TMC4361_A_MAX_REGISTER = 0x28
TMC4361_D_MAX_REGISTER = 0x29
TMC4361_BOW_1_REGISTER = 0x2d
TMC4361_BOW_2_REGISTER = 0x2e
TMC4361_BOW_3_REGISTER = 0x2f
TMC4361_BOW_4_REGISTER = 0x30
TMC4361_CLK_FREQ_REGISTER = 0x31
TMC4361_POSITION_COMPARE_REGISTER = 0x32
TMC4361_VIRTUAL_STOP_LEFT_REGISTER = 0x33
TMC4361_VIRTUAL_STOP_RIGHT_REGISTER = 0x34
TMC4361_X_LATCH_REGISTER = 0x36
TMC4361_X_TARGET_REGISTER = 0x37
TMC4361_X_TARGET_PIPE_0_REGSISTER = 0x38
TMC4361_SH_V_MAX_REGISTER = 0x40
TMC4361_SH_A_MAX_REGISTER = 0x41
TMC4361_SH_D_MAX_REGISTER = 0x42
TMC4361_SH_VBREAK_REGISTER = 0x45
TMC4361_SH_V_START_REGISTER = 0x46
TMC4361_SH_V_STOP_REGISTER = 0x47
TMC4361_SH_BOW_1_REGISTER = 0x48
TMC4361_SH_BOW_2_REGISTER = 0x49
TMC4361_SH_BOW_3_REGISTER = 0x4A
TMC4361_SH_BOW_4_REGISTER = 0x4B
TMC4361_SH_RAMP_MODE_REGISTER = 0x4C
TMC4361_ENCODER_POSITION_REGISTER = 0x50
TMC4361_ENCODER_INPUT_RESOLUTION_REGISTER = 0x54
TMC4361_COVER_LOW_REGISTER = 0x6c
TMC4361_COVER_HIGH_REGISTER = 0x6d

# how to mask REFERENCE_CONFIG_REGISTER if you want to configure just one end
TMC4361_LEFT_ENDSTOP_REGISTER_PATTERN = (_BV(0) | _BV(2) | _BV(6) | _BV(10) | _BV(11) | _BV(14))
TMC4361_RIGHT_ENDSTOP_REGISTER_PATTERN = (_BV(1) | _BV(3) | _BV(7) | _BV(12) | _BV(13) | _BV(15))

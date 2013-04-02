#maps.py

def get_key_dictionary(obj, keyboard="UK"):
  #define keys displayed on the gui keyboard (by key code)    
  if keyboard == 0:
    return                                    \
      (8,   obj.m_backspace),                 \
      (9,   obj.m_tab),                       \
      (12,  obj.m_num5),                      \
      (13,  obj.m_enter, obj.m_num_enter),    \
      (19,  obj.m_break),                     \
      (20,  obj.m_caps_lock),                 \
      (27,  obj.m_escape),                    \
      (32,  obj.m_space),                     \
      (33,  obj.m_num9, obj.m_page_up),       \
      (34,  obj.m_num3, obj.m_page_down),     \
      (35,  obj.m_num1, obj.m_end),           \
      (36,  obj.m_num7, obj.m_home),          \
      (37,  obj.m_num4, obj.m_left),          \
      (38,  obj.m_num8, obj.m_up),            \
      (39,  obj.m_num6, obj.m_right),         \
      (40,  obj.m_num2, obj.m_down),          \
      (44,  obj.m_print),                     \
      (45,  obj.m_num0, obj.m_insert),        \
      (46,  obj.m_num_period, obj.m_delete),  \
      (48,  obj.m_0),                         \
      (49,  obj.m_1),                         \
      (50,  obj.m_2),                         \
      (51,  obj.m_3),                         \
      (52,  obj.m_4),                         \
      (53,  obj.m_5),                         \
      (54,  obj.m_6),                         \
      (55,  obj.m_7),                         \
      (56,  obj.m_8),                         \
      (57,  obj.m_9),                         \
      (65,  obj.m_a),                         \
      (66,  obj.m_b),                         \
      (67,  obj.m_c),                         \
      (68,  obj.m_d),                         \
      (69,  obj.m_e),                         \
      (70,  obj.m_f),                         \
      (71,  obj.m_g),                         \
      (72,  obj.m_h),                         \
      (73,  obj.m_i),                         \
      (74,  obj.m_j),                         \
      (75,  obj.m_k),                         \
      (76,  obj.m_l),                         \
      (77,  obj.m_m),                         \
      (78,  obj.m_n),                         \
      (79,  obj.m_o),                         \
      (80,  obj.m_p),                         \
      (81,  obj.m_q),                         \
      (82,  obj.m_r),                         \
      (83,  obj.m_s),                         \
      (84,  obj.m_t),                         \
      (85,  obj.m_u),                         \
      (86,  obj.m_v),                         \
      (87,  obj.m_w),                         \
      (88,  obj.m_x),                         \
      (89,  obj.m_y),                         \
      (90,  obj.m_z),                         \
      (91,  obj.m_left_windows),              \
      (92,  obj.m_right_windows),             \
      (93,  obj.m_menu),                      \
      (96,  obj.m_num0),                      \
      (97,  obj.m_num1),                      \
      (98,  obj.m_num2),                      \
      (99,  obj.m_num3),                      \
      (100, obj.m_num4),                      \
      (101, obj.m_num5),                      \
      (102, obj.m_num6),                      \
      (103, obj.m_num7),                      \
      (104, obj.m_num8),                      \
      (105, obj.m_num9),                      \
      (106, obj.m_num_asterix),               \
      (107, obj.m_num_plus),                  \
      (109, obj.m_num_minus),                 \
      (110, obj.m_num_period),                \
      (111, obj.m_num_slash),                 \
      (112, obj.m_f1),                        \
      (113, obj.m_f2),                        \
      (114, obj.m_f3),                        \
      (115, obj.m_f4),                        \
      (116, obj.m_f5),                        \
      (117, obj.m_f6),                        \
      (118, obj.m_f7),                        \
      (119, obj.m_f8),                        \
      (120, obj.m_f9),                        \
      (121, obj.m_f10),                       \
      (122, obj.m_f11),                       \
      (123, obj.m_f12),                       \
      (144, obj.m_numlock),                   \
      (145, obj.m_scroll),                    \
      (160, obj.m_left_shift),                \
      (161, obj.m_right_shift),               \
      (162, obj.m_left_ctrl),                 \
      (163, obj.m_right_ctrl),                \
      (164, obj.m_left_alt),                  \
      (165, obj.m_right_alt),                 \
      (186, obj.m_colon),                     \
      (187, obj.m_plus),                      \
      (188, obj.m_comma),                     \
      (189, obj.m_minus),                     \
      (190, obj.m_period),                    \
      (191, obj.m_question),                  \
      (192, obj.m_at),                        \
      (219, obj.m_left_brace),                \
      (220, obj.m_backslash),                 \
      (221, obj.m_right_brace),               \
      (222, obj.m_tilde),                     \
      (223, obj.m_squiggle),                  \
      (384, obj.m_num0),                      \
      (385, obj.m_num_period)  
  else:
    return                                    \
      (8,   obj.mus_backspace),                 \
      (9,   obj.mus_tab),                       \
      (12,  obj.mus_num5),                      \
      (13,  obj.mus_enter, obj.mus_num_enter),    \
      (19,  obj.mus_break),                     \
      (20,  obj.mus_caps_lock),                 \
      (27,  obj.mus_escape),                    \
      (32,  obj.mus_space),                     \
      (33,  obj.mus_num9, obj.mus_page_up),       \
      (34,  obj.mus_num3, obj.mus_page_down),     \
      (35,  obj.mus_num1, obj.mus_end),           \
      (36,  obj.mus_num7, obj.mus_home),          \
      (37,  obj.mus_num4, obj.mus_left),          \
      (38,  obj.mus_num8, obj.mus_up),            \
      (39,  obj.mus_num6, obj.mus_right),         \
      (40,  obj.mus_num2, obj.mus_down),          \
      (44,  obj.mus_print),                     \
      (45,  obj.mus_num0, obj.mus_insert),        \
      (46,  obj.mus_num_period, obj.mus_delete),  \
      (48,  obj.mus_0),                         \
      (49,  obj.mus_1),                         \
      (50,  obj.mus_2),                         \
      (51,  obj.mus_3),                         \
      (52,  obj.mus_4),                         \
      (53,  obj.mus_5),                         \
      (54,  obj.mus_6),                         \
      (55,  obj.mus_7),                         \
      (56,  obj.mus_8),                         \
      (57,  obj.mus_9),                         \
      (65,  obj.mus_a),                         \
      (66,  obj.mus_b),                         \
      (67,  obj.mus_c),                         \
      (68,  obj.mus_d),                         \
      (69,  obj.mus_e),                         \
      (70,  obj.mus_f),                         \
      (71,  obj.mus_g),                         \
      (72,  obj.mus_h),                         \
      (73,  obj.mus_i),                         \
      (74,  obj.mus_j),                         \
      (75,  obj.mus_k),                         \
      (76,  obj.mus_l),                         \
      (77,  obj.mus_m),                         \
      (78,  obj.mus_n),                         \
      (79,  obj.mus_o),                         \
      (80,  obj.mus_p),                         \
      (81,  obj.mus_q),                         \
      (82,  obj.mus_r),                         \
      (83,  obj.mus_s),                         \
      (84,  obj.mus_t),                         \
      (85,  obj.mus_u),                         \
      (86,  obj.mus_v),                         \
      (87,  obj.mus_w),                         \
      (88,  obj.mus_x),                         \
      (89,  obj.mus_y),                         \
      (90,  obj.mus_z),                         \
      (91,  obj.mus_left_windows),              \
      (92,  obj.mus_right_windows),             \
      (93,  obj.mus_menu),                      \
      (96,  obj.mus_num0),                      \
      (97,  obj.mus_num1),                      \
      (98,  obj.mus_num2),                      \
      (99,  obj.mus_num3),                      \
      (100, obj.mus_num4),                      \
      (101, obj.mus_num5),                      \
      (102, obj.mus_num6),                      \
      (103, obj.mus_num7),                      \
      (104, obj.mus_num8),                      \
      (105, obj.mus_num9),                      \
      (106, obj.mus_num_asterix),               \
      (107, obj.mus_num_plus),                  \
      (109, obj.mus_num_minus),                 \
      (110, obj.mus_num_period),                \
      (111, obj.mus_num_slash),                 \
      (112, obj.mus_f1),                        \
      (113, obj.mus_f2),                        \
      (114, obj.mus_f3),                        \
      (115, obj.mus_f4),                        \
      (116, obj.mus_f5),                        \
      (117, obj.mus_f6),                        \
      (118, obj.mus_f7),                        \
      (119, obj.mus_f8),                        \
      (120, obj.mus_f9),                        \
      (121, obj.mus_f10),                       \
      (122, obj.mus_f11),                       \
      (123, obj.mus_f12),                       \
      (144, obj.mus_numlock),                   \
      (145, obj.mus_scroll),                    \
      (160, obj.mus_left_shift),                \
      (161, obj.mus_right_shift),               \
      (162, obj.mus_left_ctrl),                 \
      (163, obj.mus_right_ctrl),                \
      (164, obj.mus_left_alt),                  \
      (165, obj.mus_right_alt),                 \
      (186, obj.mus_colon),                     \
      (187, obj.mus_plus),                      \
      (188, obj.mus_comma),                     \
      (189, obj.mus_minus),                     \
      (190, obj.mus_period),                    \
      (191, obj.mus_question),                  \
      (192, obj.mus_squiggle),                  \
      (219, obj.mus_left_brace),                \
      (220, obj.mus_backslash),                 \
      (221, obj.mus_right_brace),               \
      (222, obj.mus_at),                        \
      (384, obj.mus_num0),                      \
      (385, obj.mus_num_period)  

  
def get_func_map():
  return                                                   \
    ('MAME', 49,  'P1 Start'),                             \
    ('MAME', 53,  'P1 Coin'),                              \
    ('MAME', 38,  'P1 Up'),                                \
    ('MAME', 40,  'P1 Down'),                              \
    ('MAME', 37,  'P1 Left'),                              \
    ('MAME', 39,  'P1 Right'),                             \
    ('MAME', 162, 'P1 Button 1'),                          \
    ('MAME', 164, 'P1 Button 2'),                          \
    ('MAME', 32,  'P1 Button 3'),                          \
    ('MAME', 160, 'P1 Button 4'),                          \
    ('MAME', 90,  'P1 Button 5'),                          \
    ('MAME', 88,  'P1 Button 6'),                          \
    ('MAME', 67,  'P1 Button 7'),                          \
    ('MAME', 86,  'P1 Button 8'),                          \
    ('MAME', 50,  'P2 Start'),                             \
    ('MAME', 54,  'P2 Coin'),                              \
    ('MAME', 82,  'P2 Up'),                                \
    ('MAME', 70,  'P2 Down'),                              \
    ('MAME', 68,  'P2 Left'),                              \
    ('MAME', 71,  'P2 Right'),                             \
    ('MAME', 65,  'P2 Button 1'),                          \
    ('MAME', 83,  'P2 Button 2'),                          \
    ('MAME', 81,  'P2 Button 3'),                          \
    ('MAME', 87,  'P2 Button 4'),                          \
    ('MAME', 73,  'P2 Button 5 | P3 Up'),                  \
    ('MAME', 75,  'P2 Button 6 | P3 Down'),                \
    ('MAME', 74,  'P2 Button 7 | P3 Right'),               \
    ('MAME', 76,  'P2 Button 8 | P3 Right'),               \
    ('MAME', 51,  'P3 Start'),                             \
    ('MAME', 55,  'P3 Coin'),                              \
    ('MAME', 163, 'P3 Button 1'),                          \
    ('MAME', 161, 'P3 Button 2'),                          \
    ('MAME', 13,  'Select | P3 Button 3'),                 \
    ('MAME', 220, 'P3 Button 4'),                          \
    ('MAME', 190, 'P3 Button 5'),                          \
    ('MAME', 44,  'P3 Button 6'),                          \
    ('MAME', 52,  'P4 Start'),                             \
    ('MAME', 56,  'P4 Coin'),                              \
    ('MAME', 89,  'P4 Up'),                                \
    ('MAME', 78,  'P4 Down'),                              \
    ('MAME', 86,  'P4 Left'),                              \
    ('MAME', 85,  'P4 Right'),                             \
    ('MAME', 96,  'P4 Button 1'),                          \
    ('MAME', 109, 'P4 Button 2'),                          \
    ('MAME', 219, 'P4 Button 3'),                          \
    ('MAME', 107, 'P4 Button 4'),                          \
    ('MAME', 109, 'P4 Button 5'),                          \
    ('MAME', 106, 'P4 Button 6'),                          \
    ('MAME', 27,  'Cancel / Exit Game'),                   \
    ('MAME', 9,   'Access in Game Menu'),                  \
    ('MAME', 80,  'Pause the Game'),                       \
    ('MAME', 118, 'Load/Save Game'),                       \
    ('MAME', 114, 'Game/Reset'),                           \
    ('MAME', 84,  'Tilt'),                                 \
    ('MAME', 189, 'Volume Down'),                          \
    ('MAME', 187, 'Volume Up'),                            \
    ('MAME', 123, 'Save Screenshot to Snaps Directory'),   \
    ('MAME', 112, 'Enable Crosshairs'),                    \
    ('MAME', 117, 'Enable/Disable Cheats'),                \
    ('MAME', 119, 'Decrease Frame Rate'),                  \
    ('MAME', 120, 'Increase Frame Rate'),                  \
    ('MAME', 122, 'Display Frames Information'),           \
    ('MAME', 115, 'Show Game Graphics'),                   \
    ('MAME', 121, 'Game Speed Throttle'),                  \
    ('MAME', 45,  'Run game at full throttle'),            \
    ('MAME', 8,   'Bill'),                                 \
    ('MAME', 113, 'Test/Service Switch'),                  \
    ('MAME', 57,  'Service 1'),                            \
    ('MAME', 48,  'Service 2'),                            \
    ('MAME', 189, 'Service 3'),                            \
    ('MAME', 187, 'Service 4'),                            \
    ('PIN',  49,  'Start (1)'),                            \
    ('PIN',  53,  'Coin (5)'),                             \
    ('PIN',  38,  'Up (UP)'),                              \
    ('PIN',  40,  'Down (DOWN)'),                          \
    ('PIN',  37,  'Left (LEFT)'),                          \
    ('PIN',  39,  'Right (RIGHT)'),                        \
    ('PIN',  162, 'Left Magnasave (L/CTRL)'),              \
    ('PIN',  163, 'Right Magnasave (R/CTRL)'),             \
    ('PIN',  32,  'Forward Nudge (SPACE)'),                \
    ('PIN',  160, 'Left Flipper (L/SHIFT)'),               \
    ('PIN',  90,  'Left Nudge (Z)'),                       \
    ('PIN',  161, 'Right Flipper (R/SHIFT)'),              \
    ('PIN',  191, 'Right Nudge (/)'),                      \
    ('PIN',  81,  'Quit Visual Pinball (Q)'),              \
    ('PIN',  13,  'Plunger (ENTER)'),                      \
    ('PIN',  19,  'Pause Game (PAUSE/BREAK)'),             \
    ('PIN',  65,  'Left Upper Flipper (A)'),               \
    ('PIN',  192, "Right Upper Flipper (')"),              \
    ('PIN',  9,   'View Backglass (Tab)'),                 \
    ('PIN',  27,  'Exit (ESC)'),                           \
    ('PIN',  114, 'VP: Reset Emulation (F3)'),             \
    ('PIN',  84,  'Tilt (T)'),                             \
    ('PIN',  50,  'VP: Buy-In / Extra Ball (2)'),          \
    ('PIN',  54,  'FP: Insert coin 2 (6)'),                \
    ('PIN',  189, 'VP: Volume Down (-)'),                  \
    ('PIN',  187, 'VP: Volume Up (BACKSPACE)'),            \
    ('PIN',  112, 'VP: Game Options (F1)'),                \
    ('PIN',  117, 'VP: Dip Switch Menu (F6)'),             \
    ('PIN',  120, 'FP: Frame Rate and Stats (F9)'),        \
    ('PIN',  122, 'VP: Frame Count (F11)'),                \
    ('PIN',  121, 'FP: Wireframe Mode On/Off (F10)'),      \
    ('PIN',  8 ,  'Bill (BACKSPACE)'),                     \
    ('PIN',  113, 'VP: Keyboard Settings (F2)'),           \
    ('PIN',  35,  'Williams Coin Door: Open/Close (END)'), \
    ('PIN',  48,  'Williams Coin Door: Enter (0)'),        \
    ('PIN',  55,  'Williams Coin Door: Escape (7)'),       \
    ('PIN',  56,  'Williams Coin Door: Down (8)'),         \
    ('PIN',  36,  'Williams Coin Door: Slam Tilt (HOME)'), \
    ('PIN',  57,  'Williams Coin Door: Up (9)'),           \
    ('PIN_US', 222, "Right Upper Flipper (')") #Fix US keyboard
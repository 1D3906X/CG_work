# src/Work0/config.py

import random

# --- 物理系统参数 ---
NUM_PARTICLES = 10000
GRAVITY_STRENGTH = 0.001
DRAG_COEF = 0.98
BOUNCE_COEF = -0.8

# --- 渲染系统参数 ---
WINDOW_RES = (800, 600)
PARTICLE_RADIUS = 1.5

# 五彩粒子
PARTICLE_COLOR = random.randint(0x000000,0xFFFFFF)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Registers:

    Z_FLAG = 0x80
    N_FLAG = 0x40
    H_FLAG = 0x20
    C_FLAG = 0x10

    def __init__(self):
        self.a = 0x00
        self.b = 0x00
        self.c = 0x00
        self.d = 0x00
        self.e = 0x00
        self.f = 0x00
        self.h = 0x00
        self.l = 0x00
        self.pc = 0x0000
        self.sp = 0x0000

    def set_af(self, word):
        self.a = ( word >> 8 ) & 0xff
        self.f = word & 0xff

    def set_bc(self, word):
        self.b = ( word >> 8 ) & 0xff
        self.c = word & 0xff

    def set_de(self, word):
        self.d = ( word >> 8 ) & 0xff
        self.e = word & 0xff

    def set_hl(self, word):
        self.h = ( word >> 8 ) & 0xff
        self.l = word & 0xff

    def get_af(self):
        return (self.a << 8) + self.f

    def get_bc(self):
        return (self.b << 8) + self.c

    def get_de(self):
        return (self.d << 8) + self.e

    def get_hl(self):
        return (self.h << 8) + self.l

    def set_z_flag(self):
        self.f |= Registers.Z_FLAG

    def reset_z_flag(self):
        self.f &= Registers.Z_FLAG ^ 0xff

    def set_n_flag(self):
        self.f |= Registers.N_FLAG

    def reset_n_flag(self):
        self.f &= Registers.N_FLAG ^ 0xff

    def set_c_flag(self):
        self.f |= Registers.C_FLAG

    def reset_c_flag(self):
        self.f &= Registers.C_FLAG ^ 0xff

    def set_h_flag(self):
        self.f |= Registers.H_FLAG

    def reset_h_flag(self):
        self.f &= Registers.H_FLAG ^ 0xff
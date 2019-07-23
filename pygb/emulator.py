#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygb.cpu import CPU
from pygb.mmu import MMU
from pygb.ppu import PPU
from pygb.screen import Screen
from pygb.sound import Sound

class Emulator:

    def __init__(self, file):
        self.mmu = MMU() 
        self.cpu = CPU(self.mmu)
        self.ppu = PPU(self.mmu, self.cpu.interruptManager)
        self.sound = Sound(self.mmu, self.cpu.interruptManager)
        self.screen = Screen()
        self.screen.start()

    def run(self):
        while True:
            self.cpu.step()
            self.ppu.step(self.cpu.ticks)
            if self.ppu.vblank:
                self.screen.render(self.ppu.framebuffer)
            self.sound.step()


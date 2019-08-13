#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygb.interrupt_manager import Interrupt, InterruptManager
from pygb.io_registers import IO_Registers
from pygb.mmu import MMU

class Sound:

    def __init__(self, mmu : MMU, interruptManager : InterruptManager):
        self.mmu = mmu
        self.interruptManager = interruptManager
        self.allModes = [
            SoundMode1(),
            SoundMode2(),
            SoundMode3(),
            SoundMode4()
        ]
        self.channels = [0]*4
        self.overridenEnabled = [True]*4
        self.output = SoundOutput()

    def step(self):
        if not self.enabled():
            return

        for i in range(0,4):
            self.channels[i] = self.allModes[i].step()

        selection = self.mmu.read_byte(IO_Registers.NR_51)
        right = 0
        left = 0

        for i in range(0,4):
            if self.overridenEnabled[i]:
                continue
            if (selection & (1 << i + 4)) != 0:
                left += self.channels[i] 
            if (selection & (1 << i)) != 0:
                right += self.channels[i]

        left = int(left / 4)
        right = int(right / 4)

        volumes = self.mmu.read_byte(IO_Registers.NR_50)
        left *= ((volumes >> 4) & 0b111)
        right *= (volumes & 0b111)

        self.output.play(left & 0xff, right & 0xff)
        
    def enabled(self) -> bool:
        sound_on_off = self.mmu.read_byte(IO_Registers.NR_52)
        return sound_on_off & 0x80 == 0x80

    def enableChannel(self, i : int, enabled : bool):
        self.overridenEnabled[i] = enabled
    

class AbstractSoundMode:

    def step(self) -> int:
        return 0

class SoundMode1(AbstractSoundMode):

    def step(self) -> int:
        return 0

class SoundMode2(AbstractSoundMode):

    def step(self) -> int:
        return 0

class SoundMode3(AbstractSoundMode):

    def step(self) -> int:
        return 0

class SoundMode4(AbstractSoundMode):

    def step(self) -> int:
        return 0

class SoundOutput:

    def __init__(self):
        pass

    def play(self, left : int, right : int):
        pass
        
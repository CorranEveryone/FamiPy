##### CHANGES REQUIRED #####
# Comments with PATCH_NEEDED require changes that weren't initially made but were known
# MISSING_PPU_STUFF
# MISSING_APU_STUFF

##### USER CONFIG (temporary solution) #####
romfilepath = "./roms/Super Mario Bros. (World).nes" # Only .nes files are supported

##### DEFINE ALL VARIABLES HERE #####
# Power Up State
ram = bytearray(b'\x00'*2048) # 2kb ram
## CPU Registers
cpu_a = bytearray(b'\x00')
cpu_x = bytearray(b'\x00')
cpu_y = bytearray(b'\x00')
cpu_pc = bytearray(b'\x80\x00')
cpu_returnpc = bytearray(b'\x80\x00')
cpu_s = bytearray(b'\xFD')
cpu_c = bytearray(b'\x00')
cpu_z = bytearray(b'\x00')
cpu_i = bytearray(b'\x01')
cpu_d = bytearray(b'\x00')
cpu_v = bytearray(b'\x00')
cpu_n = bytearray(b'\x00')
cpu_cycles = 0
## APU Regiseters

##### DEFINE FUNCTIONS HERE #####
def cpumap(address:bytearray) -> bytearray: #address:16bit
    addresspage = address[0:1]
    addressbyte = address[1:2]
    if addresspage == bytearray(b'\x00') or addresspage == bytearray(b'\x08') or addresspage == bytearray(b'\x10') or addresspage == bytearray(b'\x18'): # RAM Page 0
        return ram[addressbyte[0]:addressbyte[0]+1]
    elif addresspage == bytearray(b'\x01') or addresspage == bytearray(b'\x09') or addresspage == bytearray(b'\x11') or addresspage == bytearray(b'\x19'): # RAM Page 1
        return ram[addressbyte[0]+(256*1):addressbyte[0]+(256*1)+1]
    elif addresspage == bytearray(b'\x02') or addresspage == bytearray(b'\x0A') or addresspage == bytearray(b'\x12') or addresspage == bytearray(b'\x1A'): # RAM Page 2
        return ram[addressbyte[0]+(256*2):addressbyte[0]+(256*2)+1]
    elif addresspage == bytearray(b'\x03') or addresspage == bytearray(b'\x0B') or addresspage == bytearray(b'\x13') or addresspage == bytearray(b'\x1B'): # RAM Page 3
        return ram[addressbyte[0]+(256*3):addressbyte[0]+(256*3)+1]
    elif addresspage == bytearray(b'\x04') or addresspage == bytearray(b'\x0C') or addresspage == bytearray(b'\x14') or addresspage == bytearray(b'\x1C'): # RAM Page 4
        return ram[addressbyte[0]+(256*4):addressbyte[0]+(256*4)+1]
    elif addresspage == bytearray(b'\x05') or addresspage == bytearray(b'\x0D') or addresspage == bytearray(b'\x15') or addresspage == bytearray(b'\x1D'): # RAM Page 5
        return ram[addressbyte[0]+(256*5):addressbyte[0]+(256*5)+1]
    elif addresspage == bytearray(b'\x06') or addresspage == bytearray(b'\x0E') or addresspage == bytearray(b'\x16') or addresspage == bytearray(b'\x1E'): # RAM Page 6
        return ram[addressbyte[0]+(256*6):addressbyte[0]+(256*6)+1]
    elif addresspage == bytearray(b'\x07') or addresspage == bytearray(b'\x0F') or addresspage == bytearray(b'\x17') or addresspage == bytearray(b'\x1F'): # RAM Page 7
        return ram[addressbyte[0]+(256*7):addressbyte[0]+(256*7)+1]
    # MISSING_PPU_STUFF
    # MISSING_APU_STUFF
    elif addresspage[0] >= 128:
        return prgrom[addressbyte[0]+(addresspage[0]-128)*256:(addressbyte[0]+(addresspage[0]-128)*256)+1]
    else:
        print(f"[ERROR] {address} is not a defined CPU Memory Address")
        return bytearray(b'\x00')

def writecpumap(address:bytearray, value:bytearray) -> bool:
    addresspage = address[0:1]
    addressbyte = address[1:2]
    value = value[0]
    returncode = True
    if addresspage == bytearray(b'\x00') or addresspage == bytearray(b'\x08') or addresspage == bytearray(b'\x10') or addresspage == bytearray(b'\x18'): # RAM Page 0
        ram[addressbyte[0]:addressbyte[0]+1] = value
    elif addresspage == bytearray(b'\x01') or addresspage == bytearray(b'\x09') or addresspage == bytearray(b'\x11') or addresspage == bytearray(b'\x19'): # RAM Page 1
        ram[addressbyte[0]+(256*1):addressbyte[0]+(256*1)+1] = value
    elif addresspage == bytearray(b'\x02') or addresspage == bytearray(b'\x0A') or addresspage == bytearray(b'\x12') or addresspage == bytearray(b'\x1A'): # RAM Page 2
        ram[addressbyte[0]+(256*2):addressbyte[0]+(256*2)+1] = value
    elif addresspage == bytearray(b'\x03') or addresspage == bytearray(b'\x0B') or addresspage == bytearray(b'\x13') or addresspage == bytearray(b'\x1B'): # RAM Page 3
        ram[addressbyte[0]+(256*3):addressbyte[0]+(256*3)+1] = value
    elif addresspage == bytearray(b'\x04') or addresspage == bytearray(b'\x0C') or addresspage == bytearray(b'\x14') or addresspage == bytearray(b'\x1C'): # RAM Page 4
        ram[addressbyte[0]+(256*4):addressbyte[0]+(256*4)+1] = value
    elif addresspage == bytearray(b'\x05') or addresspage == bytearray(b'\x0D') or addresspage == bytearray(b'\x15') or addresspage == bytearray(b'\x1D'): # RAM Page 5
        ram[addressbyte[0]+(256*5):addressbyte[0]+(256*5)+1] = value
    elif addresspage == bytearray(b'\x06') or addresspage == bytearray(b'\x0E') or addresspage == bytearray(b'\x16') or addresspage == bytearray(b'\x1E'): # RAM Page 6
        ram[addressbyte[0]+(256*6):addressbyte[0]+(256*6)+1] = value
    elif addresspage == bytearray(b'\x07') or addresspage == bytearray(b'\x0F') or addresspage == bytearray(b'\x17') or addresspage == bytearray(b'\x1F'): # RAM Page 7
        ram[addressbyte[0]+(256*7):addressbyte[0]+(256*7)+1] = value
    # MISSING_PPU_STUFF
    # MISSING_APU_STUFF
    else:
        print(f"[ERROR] {address} is not writable CPU Memory Address")
        returncode = False
    return returncode

def addTo16BitInt(givenint:bytearray, inttoadd:int) -> bytearray:
    usableint1 = givenint[1]
    usableint0 = givenint[0]
    usableint1 += inttoadd
    while usableint1 > 255:
        usableint1 -= 256
        usableint0 += 1
    return bytearray([usableint0, usableint1])

def intToBin(givenint:bytearray) -> list:
    usableint = givenint[0]
    returnvalue = [0, 0, 0, 0, 0, 0, 0, 0]
    if usableint >= 128:
        returnvalue[7] = 1
        usableint -= 128
    elif usableint >= 64:
        returnvalue[6] = 1
        usableint -= 64
    elif usableint >= 32:
        returnvalue[5] = 1
        usableint -= 32
    elif usableint >= 16:
        returnvalue[4] = 1
        usableint -= 16
    elif usableint >= 8:
        returnvalue[3] = 1
        usableint -= 8
    elif usableint >= 4:
        returnvalue[2] = 1
        usableint -= 4
    elif usableint >= 2:
        returnvalue[1] = 1
        usableint -= 2
    elif usableint >= 1:
        returnvalue[0] = 1
        usableint -= 1
    return returnvalue

def signedInt(givenint:bytearray) -> int:
    usableint = givenint[0]
    if usableint >= 128:
        usableint -= 128
        usableint *= -1
    return usableint

def cpu(address:bytearray) -> bool:
    global cpu_a, cpu_x, cpu_y, cpu_pc, cpu_returnpc, cpu_s, cpu_c, cpu_z, cpu_i, cpu_d, cpu_v, cpu_n, cpu_cycles
    returncode = True
    opcode = cpumap(address)
    if opcode == bytearray(b'\x10'): #BPL - Branch if Plus
        if cpu_n == bytearray(b'\x00'):
            cpu_returnpc = addTo16BitInt(address, signedInt(addTo16BitInt(address, 1))+2)
        else:
            cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
        if cpu_n == bytearray(b'\x00'):
            cpu_cycles += 1
        if address[0:1] != addTo16BitInt(address, signedInt(addTo16BitInt(address, 1))+2):
            cpu_cycles += 1
    elif opcode == bytearray(b'\x78'): #SEI - Set Interrupt Disable
        cpu_i = bytearray(b'\x01') # PATCH_NEEDED Eventually delay by an instruction
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\x8A'): #TXA - Transfer X to A
        cpu_a = cpu_x
        if cpu_a == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_a)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\x8D'): #STA - Store A (Absolute)
        i = cpumap(addTo16BitInt(address, 2))
        i.extend(cpumap(addTo16BitInt(address, 1)))
        writecpumap(i, cpu_a)
        cpu_returnpc = addTo16BitInt(address, 3)
        cpu_cycles = 4
    elif opcode == bytearray(b'\x98'): #TYA - Transfer Y to A
        cpu_a = cpu_y
        if cpu_a == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_a)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\x9A'): #TXS - Transfer X to Stack Pointer
        cpu_s = cpu_x
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xA0'): #LDY - Load Y (#Immediate)
        cpu_y = cpumap(addTo16BitInt(address, 1))
        if cpu_y == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_y)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xA2'): #LDX - Load X (#Immediate)
        cpu_x = cpumap(addTo16BitInt(address, 1))
        if cpu_x == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_x)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xA8'): #TAY - Transfer A to Y
        cpu_y = cpu_a
        if cpu_y == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_y)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xA9'): #LDA - Load A (#Immediate)
        cpu_a = cpumap(addTo16BitInt(address, 1))
        if cpu_a == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_a)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xAA'): #TAX - Transfer A to X
        cpu_x = cpu_a
        if cpu_x == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_x)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xAD'): #LDA - Load A (Absolute)
        i = cpumap(addTo16BitInt(address, 2))
        i.extend(cpumap(addTo16BitInt(address, 1)))
        cpu_a = cpumap(i)
        if cpu_a == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_a)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 3)
        cpu_cycles = 4
    elif opcode == bytearray(b'\xB0'): #BCS - Branch if Carry Set
        if cpu_c == bytearray(b'\x01'):
            cpu_returnpc = addTo16BitInt(address, signedInt(addTo16BitInt(address, 1))+2)
        else:
            cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
        if cpu_c == bytearray(b'\x01'):
            cpu_cycles += 1
        if address[0:1] != addTo16BitInt(address, signedInt(addTo16BitInt(address, 1))+2):
            cpu_cycles += 1
    elif opcode == bytearray(b'\xBA'): #TSX - Transfer Stack Pointer to X
        cpu_x = cpu_s
        if cpu_x == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_x)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xBD'): #LDA - Load A (Absolute, X)
        i = cpumap(addTo16BitInt(address, 2))
        i.extend(cpumap(addTo16BitInt(address, 1)))
        cpu_a = cpumap(addTo16BitInt(i, cpu_x[0]))
        if cpu_a == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_a)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 3)
        cpu_cycles = 4
        if i[0:1] != addTo16BitInt(i, cpu_x[0])[0:1]: # Account for "oops" cycle
            cpu_cycles += 1
    elif opcode == bytearray(b'\xC9'): #CMP - Compare A (#Immediate)
        if cpu_a[0] >= cpumap(addTo16BitInt(address, 1))[0]:
            cpu_c = bytearray(b'\x01')
        else:
            cpu_c = bytearray(b'\x00')
        if cpu_a == cpumap(addTo16BitInt(address, 1)):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if cpu_a[0] - cpumap(addTo16BitInt(address, 1))[0] < 0:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xCA'): #DEX - Decrement X
        cpu_x[0] -= 1
        while cpu_x[0] < 0:
            cpu_x[0] += 256
        if cpu_x == bytearray(b'\x00'):
            cpu_z = bytearray(b'\x01')
        else:
            cpu_z = bytearray(b'\x00')
        if intToBin(cpu_x)[7] == 1:
            cpu_n = bytearray(b'\x01')
        else:
            cpu_n = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    elif opcode == bytearray(b'\xD0'): #BPL - Branch if Plus
        if cpu_z == bytearray(b'\x00'): #FIXFIX
            cpu_returnpc = addTo16BitInt(address, signedInt(addTo16BitInt(address, 1))+2)
        else:
            cpu_returnpc = addTo16BitInt(address, 2)
        cpu_cycles = 2
        if cpu_z == bytearray(b'\x00'):
            cpu_cycles += 1
        if address[0:1] != addTo16BitInt(address, signedInt(addTo16BitInt(address, 1))+2):
            cpu_cycles += 1
    elif opcode == bytearray(b'\xD8'): #CLD - Clear Decimal
        cpu_d = bytearray(b'\x00')
        cpu_returnpc = addTo16BitInt(address, 1)
        cpu_cycles = 2
    else:
        print(f"Unknown OPCODE: {opcode} at {address}")
        returncode = False
    return returncode

##### ACTUAL CODE BEGINS #####
### OPEN AND VERIFY ROM ###
romfile = open(romfilepath, "rb")
rom = bytearray(romfile.read())
prgrom = rom[16:(16 + 16384*rom[4])] # [FirstByteOfProgramROM:LastByteOfProgramROM*BasedOnSpecifiedFromFile]
charrom = rom[(16 + 16384*rom[4]):(17 + 16384*rom[4])+(8192*rom[5])] # [FirstByteOfCharROMAfterProgramROM:LastByteOfCharROM*BasedOnSpecifiedFromFile]

### BEGIN EMULATION ###
noerrors = True
while noerrors:
    if cpu(cpu_pc) != True:
        noerrors = False
    cpu_pc = cpu_returnpc

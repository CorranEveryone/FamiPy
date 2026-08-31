##### USER CONFIG (temporary solution) #####
romfilepath = "./roms/Super Mario Bros. (World).nes" # Only .nes files are supported

##### DEFINE ALL VARIABLES HERE #####
# Power Up State
ram = bytearray(b'\x00'*2048) # 2kb ram
## CPU Registers
cpu_a = 0 #00
cpu_x = 0 #00
cpu_y = 0 #00
cpu_pc = 65532 #$FFFC
cpu_s = 253 #FD
cpu_c = 0 #00
cpu_z = 0 #00
cpu_i = 1 #01
cpu_d = 0 #00
cpu_v = 0 #00
cpu_n = 0 #00
## APU Regiseters

##### DEFINE FUNCTIONS HERE #####
def memory(address:bytearray): #address:16bit
    addresspage = address[0:1]
    addressbyte = address[1:2]
    if addresspage == bytearray(b'\x00') or bytearray(b'\x08') or bytearray(b'\x10') or bytearray(b'\x18'): # RAM Page 0
        return ram[addressbyte[0]]
    elif addresspage == bytearray(b'\x01') or bytearray(b'\x09') or bytearray(b'\x11') or bytearray(b'\x19'): # RAM Page 1
            return ram[addressbyte[0+(256*1)]]
    elif addresspage == bytearray(b'\x02') or bytearray(b'\x0A') or bytearray(b'\x12') or bytearray(b'\x1A'): # RAM Page 2
                return ram[addressbyte[0+(256*2)]]
    elif addresspage == bytearray(b'\x03') or bytearray(b'\x0B') or bytearray(b'\x13') or bytearray(b'\x1B'): # RAM Page 3
                return ram[addressbyte[0+(256*3)]]
    elif addresspage == bytearray(b'\x04') or bytearray(b'\x0C') or bytearray(b'\x14') or bytearray(b'\x1C'): # RAM Page 4
                return ram[addressbyte[0+(256*4)]]
    elif addresspage == bytearray(b'\x05') or bytearray(b'\x0D') or bytearray(b'\x15') or bytearray(b'\x1D'): # RAM Page 5
                return ram[addressbyte[0+(256*5)]]
    elif addresspage == bytearray(b'\x06') or bytearray(b'\x0E') or bytearray(b'\x16') or bytearray(b'\x1E'): # RAM Page 6
                return ram[addressbyte[0+(256*6)]]
    elif addresspage == bytearray(b'\x07') or bytearray(b'\x0F') or bytearray(b'\x17') or bytearray(b'\x1F'): # RAM Page 7
                return ram[addressbyte[0+(256*7)]]
    else:
        return 0

def cpu(opcode:int):
    print(opcode)

##### ACTUAL CODE BEGINS #####
### OPEN AND VERIFY ROM ###
romfile = open(romfilepath, "rb")
rom = bytearray(romfile.read())
prgrom = rom[16:(16 + 16384*rom[4])] # [FirstByteOfProgramROM:LastByteOfProgramROM*BasedOnSpecifiedFromFile]
charrom = rom[(16 + 16384*rom[4]):(17 + 16384*rom[4])+(8192*rom[5])] # [FirstByteOfCharROMAfterProgramROM:LastByteOfCharROM*BasedOnSpecifiedFromFile]

print(prgrom)
print(memory(bytearray(b'\x00\x04')))
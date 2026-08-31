##### USER CONFIG (temporary solution) #####
romfilepath = "./roms/Super Mario Bros. (World).nes" # Only .nes files are supported

##### DEFINE ALL VARIABLES HERE #####
# Power Up State
ram = list(b'\x00'*2048) # 2kb ram
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
def memory(address:int): #address:16bit
    if address >= 0 and address <= 2047: # RAM $0000-$07FF
        return ram[address]
    elif address >= 2048 and address <= 4095: # RAM MIRROR $0800-$0FFF
        return ram[address-2048]
    elif address >= 4096 and address <= 6143: # RAM MIRROR $1000-$17FF
            return ram[address-4096]
    elif address >= 6144 and address <= 8191: # RAM MIRROR $1800-$1FFF
            return ram[address-6144]
    else:
        return 0

def cpu(opcode:int):
    print(opcode)

##### ACTUAL CODE BEGINS #####
### OPEN AND VERIFY ROM ###
romfile = open(romfilepath, "rb")
rom = list(romfile.read())
prgrom = rom[16:(16 + 16384*rom[4])] # [FirstByteOfProgramROM:LastByteOfProgramROM*BasedOnSpecifiedFromFile]
charrom = rom[(16 + 16384*rom[4]):(17 + 16384*rom[4])+(8192*rom[5])] # [FirstByteOfCharROMAfterProgramROM:LastByteOfCharROM*BasedOnSpecifiedFromFile]

cpu(0)
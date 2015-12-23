#
# Advent of code
# Day 23
#
# Opening the Turing Lock
#

testProgram = '''inc a
jio a, +2
tpl a
inc a
'''

part1Program='''jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
'''


def execute(instructions, registerA=0, registerB=0, verbose=False):
    registerA = registerA
    registerB = registerB
    
    running = True
    lineCounter = 0
    
    while running:
        instruction = instructions[lineCounter]
        if verbose:
            print("{0:d} {1}".format(lineCounter,
                                     instruction))
        
        assert isinstance(instruction, str)
    
        instruction = instruction.replace(',','')
        instructionBits = instruction.split(' ')
        
        if len(instructionBits) == 3:
            # a conditional jump instruction
            if instructionBits[0] == 'jio': # jump if "1"
                if instructionBits[1] == 'a':
                    if registerA == 1:
                        lineCounter += int(instructionBits[2])
                    else:
                        lineCounter += 1
                else:
                    if registerB == 1:
                        lineCounter += int(instructionBits[2])
                    else:
                        lineCounter += 1
            elif instructionBits[0] == 'jie': #jump if even
                if instructionBits[1] == 'a':
                    if registerA % 2 == 0:
                        lineCounter += int(instructionBits[2])
                    else:
                        lineCounter += 1
                else:
                    if registerB % 2 == 0:
                        lineCounter += int(instructionBits[2])
                    else:
                        lineCounter += 1
        else:
            if instructionBits[0] == 'jmp': # unconditional jump
                lineCounter += int(instructionBits[1])
            elif instructionBits[0] == 'inc': # increment register
                if instructionBits[1] == 'a':
                    registerA += 1
                    lineCounter += 1
                else:
                    registerB += 1
                    lineCounter += 1
            elif instructionBits[0] == 'tpl': # triple register
                if instructionBits[1] == 'a':
                    registerA = registerA * 3
                    lineCounter += 1
                else:
                    registerB = registerB * 3
                    lineCounter += 1
            elif instructionBits[0] == 'hlf': # half register
                if instructionBits[1] == 'a':
                    registerA = registerA // 2
                    lineCounter += 1
                else:
                    registerB = registerB // 2
                    lineCounter += 1
                    
        if lineCounter >= len(instructions):
            running = False
            
    print("Register A: {0:d}".format(registerA))
    print("Register B: {0:d}".format(registerB))
                    
                    
if __name__ == '__main__':                

    testInstructions = testProgram.splitlines()
    part1Instructions = part1Program.splitlines()
    
    print("Test instructions")
    execute(testInstructions)
    print("\nPart 1")
    execute(part1Instructions)
    print("\nPart 2")
    execute(part1Instructions, registerA=1) #255 too low


    
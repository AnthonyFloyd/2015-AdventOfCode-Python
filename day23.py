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
    registers={'a':registerA, 'b':registerB}
    lineCounter = 0
    
    while lineCounter >= 0 and lineCounter < len(instructions):
        
        # parse line, break into instruction, register, and jump (if needed)
        
        instructionLine = instructions[lineCounter].replace(',','')
        instructionBits = instructionLine.split(' ')
        
        if len(instructionBits) == 2:
            instruction, register = instructionBits
            jump = register # take care of jmp without register
        elif len(instructionBits) == 3:
            instruction, register, jump = instructionBits
        else:
            raise RuntimeError("Unknown instruction!")
            
        # every instruction advances to the next line, except jumps which advance more
        lineIncrement = 1
        
        # execute appropriate instruction
        if instruction == 'jio': # jump if "1"
            if registers[register] == 1:
                lineIncrement = int(jump)
                
        elif instruction == 'jie': #jump if even
            if registers[register] % 2 == 0:
                lineIncrement = int(jump)

        elif instruction == 'jmp': # unconditional jump
            lineIncrement = int(jump) 
            
        elif instruction == 'inc': # increment register
            registers[register] += 1
            
        elif instruction == 'tpl': # triple register
            registers[register] *= 3

        elif instructionBits[0] == 'hlf': # half register
            registers[register] //= 2
            
        if verbose: print("{0:d} {1} (a: {2:d}, b: {3:d})".format(lineCounter, instructionLine, registers['a'], registers['b']))
        lineCounter += lineIncrement
            
    print("Register A: {0:d}".format(registers['a']))
    print("Register B: {0:d}".format(registers['b']))
                    
                    
if __name__ == '__main__':                

    testInstructions = testProgram.splitlines()
    part1Instructions = part1Program.splitlines()
    
    print("Test instructions")
    execute(testInstructions)
    print("\nPart 1")
    execute(part1Instructions)
    print("\nPart 2")
    execute(part1Instructions, registerA=1) 


    
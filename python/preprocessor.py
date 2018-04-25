def clean(cfile):
    code = cfile.read().rstrip().split('\n')
    code = list(filter(lambda line: (line != ''), code))
    for i in range(0, len(code)):
        code[i] = code[i].strip()
    code = list(filter(lambda line: (not line.startswith('//')), code))
    #print code
    return code

class Define(object):
    def __init__(self):
        pass

class Include(object):
    def __init__(self):
        pass

class Preprocesser(object):
    def __init__(self, code):
        self.includes = {}  #line number keys with filenames
        self.defines = {}   #defines
        self.if_depth = 0
        
        self.pass1(code)
        self.pass2(code)

    def pass1(self, code):
        for line_num in range(0, len(code)):
            if code[line_num][0] == '#':
                line = code[line_num].split()
                if line[0] == "#includes":
                    self.parse_includes(line)
                    
                elif line[0] == "#define":
                    self.parse_defines(line)
                    
                elif line[0] == "#ifdef":
                    self.if_depth += 1
                    
                elif line[0] == "#endif":
                    self.if_depth -= 1
                    
        print self.defines
        return 0

    def parse_includes(self, line):
        pass
    
    def parse_defines(self, line):
        if len(line) == 2:
            self.defines[line[1]] = None
        elif len(line) > 2:
            #pass
            indices = range(2, len(line))
            #self.defines[line[1]] = " ".join(
            print indices
            self.defines[line[1]] = " ".join([line[i] for i in indices])
        else:
            print "Preproceessor: Insufficient arguments for define"
            exit(1)

    def pass2(self, code):
        #for line_num in range(0, len(code)):
            #line = code[line_num].split()
            #for term in line:
                #print term in self.defines.keys()
                #if term in self.defines.keys():
                    #term = self.defines[term]
            #print line
        #print code
        for line_num in range(0, len(code)):
            code[line_num] = list(map(lambda term: 
                if term in self.defines:
                    

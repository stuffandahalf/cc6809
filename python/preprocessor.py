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
                    pass
                elif line[0] == "#define":
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
                        
                elif line[0] == "#ifdef":
                    self.if_depth += 1
                    
                elif line[0] == "#endif":
                    self.if_depth -= 1
        print self.defines
        return 0

    def pass2(self, code):
        for line_num in range(0, len(code)):
            line = code[line_num].split()
            for term in line:
                print term in self.defines.keys()
                if term in self.defines.keys():
                    term = self.defines[term]
            #print line
        #print code

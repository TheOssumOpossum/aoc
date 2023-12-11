
import math 
import functools

class grid:
    rows = [[]]
    def __init__(self, data=None, integer=False):
        first = True
        self._rows = [[]]
        if isinstance(data,list):
            for i in data:
                if integer:
                    intdata = []
                    for d in i:
                        intdata.append(int(d))
                    self.addRow(intdata)
                else:
                    self.addRow(i)
            if first:
                first = False
                self.rows = self.rows[1:]
        elif isinstance(data, str):
            for i in data.split('\n'):
                if i.strip() == '':
                    continue
                if integer:
                    self.addRow([int(x) for x in [*i.strip()]])
                else:
                    self.addRow([*i.strip()])
                if first:
                    first = False
                    self.rows = self.rows[1:]

    def __getitem__(self, items):
        return self.rows[items]

    def __setitem__(self, key, value):
        self.rows[key] = value

    @property
    def width(self, row=0):
        return len(self.rows[row])

    @property
    def height(self, col=0):
        if col == 0:
            return len(self.rows)
        else:
            h = 0
            for r in self.rows:
                if len(r)-1 >= col:
                    h += 1
                else:
                    break
            return h

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self._rows = rows
        self.cols = [list(x) for x in list(zip(*rows))]
        
    def getVals(self, vals):
        if not isinstance(vals, set):
            vals = set(vals)
        return [x.pos for x in list(filter(lambda x: x.val in vals, [x for x in self.cells()]))]
        
    def cells(self):
        return [cell(row,col,val) for row in range(self.height) for col in range(self.width) for val in self.rows[row][col]]

    def addRow(self, row):
        if len(self.rows[0]) != 0 and len(row) != len(self.rows[0]):
            print("  ERROR: uneven grid width! row-0-width={}, row-{}-width={}".format(len(self.rows[0]), len(self.rows), len(row)))
            return
        self.rows.append([])
        for c in row:
            self.rows[-1].append(c)

    def addCol(self, col):
        if len(self.rows[0]) != 0 and len(col) != len(self.rows):
            print("  ERROR! uneven grid height! col-0-height={}, col-{}-height={}".format(len(self.rows), len(self.rows[0]), len(col)))
            return
        if len(self.rows) == 0:
            self.rows = [[x] for x in col]
            return
        for i in range(len(col)):
            self._rows[i].append(col[i])
        self.rows = self._rows

    def __str__(self):
        tmp = [[' ' if x<=-1 else int(x) for x in range(-2,self.width)]]
        tmp.append([' ' if x == -2 else '/' if x == -1 else '-' for x in range(-2,self.width)])
        for i in range(self.height):
            tmp.append([i,'|'] + self.rows[i])
        spacing = 0
        for i in tmp:
            for j in i:
                spacing = max(spacing, len(str(j)))
        return '\n'.join(''.join(str(i).center(spacing+1) for i in row) for row in tmp)

    def __repr__(self):
        return self.__str__()

    def goUp(self, row, col, include=False,idx=False):
        return self.transit('U',col,row,include, idx)

    def downTo(self, row, col, include=True,idx=False):
        return self.goUp(row,col,include, idx)[::-1]

    def goDown(self, row, col, include=False,idx=False):
        return self.transit('D',col,row,include, idx)

    def UpTo(self, row, col, include=True,idx=False):
        return self.goDown(row,col,include, idx)[::-1]

    def goRight(self, row, col, include=False,idx=False):
        return self.transit('R', col, row, include, idx)

    def leftTo(self, row, col, include=True,idx=False):
        return self.goRight(row,col,include, idx)[::-1]

    def goLeft(self, row, col, include=False,idx=False):
        return self.transit('L',col, row, include, idx)

    def rightTo(self, row, col, include=True,idx=False):
        return self.leftTo(row,col,include, idx)[::-1]

    def transit(self,instructions,x=0,y=0,include=True,idx=False):
        if isinstance(instructions,str):
            ins = []
            for i in instructions:
                ins.append(i)
            instructions = ins
        if instructions[-1] != 'z':
            instructions.append('zzz')
        viz = set()
        seq = []
        i = 0
        revisit = False
        while 0 <= x <= self.width-1 and 0 <= y <= self.height-1 and i <= len(instructions) and ((y,x) not in viz or (revisit and (y,x,i) not in viz) or instructions[i] in ['l','r','u','d']):
            if revisit:
                viz.add((y,x,i))
            if instructions[i] == 'z':
                i = 0
            viz.add((y,x))
            if include and not revisit:
                seq.append((y,x))
            else:
                include = True
            revisit = False
            match instructions[i]:
                case 'zzz':
                    break
                case 'l':
                    x -= 1
                    i += 1
                case 'r':
                    x += 1
                    i += 1
                case 'd':
                    y += 1
                    i += 1
                case 'u':
                    y -= 1
                    i += 1
                case 'L':
                    x -= 1
                    if (y,x) in viz:
                        x += 1
                        i += 1
                        revisit = True
                        continue
                    if x == 0:
                        i += 1
                case 'R':
                    x += 1
                    if (y,x) in viz:
                        x -= 1
                        i += 1
                        revisit = True
                        continue
                    if x == self.width-1:
                        i += 1
                case 'D':
                    y += 1
                    if (y,x) in viz:
                        y -= 1
                        i += 1
                        revisit = True
                        continue
                    if y == self.height-1:
                        i += 1
                case 'U':
                    y -= 1
                    if (y,x) in viz:
                        y += 1
                        i += 1
                        revisit = True
                        continue
                    if y == 0:
                        i += 1
        vals = []
        for i in seq:
            if idx:
                vals.append([i[0],i[1]])
            else:
                vals.append(self.rows[i[0]][i[1]])
        return vals

class cell:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

    def __str__(self):
        return f'|row,col:({self.row},{self.col}) ' + f'val:\'{self.val}\'|' if isinstance(self.val, str) else f'val:{self.val}|'
    
    def __repr__(self):
        return self.__str__()

    def __getitem__(self, items):
        match items:
            case 0:
                return self.row
            case 1:
                return self.col
            case 2:
                return self.val
            case _:
                assert False
                
    def __setitem__(self, key, value):
        match key:
            case 0:
                self.row = value
            case 1:
                self.col = value
            case 2:
                self.val = value
            case 3:
                assert False
                
    @property
    def pos(self):
        return (self.row, self.col)

import re

class PrimitiveDataType:
    def __init__(self):
        pass
    
    def date(self):
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
         'Septepber', 'October', 'November', 'December']
        # 1 - 31, 01-09, BC AC
        
    def numeric(self, value):
        p = re.compile(r'(\d+([\.,]\d+)*)')

        pos = 0
        
        values = []
        
        while 1:
            m = p.search(value, pos)
            
            if m:
                #print m.groups(), m.group(1)
                values += [m.group(1)]
                pos = m.end()
            else:
                break
            
        print '-----' * 5
        print map(lambda x: re.sub(',', '', x), values)
        print map(lambda x: len(x), values), 'of', len(value)
        print '-----' * 5
        
obj = PrimitiveDataType()

obj.numeric('1,331,330,000')
obj.numeric('June 17, 2009')
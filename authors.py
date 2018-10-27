title = ''
column1 = ''
column2 = ''
string = ''
integer = 0
rip = []
dp = ''
integers = []
strings = []
i = 0

def title_fun():
    global title
    title = input('Enter a title for the data:\n')
    print('You entered:', title)
    print()
    return

def columns():
    global column1, column2
    column1 = input('Enter the column 1 header:\n')
    print('You entered:', column1)
    print()
    column2 = input('Enter the column 2 header:\n')
    print('You entered:', column2)
    print()
    return

def data():
        global string, integer, rip, dp, strings, integers
        contin = 'start'
        while contin == 'start':
            dp = input('Enter a data point (-1 to stop input):\n')
            if dp == '-1':
                break
            else:
                commas = dp.count(',')
                if commas == 0:
                    print('Error: No comma in string.')
                    print()
                elif commas > 1:
                    print('Error: Too many commas in input.')
                    print()
                else:
                    rip = dp.split(',')
                    test = rip[1]
                    test = test.strip()
                    if not test.isnumeric():
                        print('Error: Comma not followed by an integer.')
                        print()
                        
                    else:
                        string = rip[0]
                        strings.append(string)
                        integer = int(rip[1])
                        integers.append(integer)
                        print('Data string:', string)
                        print('Data integer:', integer)
                        print()
        return

def table():
    global title, column1, column2
    print('%33s' % title)
    print('%-19s | %22s' % (column1, column2))
    print('-' * 44)
    for i in range(len(strings)):
        print('%-19s | %22d' % (strings[i], integers[i]))
    
def histo():
    if i in range(len(strings)):
        print('%20s' % strings[i], '*'*integers[i])
    return

title_fun()
columns()
data()
print()
table()
print()
histo()


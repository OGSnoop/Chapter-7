def needstring():
    cake = 'True'
    while  cake == 'True':
        comma_st = input('Enter input string:\n')
        commas = comma_st.find(',')
        if comma_st == 'q':
            cake = 'False'
        else:
            if commas < 0:
                print('Error: No comma in string.')
                print()

            elif commas >= 0:
                tokens = comma_st.split(',')
                st1 = tokens[0]
                st2 = tokens[1]
                st1 = st1.strip()
                st2 = st2.strip()
                print('First word:', st1)
                print('Second word:', st2)
                print()
        
    return
    

needstring()

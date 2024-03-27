def one_hot(input_file, output_file):
    with open(input_file, 'r') as inf:
        sequences = inf.readlines()
        
    with open(output_file, 'w') as outf:
        for sequence in sequences:
            
            sequence = sequence.strip()
            a_enc = ''
            c_enc = ''
            g_enc = ''
            t_enc = ''
            
            for char in sequence:
                if char == 'a' or char == 'A':
                    a_enc += '1'
                    c_enc += '0'
                    g_enc += '0'
                    t_enc += '0'
                elif char == 'c' or char == 'C':
                    a_enc += '0'
                    c_enc += '1'
                    g_enc += '0'
                    t_enc += '0'
                elif char == 'g' or char == 'G':
                    a_enc += '0'
                    c_enc += '0'
                    g_enc += '1'
                    t_enc += '0'
                elif char == 't' or char == 'T':
                    a_enc += '0'
                    c_enc += '0'
                    g_enc += '0'
                    t_enc += '1'
                else:
                    a_enc += '0'
                    c_enc += '0'
                    g_enc += '0'
                    t_enc += '0'
                    print("encountered non-acgt")
            
            outf.write(a_enc + '\n' + c_enc + '\n' + g_enc + '\n' + t_enc + "\n\n")

if __name__ == "__main__":
    input_file = "C:\\Users\\sdelozi\\projects\\CS_590_HW1\\p1\\pos\\ENCFF027BPY_pos.txt"
    output_file = "C:\\Users\\sdelozi\\projects\\CS_590_HW1\\p2\\pos_enc\\ENCFF027BPY_pos_enc.txt"
    
    one_hot(input_file, output_file)
    
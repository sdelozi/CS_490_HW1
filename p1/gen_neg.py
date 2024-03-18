def generate_negative_bed(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        previous_end = None
        for line in infile:
            fields = line.strip().split('\t')
            chrom, start, end = fields[0], int(fields[1]), int(fields[2])
            if previous_end is not None and previous_end < start:
                # Generate negative interval
                neg_start = previous_end
                neg_end = start
                outfile.write(f"{chrom}\t{neg_start}\t{neg_end}\n")
            previous_end = end

if __name__ == "__main__":
    input_file = "C:\\Users\\deloz\\Projects\\CS_590_HW1\\p1\\data\\ENCFF829XGX.bed"
    output_file = "C:\\Users\\deloz\\Projects\\CS_590_HW1\\p1\\data\\ENCFF829XGX_neg.bed"
    
    generate_negative_bed(input_file, output_file)
    print("Negative BED file generated:", output_file)
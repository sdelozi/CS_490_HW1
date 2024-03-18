def calculate_percentile(sequence_lengths, percentile):
    sorted_lengths = sorted(sequence_lengths)
    index = int(percentile / 100.0 * len(sorted_lengths))
    return sorted_lengths[index]

def calculate_target_length(input_file, percentile=95):
    sequence_lengths = []
    with open(input_file, 'r') as infile:
        for line in infile:
            if not line.startswith('>'):  # Ignore header lines
                sequence_lengths.append(len(line.strip()))
    
    target_length = calculate_percentile(sequence_lengths, percentile)
    return int(target_length)

def crop_sequences(input_file, output_file, target_length):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.startswith('>'):  # Ignore header lines
                sequence = line.strip()
                if len(sequence) >= target_length:  # Check if sequence meets target length
                    #sequence = sequence[:target_length]  # Crop sequence to target length
                    start_index = (len(sequence) - target_length) // 2
                    end_index = start_index + target_length
                    sequence = sequence[start_index:end_index]  # Crop sequence equally from both ends
                    outfile.write(sequence + '\n')  # Write cropped sequence to output file

if __name__ == "__main__":
    input_file = "C:\\Users\\deloz\\Projects\\CS_590_HW1\\p1\\nucleotides\\ENCFF027BPY.txt"
    output_file = "C:\\Users\\deloz\\Projects\\CS_590_HW1\\p1\\pos\\ENCFF027BPY_pos.txt"
    
    target_length = calculate_target_length(input_file, percentile=25)  # Adjust percentile as needed
    print("Target sequence length:", target_length)
    
    crop_sequences(input_file, output_file, target_length)
    print("Sequences cropped and written to", output_file)
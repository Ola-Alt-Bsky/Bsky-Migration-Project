import glob

twitter_copy_folder = 'Twitter Copies/*'
files = glob.glob(twitter_copy_folder)
unique_lines = set()

# Read lines from each file and add them to the set
for file in files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as follower_file:
        for line in follower_file:
            stripped_line = line.strip()  # Remove leading/trailing whitespace
            if stripped_line.startswith('@'):
                unique_lines.add(stripped_line)

# Convert the set to a list and split into chunks of 800 lines each
unique_lines_list = list(unique_lines)
chunk_size = 800
chunks = [unique_lines_list[i:i + chunk_size] for i in range(0, len(unique_lines_list), chunk_size)]

# Write each chunk to a separate file
for i, chunk in enumerate(chunks):
    output_filename = f'Twitter Copies/Combined_Followers_Part_{i + 1}.txt'
    with open(output_filename, 'w') as combined_file:
        for line in chunk:
            combined_file.write(line + '\n')

print(f"Created {len(chunks)} files with up to {chunk_size} lines each.")

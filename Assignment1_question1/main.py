"""
    Olympics_Medals
"""
import os
from argparse import ArgumentParser as  ap
def process_files(folder_name):
    """
    To execute the this program use this format:python medals.py folder
    here folder is the path of the testcase folder which contains the data
    """
    folder_path = os.path.join(folder_name)
    counts = {}
    # Walk through the directory to find all text files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as file_inside:
                    for line in file_inside:
                        parts = line.strip().split('-')
                        country = parts[0]
                        gold_medals = int(parts[1])
                        silver_medals = int(parts[2])
                        bronze_medals = int(parts[3])
                        if country in counts:
                            # Update the existing counts
                            counts[country][0] += gold_medals
                            counts[country][1] += silver_medals
                            counts[country][2] += bronze_medals
                        else:
                            # Create a new entry
                            counts[country] = [gold_medals, silver_medals, bronze_medals]
    return counts
def sort_data(m_counts):
    """
    Sorted the data on the basis of number of gold medals
    and alphabetical order of country name in case of tie.
    """
    sorted_countries = sorted(m_counts.items(), key=lambda x: (-x[1][0], x[0]))
    sorted_data = {country: medals for country, medals in sorted_countries}
    return sorted_data
if __name__ == "__main__":
    # Set up argument parsing
    parser = ap()
    parser.add_argument('folder_name', type=str, help='folder name containing text files')
    args = parser.parse_args()
    # Process the files and print the result
    medal_counts = process_files(args.folder_name)
    print(sort_data(medal_counts))

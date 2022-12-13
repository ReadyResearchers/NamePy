"""Perform data processing using cron jobs implemented in Python."""

# Add all of the required imports
import schedule
import time
from faker import Faker
import os, glob
import sys
import datetime
import csv
from collections import defaultdict

generate_counter = 0
fake = Faker()

# Implement the following features:
#
# 1)** Delete all of the files in the data/ directory before execution
# 2) Run a data generation task that will create audio file data and save it to a CSV file
# 3) Run a data summarization task that will summarize audio file data and save it to a CSV file
# 4) Parse the command-line arguments to the program and configure the data processor
# 5)** Display diagnostic information about all of the provided command-line arguments
# 6)** Display timestamped information about how the program runs the generation and summarization tasks
# 7)** Do not display a stack trace if a person types CTRL-c and exit with a zero exit code
# 8) Produce a zero exit code in all cases in which the program runs to completion without error
# 9) Produces a non-zero exit code only in cases when, for instance, it experiences corrupted files
# 10) Runs correctly in a virtual environment called venv that contains all of its dependencies

# review the content in the README.md file for additional details about this project


def delete_data():
    """Deletes all csv files in the data directory."""
    for filename in glob.iglob("data/*.csv", recursive=True):
        os.remove(filename)
    # print("deletion worked")


def generate():
    """Generates random audio files and sizes written to generated.csv."""
    global generate_counter
    generate_counter += 1
    now = datetime.datetime.now()
    print(now.strftime("%a %b %d %H:%M:%S %Y Generating Data"))
    # Was not sure how to leverage the range operation in this case, 
    # so I used separate providers.
    # for _ in range(10):
    x0 = fake.file_name(category="audio")
    x1 = fake.file_name(category="audio")
    x2 = fake.file_name(category="audio")
    x3 = fake.file_name(category="audio")
    x4 = fake.file_name(category="audio")
    x5 = fake.file_name(category="audio")
    x6 = fake.file_name(category="audio")
    x7 = fake.file_name(category="audio")
    x8 = fake.file_name(category="audio")
    x9 = fake.file_name(category="audio")
    y0 = fake.random_int(min=0, max=1024)
    y1 = fake.random_int(min=0, max=1024)
    y2 = fake.random_int(min=0, max=1024)
    y3 = fake.random_int(min=0, max=1024)
    y4 = fake.random_int(min=0, max=1024)
    y5 = fake.random_int(min=0, max=1024)
    y6 = fake.random_int(min=0, max=1024)
    y7 = fake.random_int(min=0, max=1024)
    y8 = fake.random_int(min=0, max=1024)
    y9 = fake.random_int(min=0, max=1024)
    with open("data/generated.csv", mode="a") as music_file:
        song = csv.writer(music_file)
        song.writerow([x0, y0])
        song.writerow([x1, y1])
        song.writerow([x2, y2])
        song.writerow([x3, y3])
        song.writerow([x4, y4])
        song.writerow([x5, y5])
        song.writerow([x6, y6])
        song.writerow([x7, y7])
        song.writerow([x8, y8])
        song.writerow([x9, y9])


def summarize():
    """Writes the means of generated.csv file sizes to summary.csv"""
    now = datetime.datetime.now()
    print(now.strftime("%a %b %d %H:%M:%S %Y Summarizing Data"))
    columns = defaultdict(list)
    with open("data/generated.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            for (i, v) in enumerate(line):
                columns[i].append(v)
    x = [int(value) for value in columns[1]]
    y = (sum(x)) / (len(x))
    z = len(columns[0]) + 1
    list01 = []
    len_list = []
    with open("data/summary.csv", mode="a") as summary_file:
        summary = csv.writer(summary_file)
        list01.append(y)
        len_list.append(z)
        summary.writerow([len_list, list01])


def main():
    global fake
    arg0 = sys.argv[0]
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    arg3 = int(sys.argv[3])
    Faker.seed(0)
    print("\nprocess: Schedule data generation and processing\n")
    print("Summary of command-line arguments: ")
    print("  Number of arguments:", len(sys.argv))
    print("  Name of the program:", arg0)
    print("  Data Generation maximum:", arg1, "generation rounds")
    print("  Data generation periodicity:", arg2, "seconds")
    print("  Data summarization periodicity:", arg3, "seconds\n")
    print("Deleting any existing data or summary CSV files!")
    delete_data()
    print("Starting to run the cron job scheduler!\n")
    schedule.every(arg2).seconds.do(generate)
    schedule.every(arg3).seconds.do(summarize)
    global generate_counter
    while True:
        try:
            if generate_counter == arg1:
                break
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("")
            exit()


if __name__ == "__main__":
    main()
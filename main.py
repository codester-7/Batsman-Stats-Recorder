import pandas as pd
import csv
from data_entry import get_name, get_matches, get_runs_scored, get_strike_rate, get_average
import matplotlib.pyplot as plt

class CSV:

    CSV_FILE = "batsman_stats_recorder.csv"
    COLUMNS = ["Name", "Matches", "Runs Scored", "Strike Rate", "Average"]    # specifying columns to be used

    @classmethod
    def initialise_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)       
            df.to_csv(cls.CSV_FILE, index=False)


    @classmethod
    def add_entry(cls, name, matches, runs_scored, strike_rate, average):
        new_entry = {
            "Name": name,
            "Matches": matches,
            "Runs Scored": runs_scored,
            "Strike Rate": strike_rate,
            "Average": average
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:     # CONTEXT MANAGER - automatically closes file after entries have been added
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")


with open('batsman_stats_recorder.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)


def add():
    CSV.initialise_csv()
    name = get_name()
    matches = get_matches()
    runs_scored = get_runs_scored()
    strike_rate = get_strike_rate()
    average = get_average()
    CSV.add_entry(name, matches, runs_scored, strike_rate, average)



def plot_bar_chart():
    df = pd.read_csv(CSV.CSV_FILE)
    if df.empty:
        print("No data available to plot...")
        return
    
    plt.figure(figsize=(10,6))
    plt.bar(df["Name"], df["Runs Scored"])
    plt.xlabel("Player Name")
    plt.ylabel("Runs Scored")
    plt.title("Most Runs Scored in Season")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def main():
    while True:
        print("\n1. Add player stats")
        print("2. View all player stats")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            df = pd.read_csv('batsman_stats_recorder.csv')
            print(df)

            if input("Do you want to see a bar chart of the data? (y/n) ").lower() == "y":
                plot_bar_chart()
                
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()





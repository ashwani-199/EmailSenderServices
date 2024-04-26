import csv


class ReadCSV():
    def __init__(self) -> None:
        pass

    # Read the CSV file
    @staticmethod
    def read_file(csv_file):
        recipients = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recipients.append((row['Name'], row['Email']))
        
        return recipients


    @staticmethod
    def read_file_sender(csv_file):
        sender_details = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sender_details.append((row['Email'], row['Password'], row['Subject']))
        
        return sender_details
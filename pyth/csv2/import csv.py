import csv
import os
import random

class CSVProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_csv()

    def load_csv(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    def show(self, output_type='top', num_rows=5, separator=','):
        header = self.data[0]
        rows = self.data[1:]

        if output_type == 'bottom':
            rows_to_show = rows[-num_rows:]
        elif output_type == 'random':
            rows_to_show = random.sample(rows, min(num_rows, len(rows)))
        else:
            rows_to_show = rows[:num_rows]

        print(f"{' | '.join(header)}")
        for row in rows_to_show:
            print(f"{' | '.join(row)}")

    def info(self):
        header = self.data[0]
        rows = self.data[1:]

        print(f"Колво строк и столбов: {len(rows)}x{len(header)}")

        for i, field in enumerate(header):
            non_empty_values = sum(1 for row in rows if row[i])
            value_type = 'string' if any(row[i].isalpha() for row in rows) else 'int'
            print(f"{field} {non_empty_values} {value_type}")

    def del_nan(self):
        header = self.data[0]
        rows = self.data[1:]
        self.data = [header] + [row for row in rows if all(field for field in row)]

    def make_ds(self):
        header = self.data[0]
        rows = self.data[1:]

        random.shuffle(rows)
        split_index = int(0.7 * len(rows))
        train_data = [header] + rows[:split_index]
        test_data = [header] + rows[split_index:]

        os.makedirs('C:\Users\User\Desktop\PROGVS\csv2', exist_ok=True)
        

        with open('C:\Users\User\Desktop\PROGVS\csv2\data.csv', 'w', newline='') as train_file:
            writer = csv.writer(train_file)
            writer.writerows(train_data)

        with open('C:\Users\User\Desktop\PROGVS\csv2\data.csv', 'w', newline='') as test_file:
            writer = csv.writer(test_file)
            writer.writerows(test_data)


# Example usage:
processor = CSVProcessor('data.csv')
processor.show(output_type='top', num_rows=5, separator=',')
processor.info()
processor.del_nan()
processor.make_ds()
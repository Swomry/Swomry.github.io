import csv, time, os
from collections import Counter

dayCount = [12278385, 30052580, 47857940]

countLimit = 2



def tester(day):
    with open(f'C:/Users/Swomr/Desktop/rPlace/rPlaceDays/rPlaceDay{day}.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            #day = int(line[0].split(' ')[0].split('-')[2])
            print(line)

def test():
    os.system('cls')
    start = time.time()
    lineCount = 0
    with open('C:/Users/Swomr/Desktop/rPlace/rPlace.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = []

        for line in reader:
            day = int(line[0].split(' ')[0].split('-')[2])
            with open(f'C:/Users/Swomr/Desktop/rPlace/rPlaceDays/rPlaceDay{day}.csv', 'a', newline='') as wfile:
                writer = csv.writer(wfile)
                

                lineCount += 1
                writer.writerow(line)
                wfile.flush()
                wfile.close()
                end = time.time()

            print("\033[H\033[x", end="")
            print(f"{lineCount} in {str(end - start).split('.')[0]} seconds.")
            print(line)


def count():
    os.system('cls')
    start = time.time()
    count = 0
    with open('C:/Users/Swomr/Desktop/rPlace/rPlace.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            count += 1
            print("\033[H\033[x", end="")
            print(count)
        seconds = time.time() - start
        minutes = seconds/60
        print(f'Task took {time} seconds\nor {minutes} minutes\nor {minutes/60} hours')
        

        

        
        
        
            



count()
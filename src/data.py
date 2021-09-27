import csv


def csv_data_writer(*args):
    with open("data/derivative.csv", mode="a") as w_file:
        file_writer = csv.writer(w_file, lineterminator="\r", delimiter=',')
        for index in range(len(args[0])):
            row = [args[i][index] for i in range(len(args))]
            file_writer.writerow(row)


def clean_data(file_name="data/derivative.csv"):
    #можно вообще os.remove("filename.csv")
    f = open(file_name, "w")
    f.truncate()
    f.close()


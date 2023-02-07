import xlwings as xw
import time

def main():
    # Access the active Excel workbook
    wb = xw.Book.active

    # Access a specific sheet
    sht = wb.sheets[0]

    # Define a list to save to Excel
    my_list = [1, 2, 3, 4, 5]

    # Write the list to Excel starting at cell A1
    sht.range("A1").value = 444

    time.sleep(100000)


if __name__ == '__main__':
    main()

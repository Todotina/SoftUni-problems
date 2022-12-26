import re

barcode_pattern = r'@#+[A-Z][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]+[A-Z]@#+'
group_pattern = r'\d+'


def valid_barcode(string):
    barcode = re.findall(barcode_pattern, string)
    if len(barcode) > 0:
        product_group = re.findall(group_pattern, string)
        if len(product_group) < 1:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")
    else:
        print("Invalid barcode")


count_of_barcodes = int(input())
for string in range(count_of_barcodes):
    current_string = input()
    valid_barcode(current_string)

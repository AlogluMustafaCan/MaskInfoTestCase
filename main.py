from CsvFieldMask import CsvFieldMask

csv_processor = CsvFieldMask('/Users/can/Documents/Python/dev/MaskInfoTestCase', 'Test_Customers.csv',
                             'Masked_Clients.csv')
if __name__ == '__main__':
    csv_processor.mask_fields()

# TestCase
Given requirements in `Statement.md` are implemented in `CvsFiledMask.py`.

## Usage is in example main.py file

```python
from CsvFieldMask import CsvFieldMask

csv_processor = CsvFieldMask('/Users/canaloglu/Documents/PycharmProjects/TestCaseVodafone', 'Test_Customers.csv',
                              'masked_clients.csv')
if __name__ == '__main__':
    csv_processor.mask_fields()
```
```
CsvFieldMask(path,input_filename,output_filename)
```

## Usage in CMD
Open a Shell in the directory where CsvFieldMask.py locates.
```shell
python
>>> from CsvFieldMask import CsvFieldMask
>>> csv_processor = CsvFieldMask('/Users/canaloglu/Documents/PycharmProjects/TestCaseVodafone', 'Test_Customers.csv',
                              'masked_clients.csv')
>>> csv_processor.mask_fields()
```

## Example Test Input File
```
ID,Name,Email,Billing,Location
1,John Smith,john@mail.com,15000,New York
2,Kelly Lawrence Gomez,Kelly@your-mail.com,20000,Washington
3,Carl Winslow,carl-wins@mail-bot.com, ,Seattle
4,Roger Rogers,doubleR@mailer.com,12400.27,Boston
5,Gerald Frances, gf@jmail.com,53000,Dallas
6,Roger Rogers,doubleR@mailer.com,5000,Boston
7,Roger Rogers,doubleR@mailer.com,1000,Boston
8,Gerald Frances, gf@jmail.com,100,Dallas
9,M_u-s!t%a+f$(a)[]*! Can Aloglu,can@gmail.com,10000,Istanbul
10,±!@£$%@^&*()_+¡€#¢∞§¶•@ªº–≠<>,,,
```

## Example Test Output File
```
ID,Name,Email,Billing,Location
1,XXXX XXXXX,XXXX@XXXX.XXX,XXXXX,New York
2,XXXXX XXXXXXXX XXXXX,XXXXX@XXXXXXXXX.XXX,XXXXX,Washington
3,XXXX XXXXXXX,XXXXXXXXX@XXXXXXXX.XXX,,Seattle
4,XXXXX XXXXXX,XXXXXXX@XXXXXX.XXX,4850.0675,Boston
5,XXXXXX XXXXXXX,XX@XXXXX.XXX,26550.0,Dallas
6,XXXXX XXXXXX,XXXXXXX@XXXXXX.XXX,4850.0675,Boston
7,XXXXX XXXXXX,XXXXXXX@XXXXXX.XXX,4850.0675,Boston
8,XXXXXX XXXXXXX,XX@XXXXX.XXX,26550.0,Dallas
9,XXXXXXXXXXXXXXXXXXX XXX XXXXXX,XXX@XXXXX.XXX,XXXXX,Istanbul
10,XX@XXX@XXXXXXXXXXXXXXX@XXXXXX,,,
```



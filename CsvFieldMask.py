class CsvFieldMask:
    email_store = {}

    # Constructor
    def __init__(self, path, in_file_name, out_file_name):
        self.path = path
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name

    def name_billing_min_avg_max(self, results):
        name_list = []
        billing_list = []
        for num in range(1, len(results)):
            name_list.append(len(results[num][0].replace(" ", "")))  # delete the whitespace first to get real len of the name
            billing = results[num][2].replace(" ", "")
            if billing:
                billing_list.append(float(billing))
        print("Name: Max. {}, Min. {}, Avg. {}".format(max(name_list), min(name_list),
                                                       sum(name_list) / len(name_list)))
        print("Billing: Max. {}, Min. {}, Avg. {}".format(max(billing_list), min(billing_list),
                                                          sum(billing_list) / len(billing_list)))

    def mask_fields(self):
        try:
            input_file = open(self.path + '/' + self.in_file_name, 'r', encoding="utf8")
            output_file = open(self.path + '/' + self.out_file_name, 'w', encoding="utf8")
            lines = [line.rstrip() for line in input_file]  # type(lines) = List
            # checking of if there is more then one customer in the csv file.

            results = []
            for line in lines:
                words = line.split(',')
                # type(words) = List
                results.append(words[1:])
            self.check_email_duplication(results)

            # Sensitive data fields (Name, Email) will be masked
            # Billing sensitive data field will only be masked if there exists one billing per client
            # otherwise avg. will be written.

            first = True
            for line in lines:
                words = line.split(',')
                if first:
                    output_file.write(line + "\n")
                    first = False
                else:
                    out_word = ''
                    for num in range(0, len(words)):
                        if num == 0:
                            out_word = words[num].strip() + ","
                        elif num == 3:  # billing column
                            if words[num - 1] in self.email_store:
                                out_word += str(self.email_store[words[num - 1]]) + ","
                            else:
                                masked_word = self.replace_with_mask(words[num].strip())
                                out_word += masked_word + ","
                        elif num == 4:
                            out_word += words[num].strip()
                        else:
                            masked_word = self.replace_with_mask(words[num].strip())
                            out_word += masked_word + ","
                    output_file.write(out_word + "\n")
            print("Masked output file has been created in '"'{}'"'".format(self.path + "/" + self.out_file_name))
            self.name_billing_min_avg_max(results)
        except(OSError, Exception) as exc:
            print("mask_fields() exception handler : " + str(exc))
        finally:
            input_file.close()
            output_file.close()

    # checks email multiplicity
    def check_email_duplication(self, results):
        for num in range(1, len(results)):
            email = results[num][1]
            if email not in self.email_store:
                avg_billing = results[num][2]
                for num1 in range(num + 1, len(results)):
                    if email == results[num1][1]:
                        avg_billing = (float(avg_billing) + float(results[num1][2])) / 2
                        self.email_store[email] = avg_billing
            else:
                break

    # Implements mask algorithm
    def replace_with_mask(self, in_word):
        out_word = ""
        for char in in_word:
            if (char != "@") and (char != ",") and (char != ".") and (char != " "):
                out_word += "X"
            else:
                out_word += char
        return out_word

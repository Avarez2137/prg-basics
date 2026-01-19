import re
def f(dates):
    test = r'^\d{1-2} [A-Z][a-z] \d{4}$'
    listFinal = []

    list = re.findall (r'\d+ [A-Z][a-z]+ \d\d\d\d', dates)

    list1 = re.findall (r'\d [A-Z][a-z]+ \d\d\d\d', dates)

    list2 = re.findall (r'\d\d [A-Z][a-z]+ \d\d\d\d', dates)

    for i in list:
        if i in list1 or i in list2:
            listFinal.append(i)

    return listFinal


if __name__ == "__main__":
    dates = "17 July 1999; 05/12/2024; Apro; 7 20014, 9 May 2007;;2001-12-07:,1 May 23"
    print(f(dates))
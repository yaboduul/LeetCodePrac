def main():
    data = ("Robin", 10, "chocolates")
    a,b,c = data
    format_string = 'Hello {}. You are currently lef with {} {}'
    print(format_string.format(a,b,c)) 
    
    return 0

if __name__ == '__main__':
    main()
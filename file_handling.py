def modify_content(content):
    return content.upper()

def main():
    try:
        input_filename = input('Enter the name of the file to read')

        with open(input_filename, "r") as infile:
            content = infile.read()
            print('File read successfully')

        modified_content = modify_content(content)
        
        output_filename = f'modified_{input_filename}'
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
            print(f'Modified content written ti: {output_filename}')

    except FileNotFoundError:
        print('Error: The file you specified does not exit.')
    except IOError:
        print('Error: The file could not be read or written')
    except Exception as e:
        print(f'An unexpected error occured: {e}')

if __name__ =="__main__":
    main()
# Backward compatibility wrapper
import sys

from reader import read_excel


def main():
    if len(sys.argv) < 2:
        print("Usage: python read_excel.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    df = read_excel(file_path)
    
    if df is not None:
        print(f"Successfully read {len(df)} rows from {file_path}")
        print(df.head())


if __name__ == "__main__":
    main() 


        

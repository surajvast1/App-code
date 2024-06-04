import struct

def write_records_to_file(filename, records):
    with open(filename, 'wb') as file:
        for record in records:
            item_no = record[0]
            item_name = record[1].ljust(20)  # Pad the item name to 20 characters
            qty = record[2]
            price = record[3]
            packed_data = struct.pack('i20sif', item_no, item_name.encode('utf-8'), qty, price)
            file.write(packed_data)

def read_records_from_file(filename):
    records = []
    record_struct = struct.Struct('i20sif')
    with open(filename, 'rb') as file:
        while chunk := file.read(record_struct.size):
            unpacked_data = record_struct.unpack(chunk)
            item_no = unpacked_data[0]
            item_name = unpacked_data[1].decode('utf-8').strip()
            qty = unpacked_data[2]
            price = unpacked_data[3]
            records.append((item_no, item_name, qty, price))
    return records
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def display_records(records):
    for record in records:
        item_no, item_name, qty, price = record
        amount = qty * price
        print(f"Item No: {item_no}")
        print(f"Item Name: {item_name}")
        print(f"Quantity: {qty}")
        print(f"Price per item: {price:.2f}")
        print(f"Amount: {amount:.2f}\n")

def main():
    filename = 'items.dat'
    
    num_records = int(input("Enter the number of records to be entered: "))
    records = []
    
    for _ in range(num_records):
        item_no = int(input("Enter Item No: "))
        item_name = input("Enter Item Name: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price per item: "))
        records.append((item_no, item_name, qty, price))
    
    write_records_to_file(filename, records)
    
    print("\nDisplaying records from the file:")
    stored_records = read_records_from_file(filename)
    display_records(stored_records)

if __name__ == "__main__":
    main()

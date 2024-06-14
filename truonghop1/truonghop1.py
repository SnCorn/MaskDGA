import pandas as pd
import random

def insert_random_hyphens(domain):
    # Tách phần tên miền trước dấu chấm
    name, rest = domain.split('.', 1)
    
    # Giữ nguyên ký tự đầu tiên của phần tên miền trước dấu chấm
    first_char = name[0]
    remaining_name = name[1:]
    
    # Chia đôi phần còn lại của tên miền
    middle_index = len(remaining_name) // 2
    first_part = remaining_name[:middle_index]
    second_part = remaining_name[middle_index:]
    
    # Tạo danh sách các ký tự từ phần đầu
    char_list = list(first_part)
    
    # Chọn ngẫu nhiên số lượng vị trí để thêm dấu '-'
    num_hyphens = random.randint(1, len(char_list))
    
    # Chọn ngẫu nhiên các vị trí để thêm dấu '-'
    hyphen_positions = random.sample(range(len(char_list)), num_hyphens)
    
    # Chèn dấu '-' vào các vị trí đã chọn
    for pos in hyphen_positions:
        char_list[pos] = '-'
    
    # Tạo lại phần đầu đã được thay thế
    replaced_part = ''.join(char_list)
    
    # Tạo tên miền mới
    new_domain = first_char + replaced_part + second_part + '.' + rest
    
    return new_domain

# Đọc file data.csv
df = pd.read_csv('data.csv')

# Giả sử tên miền nằm trong cột 'domain', bạn có thể thay đổi tên cột phù hợp
df['masked_domain'] = df['domain'].apply(insert_random_hyphens)

# Chỉ giữ lại cột mới tạo
df_new = df[['masked_domain']]

# Ghi kết quả ra file truonghop1.csv
df_new.to_csv('truonghop1.csv', index=False)

print("File truonghop1.csv đã được tạo thành công!")

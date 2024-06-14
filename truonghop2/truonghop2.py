import pandas as pd
import random

def replace_with_random_numbers_and_hyphens(domain):
    # Tách phần tên miền trước dấu chấm
    name, rest = domain.split('.', 1)
    
    # Chia đôi phần tên miền trước dấu chấm
    middle_index = len(name) // 2
    first_part = name[:middle_index]
    second_part = name[middle_index:]
    
    # Tạo danh sách các ký tự từ phần đầu
    char_list = list(first_part)
    
    # Xác định số lượng ký tự sẽ được thay thế
    num_replacements = random.randint(1, len(char_list))
    num_hyphens = random.randint(1, len(char_list) - 1)  # Giảm 1 để không thay thế ký tự đầu tiên bằng dấu gạch ngang
    
    # Chọn ngẫu nhiên các vị trí để thay thế
    replacement_positions = random.sample(range(len(char_list)), num_replacements)
    hyphen_positions = random.sample(range(1, len(char_list)), num_hyphens)  # Bắt đầu từ 1 để bỏ qua ký tự đầu tiên
    
    # Thay thế các ký tự tại các vị trí đã chọn bằng số ngẫu nhiên từ 0 đến 9
    for pos in replacement_positions:
        char_list[pos] = str(random.randint(0, 9))
    
    # Thêm dấu '-' vào các vị trí đã chọn
    for pos in hyphen_positions:
        char_list[pos] = '-'
    
    # Tạo lại phần đầu đã được thay thế
    replaced_part = ''.join(char_list)
    
    # Tạo tên miền mới
    new_domain = replaced_part + second_part + '.' + rest
    
    return new_domain

# Đọc file data.csv
df = pd.read_csv('data.csv')

# Giả sử tên miền nằm trong cột 'domain', bạn có thể thay đổi tên cột phù hợp
df['masked_domain'] = df['domain'].apply(replace_with_random_numbers_and_hyphens)

# Chỉ giữ lại cột mới tạo
df_new = df[['masked_domain']]

# Ghi kết quả ra file truonghop2.csv
df_new.to_csv('truonghop2.csv', index=False)

print("File truonghop2.csv đã được tạo thành công!")

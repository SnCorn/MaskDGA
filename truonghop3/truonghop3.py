import pandas as pd
import random

# Hàm chèn thêm nguyên âm
def insert_vowels(domain):
    vowels = 'aeiou' # Bao gồm các nguyên âm a, e, i, o, u, y
    new_domain = ''
    for char in domain:
        new_domain += char
        if char.isalpha() and char.lower() not in vowels:
            new_domain += random.choice(vowels)
    return new_domain

# Hàm biến đổi ký tự
def transform_characters(domain):
    transformations = {'j': 'y'}  # Định nghĩa các quy tắc biến đổi, ví dụ: j -> y
    new_domain = ''
    for char in domain:
        new_domain += transformations.get(char, char)
    return new_domain

# Hàm tổng hợp hai phương pháp
def combined_transformation(domain):
    # Chia đôi domain và thực hiện biến đổi
    first_half = domain[:len(domain)//2]
    second_half = domain[len(domain)//2:]
    transformed_first_half = transform_characters(first_half)
    
    # Nếu chia đôi và biến đổi thất bại, giữ nguyên domain
    if transformed_first_half == first_half:
        return domain
    
    # Chèn thêm nguyên âm vào phần biến đổi
    transformed_first_half_with_vowels = insert_vowels(transformed_first_half)
    
    # Ghép kết quả
    return transformed_first_half_with_vowels + second_half

# Đọc file data.csv
df = pd.read_csv('data.csv')

# Áp dụng hàm combined_transformation cho cột 'domain'
df['transformed_domain'] = df['domain'].apply(combined_transformation)

# Chỉ giữ lại cột mới tạo
df_new = df[['transformed_domain']]

# Ghi kết quả ra file truonghop3.csv
df_new.to_csv('truonghop3.csv', index=False)

print("File truonghop3.csv đã được tạo thành công!")

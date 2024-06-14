import json

# Đường dẫn tới tệp tin dga_domains.txt
file_path = "dga_domains.txt"

# Khởi tạo các biến đếm
count_true = 0
count_false = 0

# Đọc nội dung từ tệp tin
with open(file_path, "r") as file:
    content = file.read()
    
    # Tách các đối tượng JSON
    json_objects = content.split("}{")
    
    # Sửa lại định dạng JSON cho các đối tượng
    json_objects[0] = json_objects[0] + "}"
    json_objects[-1] = "{" + json_objects[-1]
    for i in range(1, len(json_objects) - 1):
        json_objects[i] = "{" + json_objects[i] + "}"
    
    # Duyệt qua từng đối tượng JSON và đếm số lượng is_dga
    for obj in json_objects:
        domain_info = json.loads(obj)
        if domain_info["is_dga"]:
            count_true += 1
        else:
            count_false += 1

# Ghi kết quả vào file result.txt
with open('result.txt', 'w') as result_file:
    result_file.write("Tổng số is_dga = true: " + str(count_true) + "\n")
    result_file.write("Tổng số is_dga = false: " + str(count_false) + "\n")

print("Kết quả đã được ghi vào file result.txt")

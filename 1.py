cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
choice=0

while True:
    choice=(input('''
SHOPEE CART MANAGEMENT SYSTEM

1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình

Mời bạn chọn chức năng (1-5):  '''))
    match choice:
        case "1":
            print("--- Chi tiết giỏ hàng---")
            print(f"{"STT":<5}|{"Mã sản phẩm":<15}|{"Tên sản phẩm":<30}|{"SL":<5}|{"Đơn giá":<15}|{"Thành tiền":<15}")
            total_quantity=0
            total_price=0
            price_last=0
            for i, items in enumerate(cart_items,1):
                id,product,quantity,price=items
                total_price=quantity* price
                total_quantity+=quantity
                price_last+=total_price
                print(f"{i:<5}|{id:<15}|{product:<30}|{quantity:<5}|{price:<15}|{total_price:<15}")
            
            print(f"Tổng số lượng sản phẩm có trong giỏ: {total_quantity}")
            print(f"Tổng tiền thanh toán :{price_last:,}")
        case "2":
            input_id=input("Nhập mã sản phẩm: ")
            input_name=input("Nhập tên sản phẩm: ")
            input_quantity=input("Nhập số lượng: ").strip()
            input_price=input("Nhập đơn giá: ").strip()

            nice_id=input_id.strip().upper()
            nice_name=input_name.strip().title()
            nice_quantity=int(input_quantity)
            nice_price=float(input_price)
            found=False
            for i in cart_items:
                if nice_id == i[0]:
                    i[2]+=nice_quantity
                    print(f"Đã cộng thêm {nice_name}, {i}")
                    found=True
                    break
            if not found:
                new_item=[nice_id,nice_name,nice_quantity,nice_price]
                cart_items.append(new_item)
                print(f"Đã thêm {nice_name} vào shop")
        case "3":
            found=False
            fix_id=input("Nhập mã sản phẩm cần sửa: ")
            fix_quantity=input("Nhập số lượng cần sửa:").strip()
            nice_id=fix_id.strip()
            nice_quantity=int(fix_quantity)
            
            for i in cart_items:
                if nice_quantity > i[2]:
                    print("Số sản phẩm không thể âm")
                    break
                if nice_id == i[0]:
                    i[2]=nice_quantity
                    found=True
                    print(f"Đã cập nhật {nice_id}")
            if not found:
                print("Không tìm thấy sản phẩm có mã:",nice_id )
        case "4":
            found=False
            del_id=input("Nhập id cần xóa: ").strip()
            for i in cart_items:
                if del_id == i[0]:
                    cart_items.remove(i)
                    print(f" Đã xóa hoàn toàn sản phẩm {del_id} khỏi giỏ hàng.")
                    found = True
                    break
            if not found:
                print(" Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "5":
            print("Bai bai")
            break
        case _:
            print("Nhập sai yêu cầu(Phải nhập từ 1->5)")
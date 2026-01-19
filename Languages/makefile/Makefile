TARGET_DIR := $(CURDIR)
# 2. Kiểm tra thư viện Python
check-py-libs:
	@echo "--- Đang kiểm tra thư viện Python trên máy $(USER) ---"
	@if command -v pip3 >/dev/null 2>&1; then \
		COUNT=$$(pip3 list | tail -n +3 | wc -l); \
		echo "[ INFO ] Tổng số thư viện đã cài: $$COUNT"; \
		echo "Dưới đây là 10 thư viện đầu tiên trong danh sách:"; \
		pip3 list | sed -n '3,12p'; \
	else \
		echo "[ FAIL ] Chưa cài pip3."; \
	fi
.PHONY: gen-req

# Target: Quét thư mục hiện tại và tạo file requirements.txt
gen-req:
	@echo "--- Đang quét các thư viện thực tế được import trong $(TARGET_DIR) ---"
	@if command -v pipreqs >/dev/null 2>&1; then \
		pipreqs $(TARGET_DIR) --force; \
		echo "[ OK ] Đã tạo/cập nhật file requirements.txt thành công."; \
		echo "Nội dung file:"; \
		cat requirements.txt; \
	else \
		echo "[ FAIL ] Chưa cài pipreqs. Đang tiến hành cài đặt..."; \
		pip install pipreqs && pipreqs $(TARGET_DIR) --force; \
	fi

# Tìm nhanh một thư viện cụ thể (Ví dụ: make find-lib name=torch)
find-lib:
	@pip3 list | grep -i "$(name)" || echo "Không tìm thấy thư viện: $(name)"

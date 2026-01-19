SRC_DIR=src/main/java/com/mycompany/app

all:
	@mvn -q compile exec:java -Dexec.mainClass="com.mycompany.app.App"
debug:
	@mvn -q compile
	@java -cp target/classes com.mycompany.app.App
create:
	@printf "package com.mycompany.app;\n\npublic class $(name) {\n    public void Hello() {\n        System.out.println(\"Hello from $(name)!\");\n    }\n}\n" > $(SRC_DIR)/$(name).java
	@echo "Đã tạo thành công: $(SRC_DIR)/$(name).java"
run: all

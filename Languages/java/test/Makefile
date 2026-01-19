all:
	@mvn -q compile exec:java -Dexec.mainClass="com.mycompany.app.App"
debug:
	@mvn -q compile
	@java -cp target/classes com.mycompany.app.App
run: all

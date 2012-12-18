
JAVA = java
CLOSURE_COMPILER_JAR=../../../closure-compiler/compiler.jar
LOCAL_URL = http://localhost:8000/static/
PRODUCTION_URL = http://static.morseless.me.uk/

js_files = unmorse.js

all: $(js_files:.js=.min.js)

clean:
	rm -f $(js_files:.js=.min.js)

%.js: %.local.js
	sed s,$(LOCAL_URL),$(PRODUCTION_URL), $< > $@

%.min.js: %.js $(CLOSURE_COMPILER_JAR)
	$(JAVA) -jar $(CLOSURE_COMPILER_JAR) --js $< --js_output_file $@
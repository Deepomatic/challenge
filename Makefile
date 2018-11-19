MAKEFILE_ROOT = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
CPP_ROOT = $(MAKEFILE_ROOT)/cpp/build
USE_CPP = $(shell cd $(MAKEFILE_ROOT) && python -c "import sys; import config; print(int(config.use_cpp_implementation))")

all: build
	python main.py

test: build
	python test.py

build:
	@if [ "$(USE_CPP)" = "1" ]; then\
		echo "Using CPP implementation";\
		mkdir -p $(CPP_ROOT);\
		cd $(CPP_ROOT) && cmake .. && make;\
	else\
		echo "Using Python implementation";\
	fi

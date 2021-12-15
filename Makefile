all: cpuid_pb2.py

cpuid_pb2.py: cpuid.proto
	protoc -I=. --python_out=. cpuid.proto

clean:
	rm -f *pyc

realclean: clean
	rm -f cpuid_pb2.py



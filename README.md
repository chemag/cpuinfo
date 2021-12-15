# cpuinfo

A `/proc/cpuinfo` parser for ARM devices. Will translate the ARM information (CPU implementer, part, revision, and variant) from ID to a string.



# 1. Introduction

ARM devices have a base register (CPUID) that includes information about each processor core. CPUID is a 32-bit register with the following structure:

```
   3                   2                   1                   0
 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  implementer  |variant|  0xf  |           part          | rev |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Where:
* implementer: implementer id
* variant: procesor revision (ordinal)
* part: part number
* rev: revision (path release)

The part field is defined by each implementer.

Some databases containing information about the implementer and part IDs are:
* [util-linux](https://github.com/util-linux/util-linux/) [lscpu-arm.c](https://github.com/util-linux/util-linux/blob/master/sys-utils/lscpu-arm.c)
* llvm [Host.cpp](https://llvm.org/doxygen/Host_8cpp_source.html)


# 2. Operation




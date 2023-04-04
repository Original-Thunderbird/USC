# CSCI402
Public sharing of ANY course content is regulated. contact dafu690127@gmail.com for materials.
## CSCI402.1 Doubly-linked Circular List

## CSCI402.2 Multi-server query processing simulation
Simulate a traffic shaper that transmits/services packets controlled by a token bucket filter using multi-threading within a single process. Use an extra thread to handle SIGINT. Gather a series of statistics during the simulation.

This serves as a advanced version of [UoM-COMP28112.3](https://github.com/Original-Thunderbird/UoM/tree/master/yr2/COMP28112%20Distributed%20Computing/ex3)

### 1. Getting Started
compile
```
make warmup2
```

cmdline syntax to run
```
warmup2 [-lambda lambda] [-mu mu] [-r r] [-B B] [-P P] [-n num] [-t tsfile]
```

### 2. Technologies
C, gdb


## CSCI402.proj Operating System
Implement core parts of OS kernel so it eventually can run simple user-space processes.

The project consists of 3 major parts:

#### Threads and Processes
Mutex, thread management, process management, scheduler, kernel startup
#### Virtual File System
Device creation & I/O, pathname resolution, VFS system call, open file
#### Virtual Memory
Page frame management, page fault handling, read/write system call, virtual memory mapper, shadow object

### 1. Getting Started
A ubuntu **16.04** environment is required.

compile and run
```
make clean
make
./weenix -n
```


### 2. Technologies
C, gdb
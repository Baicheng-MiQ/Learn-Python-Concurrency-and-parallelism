# Speed Up Your Python Program With Concurrency

From [Real Python](https://realpython.com/python-concurrency/)

## Overview

Only `multiprocessing` actually runs at literally the same time. 
 
`Threading` and `asyncio` both run on a single processor and therefore only run one at a time. 
### Multiprocessing
- Uses more cores
- Creates new **process**
- each process runs in its own Python Interpreter

### Threading
- **Pre-emptive** multitasking
- the _operating system_ interrupts it at any time to start running a different thread.
- handy in that the code in the thread doesn't need to do anything to make the switch

### Asyncio
- **Cooperative** multitasking
- the task must announce when they are ready to be switched out.
- will not be swapped out in the middle of a Python statement unless that statement is marked.

| **Concurrency Type**                 | **Switching Decision**                                                | **Number of Processors** |
|--------------------------------------|-----------------------------------------------------------------------|--------------------------|
| Pre-emptive multitasking (threading) | The operating system decides when to switch tasks external to Python. | 1                        |
| Cooperative multitasking (asyncio)   | The tasks decide when to give up control.                             | 1                        |
| Multiprocessing (multiprocessing)    | The processes all run at the same time on different processors.       | Many                     |



## When Is Concurrency Useful?
Two problems
1. CPU-bound
2. IO-bound: (external resource)

| I/O-Bound Process                                                       | CPU-Bound Process                                                                 |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| spends most of its time talking to a slow device                        | spends most of its time doing CPU operations.                                     |
| Speeding up: **overlapping** the times spent waiting for these devices. | Speeding up: finding ways to do **more computations** in the same amount of time. |
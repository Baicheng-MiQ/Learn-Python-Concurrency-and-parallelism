# Speed Up Your Python Program With Concurrency
Why I'm learning this:
- Facing efficiency issue calling third party API when I'm building back-end of the PS editor project.

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


# Synchronous 
See [synchronous method](synchronous_method.py)
- It is slow.

## With Threading 
See [threading method](threading_method.py)
![How threading works](https://files.realpython.com/media/Threading.3eef48da829e.png)

## With asyncio 
- It is simplified. 
- Each task takes far fewer resources and less time to create than a thread
### Event loop
Maintains a minimum of two lists containing two **states**
- **Ready state**: task has work, ready to run.
- **Waiting state**: waiting for some external thing to finish.

1. It selects **ready** tasks and starts it,
2. Then that task is in complete control until it cooperatively hands the control back to the event loop.
3. the event loop then places that task into either the ready or waiting list 
4. and then goes through each of the tasks in the waiting list to see if it has become ready by an I/O operation completing. 
5. Once all the tasks have been sorted into the right list again, the event loop picks the next task to run, and the process repeats. 

### `async` and `await`
- `await` as the magic that allows the task to hand control back to the event loop.
- `async` as a flag to Python telling it that the function about to be defined with await.
- **OR** flag this context manager as something that can get swapped out.

### Code
```pip install aiohttp```

See [asyncio method](asyncio_method.py)

![How asyncio works](https://files.realpython.com/media/Asyncio.31182d3731cf.png)

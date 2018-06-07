# Multithreading-in-Python
This repo will include multithreading snippets written in python and some small projects. 

Python has several modules for Multithreading, which includes thread, threading and queue modules.
1. Thread Module: For basic thread and locking support
2. Threading Module: For higher level fully featured thread management
3. Queue Module: for creating Queue data structure that can be shared across multiple threads.

Note: Why to avoid using Thread module over Threading module?
With thread module, there is no control of when process exits. When the main thread finishes any other thread will also die, 
without warning or proper cleanup. Whereas Threading module supports daemonic threads. A daemon is typically a server that waits for 
client requests to service. If there is no client work to be done, the daemon sits idle.
     

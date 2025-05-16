# x64dbg Command Reference for LLM Consumption

This reference provides information about commands available in x64dbg, formatted for easy consumption by Large Language Models.

## Operating System Control

### Command: DisablePrivilege

**Description**: Revoke the privilege.

**Syntax**: `DisablePrivilege arg1`

**Arguments**:

- `arg1`: The name of the privilege. Example: The name of the privilege. Example: `SeDebugPrivilege`

**Response**: None

### Command: EnablePrivilege

**Description**: Permit the privilege.

**Syntax**: `EnablePrivilege arg1`

**Arguments**:

- `arg1`: The name of the privilege. Example: The name of the privilege. Example: `SeDebugPrivilege`

**Response**: None

### Command: GetPrivilegeState

**Description**: Query whether the privilege is enabled on the debuggee.

**Syntax**: `GetPrivilegeState arg1`

**Arguments**:

- `arg1`: The name of the privilege. Example: The name of the privilege. Example: `SeDebugPrivilege`.

**Response**: None

### Command: handleclose

**Description**: Close a remote handle so that its system resources can be released.

**Syntax**: `handleclose arg1`

**Arguments**:

- `arg1`: The handle value of the handle, in the context of the debuggee.

**Response**: None

## Memory Operations

### Command: alloc

**Description**: Allocate memory in the debuggee (using VirtualAllocEx). The memory is allocated with PAGE_EXECUTE_READWRITE protection.

**Syntax**: `alloc [arg1] [arg2]`

**Arguments**:

- `[arg1]`: Size of the memory to allocate. When not specified, a default size of 0x1000 is used.
- `[arg2]`: Address to allocate the memory at. Unspecified or zero means a random address.

**Response**: This command sets $result to the allocated memory address. It also sets the $lastalloc variable to the allocated memory address when VirtualAllocEx succeeded.

### Command: Fill

**Description**: Set memory of the debuggee to a specified byte.

**Syntax**: `Fill arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: Memory address to start setting bytes.
- `arg2`: Value (byte) to set memory with.
- `[arg3]`: Size to set. When not specified the rest of the page is used.

**Response**: This command does not set any result variables.

### Command: memcpy

**Description**: Copy memory in the context of the debuggee, without applying patches.

**Syntax**: `memcpy arg1 arg2 arg3`

**Arguments**:

- `arg1`: Destination address. Destination address.
- `arg2`: Source address. Source address.
- `arg3`: Size to copy.

**Response**: This command sets `$result` to the total amount of bytes written at the destination. The condition `$result==arg3` is true if all memory was copied.

### Command: free

**Description**: Free memory in the debuggee (using VirtualFreeEx).

**Syntax**: `free [arg1]`

**Arguments**:

- `[arg1]`: Address of the memory to free. When not specified, the value at $lastalloc is used.

**Response**: This command sets $result to 1 if VirtualFreeEx succeeded, otherwise it’s set to 0. $lastalloc is set to zero when the address specified is equal to $lastalloc.

### Command: getpagerights

**Description**: Get the rights of a memory page.

**Syntax**: `getpagerights arg1`

**Arguments**:

- `arg1`: Memory Address of page (it fix the address if this arg is not the top address of a page).

**Response**: This command does not set any result variables.

### Command: setpagerights

**Description**: Change the rights of a memory page.

**Syntax**: `setpagerights arg1 arg2`

**Arguments**:

- `arg1`: Memory Address of page (it fix the address if this arg is not the top address of a page).
- `arg2`: New Rights, this can be one of the following values: “Execute”, “ExecuteRead”, “ExecuteReadWrite”, “ExecuteWriteCopy”, “NoAccess”, “ReadOnly”, “ReadWrite”, “WriteCopy”. You can add a G at first for add PAGE GUARD. example: “GReadOnly”. Read the MSDN for more info.

**Response**: This command does not set any result variables.

### Command: savedata

**Description**: Save a memory region to disk.

**Syntax**: `savedata arg1 arg2 arg3`

**Arguments**:

- `arg1`: The filename. If you use The filename. If you use `:memdump:` as name it will save a file as `memdump_pid_addr_size.bin` in the x64dbg directory. You can use String Formatting here.
- `arg2`: The address of the memory region.
- `arg3`: The size of the memory region.

**Response**: None

### Command: minidump

**Description**: Create aminidumpwith full memory and handle information from the debuggee.

**Syntax**: `minidump arg1`

**Arguments**:

- `arg1`: The filename of the The filename of the `.dmp`.

**Response**: None

## Thread Control

### Command: createthread[,threadcreate,newthread,threadnew]

**Description**: Create a new thread at the specified entry.

**Syntax**: `createthread[,threadcreate,newthread,threadnew] arg1 [arg2]`

**Arguments**:

- `arg1`: The entry of the new thread.
- `[arg2]`: The argument of the new thread. If the argument is not specified, the default argument is 0.

**Response**: None

### Command: switchthread

**Description**: Switch the internal current thread to another thread (resulting in different callstack + different registers displayed).

**Syntax**: `switchthread [arg1]`

**Arguments**:

- `[arg1]`: ThreadId of the thread to switch to (see the Threads tab). When not specified, the main thread is used.

**Response**: This command does not set any result variables.

### Command: suspendthread

**Description**: Suspend a thread in the debuggee.

**Syntax**: `suspendthread [arg1]`

**Arguments**:

- `[arg1]`: ThreadId of the thread to suspend (see the Threads tab). When not specified, the main thread is used.

**Response**: This command does not set any result variables.

### Command: resumethread

**Description**: Resume a thread in the debuggee.

**Syntax**: `resumethread [arg1]`

**Arguments**:

- `[arg1]`: ThreadId of the thread to resume (see the Threads tab). When not specified, the main thread is used.

**Response**: This command does not set any result variables.

### Command: killthread

**Description**: Kill a thread in the debuggee.

**Syntax**: `killthread [arg1] [arg2]`

**Arguments**:

- `[arg1]`: ThreadId of the thread to kill (see the Threads tab). When not specified, the main thread is used.
- `[arg2]`: Thread exit code. When not specified, 0 will be used.

**Response**: This command does not set any result variables.

### Command: suspendallthreads

**Description**: Suspend all threads in the debuggee.

**Syntax**: `suspendallthreads`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: resumeallthreads

**Description**: Resume all threads in the debuggee.

**Syntax**: `resumeallthreads`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: setthreadpriority

**Description**: Set thread priority in the debuggee.

**Syntax**: `setthreadpriority arg1 arg2`

**Arguments**:

- `arg1`: ThreadId of the thread to change the priority of (see the Threads tab).
- `arg2`: Priority value, this can be the integer of a valid thread priority (see MSDN) or one of the following values: “Normal”, “AboveNormal”, “TimeCritical”, “Idle”, “BelowNormal”, “Highest”, “Lowest”.

**Response**: This command does not set any result variables.

### Command: setthreadname

**Description**: Set thread name (only for the debugger, nothing changes in the debuggee).

**Syntax**: `setthreadname arg1 arg2`

**Arguments**:

- `arg1`: ThreadId of the thread to change the priority of (see the Threads tab).
- `arg2`: New thread name. Leave empty to remove the current name.

**Response**: This command does not set any result variables.

## Watch Control

### Command: AddWatch

**Description**: Add a watch item.

**Syntax**: `AddWatch arg1 [arg2]`

**Arguments**:

- `arg1`: The expression to watch.
- `[arg2]`: The data type of the watch item. `uint` displays hexadecimal value, `int` displays signed decimal value, `ascii` displays the ASCII string pointed by the value. `unicode` displays the Unicode string pointed by the value. `uint` is the default type..

**Response**: None

### Command: DelWatch

**Description**: Delete a watch item.

**Syntax**: `DelWatch arg1`

**Arguments**:

- `arg1`: The id of the watch item to delete.

**Response**: This command does not set any result variables.

### Command: SetWatchdog

**Description**: Set the watchdog mode of a watch item.

**Syntax**: `SetWatchdog arg1 [arg2]`

**Arguments**:

- `arg1`: The id of the watch item.
- `[arg2]`: The watchdog mode. Possible values:

**Response**: None

### Command: SetWatchExpression

**Description**: Change the expression of an existing watch item.

**Syntax**: `SetWatchExpression arg1 arg2 arg3`

**Arguments**:

- `arg1`: The id of the watch item.
- `arg2`: The new expression to watch.
- `arg3`: The new data type of the watch item.

**Response**: None

### Command: SetWatchName

**Description**: Rename a watch item.

**Syntax**: `SetWatchName arg1 arg2`

**Arguments**:

- `arg1`: The id of the watch item to rename.
- `arg2`: The new name.

**Response**: None

### Command: CheckWatchdog

**Description**: Evaluate all the watch items, trigger or reset watchdog when appropiate.

**Syntax**: `CheckWatchdog`

**Arguments**: None

**Response**: None

## Variables

### Command: var

**Description**: Declare a new variable.

**Syntax**: `var arg1 [arg2]`

**Arguments**:

- `arg1`: Variable name (will be prefixed with ‘$’ if not done).
- `[arg2]`: Initial variable value (see console input for details).

**Response**: This command does not set any result variables.

### Command: vardel

**Description**: Delete a user-defined variable.

**Syntax**: `vardel arg1`

**Arguments**:

- `arg1`: Name of the variable to delete ($ will be prepended when not present).

**Response**: This command does not set any result variables.

### Command: varlist

**Description**: Get a list of all variables and their values.

**Syntax**: `varlist [arg1]`

**Arguments**:

- `[arg1]`: Filter (USER, SYSTEM, READONLY).

**Response**: This command does not set any result variables.

## Tracing

### Command: TraceIntoConditional

**Description**: Trace the program byStepInto, until the specified condition is satisfied, or maximum number of steps reached.

**Syntax**: `TraceIntoConditional arg1 [arg2]`

**Arguments**:

- `arg1`: The condition used. When this is evaluated to be a value other than 0, tracing will stop.
- `[arg2]`: The maximum step count to trace before the debugger gives up.

**Response**: None

### Command: TraceOverConditional

**Description**: Trace the program byStepOver, until the specified condition is satisfied, or maximum number of steps reached.

**Syntax**: `TraceOverConditional arg1 [arg2]`

**Arguments**:

- `arg1`: The condition used. When this is evaluated to be a value other than 0, tracing will stop.
- `[arg2]`: The maximum step count to trace before the debugger gives up.

**Response**: None

### Command: TraceIntoBeyondTraceCoverage

**Description**: PerformStepIntountil the program reaches somewhere outside the trace coverage. This is similar toticndtr.hitcount(cip)==0&&arg1,arg2except that it achieves higher performance by avoiding the expression function invocation.

**Syntax**: `TraceIntoBeyondTraceCoverage [arg1] [arg2]`

**Arguments**:

- `[arg1]`: The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
- `[arg2]`: The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

**Response**: This command does not set any result variables.

### Command: TraceOverBeyondTraceCoverage,TraceOverBeyondTraceRecord

**Description**: Perform StepOver until the program reaches somewhere outside the trace coverage.

**Syntax**: `TraceOverBeyondTraceCoverage,TraceOverBeyondTraceRecord [arg1] [arg2]`

**Arguments**:

- `[arg1]`: The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
- `[arg2]`: The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

**Response**: This command does not set any result variables.

### Command: TraceIntoIntoTraceCoverage

**Description**: Perform StepInto until the program reaches somewhere inside the trace coverage.

**Syntax**: `TraceIntoIntoTraceCoverage [arg1] [arg2]`

**Arguments**:

- `[arg1]`: The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
- `[arg2]`: The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

**Response**: This command does not set any result variables.

### Command: TraceOverIntoTraceCoverage

**Description**: Perform StepOver until the program reaches somewhere inside the trace coverage.

**Syntax**: `TraceOverIntoTraceCoverage [arg1] [arg2]`

**Arguments**:

- `[arg1]`: The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
- `[arg2]`: The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

**Response**: This command does not set any result variables.

### Command: RunToParty

**Description**: Run the program until the program reaches somewhere belonging to the party number. This works by putting temporary memory breakpoints on all memory pages with matching party number.

**Syntax**: `RunToParty arg1`

**Arguments**:

- `arg1`: The party number. This value cannot be an expression. Note: The party number. Note: `0` is user module, `1` is system module..

**Response**: None

### Command: RunToUserCode

**Description**: Run until user code is reached. It is equivallent toRunToParty0.

**Syntax**: `RunToUserCode`

**Arguments**: None

**Response**: None

### Command: TraceSetLog

**Description**: Change the trace log text and condition during tracing. SeeConditional Tracingfor more information.

**Syntax**: `TraceSetLog [arg1] [arg2]`

**Arguments**:

- `[arg1]`: Log text. If not specified the current text/condition is cleared.
- `[arg2]`: Log condition. If not specified the default condition is used.

**Response**: None

### Command: TraceSetCommand

**Description**: Change the trace command text and condition during tracing. SeeConditional Tracingfor more information.

**Syntax**: `TraceSetCommand [arg1] [arg2]`

**Arguments**:

- `[arg1]`: Command text. If not specified the current text/condition is cleared.
- `[arg2]`: Command condition. If not specified the default condition is used.

**Response**: None

### Command: TraceSetLogFile

**Description**: Redirect the trace log to a file.

**Syntax**: `TraceSetLogFile arg1`

**Arguments**:

- `arg1`: File name to redirect the trace log to. This file will be cleared and overwritten when the trace starts. This does nothing if you don’t set the log text!

**Response**: None

### Command: StartTraceRecording

**Description**: Start recording a trace to the specified file. The file will also be opened in the trace view. Note you need to useTraceIntoConditionalor other command to actually trace the program and record instructions.

**Syntax**: `StartTraceRecording arg1`

**Arguments**:

- `arg1`: The file name. Default file extension “trace32” or “trace64” is not added automatically.

**Response**: This command does not set any result variables.

### Command: StopTraceRecording

**Description**: Stops trace recording and closes the file.

**Syntax**: `StopTraceRecording`

**Arguments**: None

**Response**: This command does not set any result variables.

## Searching

### Command: find

**Description**: Find a pattern in a memory page. If you want to find all occurrences of a pattern in a memory page usefindall.

**Syntax**: `find arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first. If you want to find all occurrences of a pattern in the entire memory map use The address to start searching from. If you want to find all occurrences of a pattern in the entire memory map use findallmem..
- `arg2`: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`. You can use String Formatting here.
- `[arg3]`: The size of the data to search in. Default is the size of the memory region.

**Response**: The `$result` variable is set to the virtual address of the address that matches the byte pattern. `$result` will be 0 when the pattern could not be matched.

### Command: findall

**Description**: Find all occurrences of a pattern in a memory page.

**Syntax**: `findall arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first. You can use The address to start searching from. You can use findallmem to search for a pattern in the whole memory..
- `arg2`: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`. You can use String Formatting here.
- `[arg3]`: The size of the data to search in. Default is the size of the memory region.

**Response**: `$result` is set to the number of occurrences.

### Command: findallmem

**Description**: Find all occurrences of a pattern in the entire memory map.

**Syntax**: `findallmem arg1 arg2 [arg3] [arg4]`

**Arguments**:

- `arg1`: The address to start searching from.
- `arg2`: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`. You can use String Formatting here.
- `[arg3]`: The size of the data to search in. Default is the entire memory map ( The size of the data to search in. Default is the entire memory map ( `-1`).
- `[arg4]`: Set to Set to `user`/ `system`/ `module` to only include (user/system) modules in the search.

**Response**: `$result` is set to the number of occurrences.

### Command: findasm

**Description**: Find assembled instruction.

**Syntax**: `findasm arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: Instruction to look for (make sure to use quoted “mov eax, ebx” to ensure you actually search for that instruction). You can use Instruction to look for (make sure to use quoted “mov eax, ebx” to ensure you actually search for that instruction). You can use String Formatting here.
- `[arg2]`: Address of/inside a memory page to look in. When not specified CIP will be used.
- `[arg3]`: The size of the data to search in. Default is the size of the memory region.

**Response**: The `$result` variable is set to the number of references found.

### Command: findguid

**Description**: Find references to GUID. The referenced GUID must be registered in the system, otherwise it will not be found.

**Syntax**: `findguid [arg1] [arg2] [arg3]`

**Arguments**:

- `[arg1]`: The base of the memory range. If not specified, The base of the memory range. If not specified, `RIP` or `EIP` will be used.
- `[arg2]`: The size of the memory range.
- `[arg3]`: The region to search. `0` is current region (specified with arg1 and arg2). `1` is current module (the module specified with arg1). `2` is all modules..

**Response**: None

### Command: reffind

**Description**: Find references to a certain value.

**Syntax**: `reffind arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: The value to look for.
- `[arg2]`: Address of/inside a memory page to look in. When not specified CIP will be used.
- `[arg3]`: The size of the data to search in.

**Response**: The `$result` variable is set to the number of references found.

### Command: reffindrange

**Description**: Find references to a certain range of values.

**Syntax**: `reffindrange arg1 [arg2] [arg3] [arg4]`

**Arguments**:

- `arg1`: Start of the range (will be included in the results when found).
- `[arg2]`: End of range (will be included in the results when found). When not specified the first argument will be used.
- `[arg3]`: Address of/inside a memory page to look in. When not specified CIP will be used.
- `[arg4]`: The size of the data to search in.

**Response**: The `$result` variable is set to the number of references found.

### Command: refstr

**Description**: Find referenced text strings.

**Syntax**: `refstr [arg1] [arg2]`

**Arguments**:

- `[arg1]`: Address of/inside a memory page to find referenced text strings in. When not specified CIP will be used.
- `[arg2]`: The size of the data to search in.

**Response**: The `$result` variable is set to the number of string references found.

### Command: modcallfind

**Description**: Find all inter-modular calls.

**Syntax**: `modcallfind [arg1] [arg2]`

**Arguments**:

- `[arg1]`: Address of/inside a memory page to find inter-modular calls in. When not specified EIP/RIP will be used.
- `[arg2]`: The size of the data to search in.

**Response**: The `$result` variable is set to the number of inter-modular calls found.

### Command: setmaxfindresult

**Description**: Set the maximum number of occurences found.

**Syntax**: `setmaxfindresult arg1`

**Arguments**:

- `arg1`: The maximum number of occurences. The default value is 5000.

**Response**: None

## Debug Control

### Command: InitDebug

**Description**: Initializes the debugger. This command will load the executable (do some basic checks), set breakpoints on TLS callbacks (if present), set a breakpoint at the process entry point and break at the system breakpoint before giving back control to the user.

**Syntax**: `InitDebug arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: Path to the executable file to debug. If no full path is given, the Path to the executable file to debug. If no full path is given, the `GetCurrentDirectory` API will be called to retrieve a full path. Use quotation marks to include spaces in your path.
- `[arg2]`: Commandline to create the process with.
- `[arg3]`: Current folder (passed to the Current folder (passed to the `CreateProcess` API) (this is also sometimes called ‘working directory’ or ‘current directory’)

**Response**: This command will give control back to the user after the system breakpoint is reached. It will set `$pid` and `$hp`/`$hProcess` variables.

### Command: StopDebug

**Description**: Terminate the current debuggee and stop debugging it.

**Syntax**: `StopDebug`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: AttachDebugger

**Description**: Attach the debugger to a running process.

**Syntax**: `AttachDebugger arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: Process Identifier (PID) of the running process.
- `[arg2]`: Handle to an Event Object to signal (this is for internal use only).
- `[arg3]`: Thread Identifier (TID) of the thread to resume after attaching (this is for internal use only).

**Response**: This command will give control back to the user after the system breakpoint is reached. It will set `$pid` and `$hp`/`$hProcess` variables.

### Command: DetachDebugger

**Description**: Detach the debugger from the currently-debugged process.

**Syntax**: `DetachDebugger`

**Arguments**: None

**Response**: None

### Command: run

**Description**: Free the lock and allow the program to run.

**Syntax**: `run [arg1]`

**Arguments**:

- `[arg1]`: When specified, place a single-shot breakpoint at this location before running.

**Response**: None

### Command: erun

**Description**: Free the lock and allow the program to run,passing all first-chance exceptions to the debuggee.

**Syntax**: `erun [arg1]`

**Arguments**:

- `[arg1]`: When specified, place a single-shot breakpoint at this location before running.

**Response**: None

### Command: serun

**Description**: Free the lock and allow the program to run,swallowing the current exception, skipping exception dispatching in the debuggee.

**Syntax**: `serun [arg1]`

**Arguments**:

- `[arg1]`: When specified, place a single-shot breakpoint at this location before running.

**Response**: None

### Command: pause

**Description**: Pause the debuggee or stop animation if animation is in progress.

**Syntax**: `pause`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: DebugContinue

**Description**: Set debugger continue status.

**Syntax**: `DebugContinue [arg1]`

**Arguments**:

- `[arg1]`: When set (to anything), the exception will be handled by the program. Otherwise the exception will be swallowed.

**Response**: This command does not set any result variables.

### Command: StepInto

**Description**: Single Step (using Trap-Flag).

**Syntax**: `StepInto [arg1]`

**Arguments**:

- `[arg1]`: The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: eStepInto

**Description**: Single Step (using Trap-Flag),passing all first-chance exceptions to the debuggee.

**Syntax**: `eStepInto [arg1]`

**Arguments**:

- `[arg1]`: The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: seStepInto

**Description**: Single Step (using Trap-Flag),swallowing the current exception, skipping exception dispatching in the debuggee.

**Syntax**: `seStepInto [arg1]`

**Arguments**:

- `[arg1]`: The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: StepOver

**Description**: Step over calls. When the instruction at EIP/RIP isn’t a call, a StepInto is performed.

**Syntax**: `StepOver`

**Arguments**: None

**Response**: None

### Command: eStepOver

**Description**: Step over calls,passing all first-chance exceptions to the debuggee. When the instruction at EIP/RIP isn’t a call, aeStepIntois performed.

**Syntax**: `eStepOver [arg1]`

**Arguments**:

- `[arg1]`: The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: seStepOver

**Description**: Step over calls,swallowing the current exception, skipping exception dispatching in the debuggee. When the instruction at EIP/RIP isn’t a call, aeStepIntois performed.

**Syntax**: `seStepOver [arg1]`

**Arguments**:

- `[arg1]`: The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: StepOut

**Description**: Return from function by calling StepOver until the current instruction is a RET.

**Syntax**: `StepOut [arg1]`

**Arguments**:

- `[arg1]`: The number of times to step out. If not specified The number of times to step out. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: eStepOut

**Description**: Return from function by calling eStepOver until the current instruction is a RET. This commandpasses all first-chance exceptions to the debuggee.

**Syntax**: `eStepOut [arg1]`

**Arguments**:

- `[arg1]`: The number of times to step out. If not specified The number of times to step out. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: skip

**Description**: Skip the next instruction. This command swallows the current exception (if present). Useful if you want to continue after an INT3 command.

**Syntax**: `skip [arg1]`

**Arguments**:

- `[arg1]`: The number of instructions to skip. If not specified The number of instructions to skip. If not specified `1` is used.

**Response**: This command does not set any result variables.

### Command: InstrUndo

**Description**: Undo last instruction stepped. This command is only valid if some instructions are stepped in. Stepping over, running or tracing will clear the history context.

**Syntax**: `InstrUndo`

**Arguments**: None

**Response**: None

### Command: StepUser

**Description**: Step into until reaching a user module.

**Syntax**: `StepUser`

**Arguments**: None

**Response**: None

### Command: StepSystem

**Description**: Step into until reaching a system module.

**Syntax**: `StepSystem`

**Arguments**: None

**Response**: None

## Plugins

### Command: StartScylla

**Description**: Start the Scylla plugin auto-selecting the currently debugged DLL/EXE and EIP/RIP as entry point.

**Syntax**: `StartScylla`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: plugload

**Description**: Load a plugin.

**Syntax**: `plugload arg1`

**Arguments**:

- `arg1`: Name of the plugin.

**Response**: This command does not set any result variables.

### Command: plugunload

**Description**: Unload a plugin.

**Syntax**: `plugunload arg1`

**Arguments**:

- `arg1`: Name of the plugin.

**Response**: This command does not set any result variables.

## Breakpoint Control

### Command: SetBPX

**Description**: Set an INT3 (SHORT/LONG) or UD2 breakpoint and optionally assign a name to it.

**Syntax**: `SetBPX arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: Address to put a breakpoint on. This can be an API name.
- `[arg2]`: Name of the breakpoint, use quotation marks to include spaces. This name can be used by the EnableBPX, DisableBPX and DeleteBPX functions as alias, but is mainly intended to provide a single line of information about the currently-hit breakpoint. When arg2 equals to a valid type (arg3) the type is used and arg2 is ignored.
- `[arg3]`: Breakpoint type. Can be one of the following options in random order: “ss” (single shot breakpoint), “long” (CD03), “ud2” (0F0B) and “short” (CC). You can combine the “ss” option with one of the type options in one string. Example: “SetBPX 00401000,”entrypoint”,ssud2” will set a single shot UD2 breakpoint at 00401000 with the name “entrypoint”. When specifying no type or just the type “ss” the default type will be used. Per default this equals to the “short” type. You can change the default type using the “SetBPXOptions” command.

**Response**: This command does not any result variables.

### Command: DeleteBPX

**Description**: Delete a breakpoint set using the SetBPX command.

**Syntax**: `DeleteBPX [arg1]`

**Arguments**:

- `[arg1]`: Name or address of the breakpoint to delete. If this argument is not specified, all breakpoints will be deleted.

**Response**: This command does not set any result variables.

### Command: EnableBPX

**Description**: Enable a breakpoint set using the SetBPX command.

**Syntax**: `EnableBPX [arg1]`

**Arguments**:

- `[arg1]`: Name or address of the breakpoint to enable. If this argument is not specified, all breakpoints will be enabled.

**Response**: This command does not set any result variables.

### Command: DisableBPX

**Description**: Disable a breakpoint set using the SetBPX command.

**Syntax**: `DisableBPX [arg1]`

**Arguments**:

- `[arg1]`: Name or address of the breakpoint to disable. If this argument is not specified, all breakpoints will be disabled.

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpoint

**Description**: Set a hardware breakpoint (using debug registers).

**Syntax**: `SetHardwareBreakpoint arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: Address of the hardware breakpoint.
- `[arg2]`: Hardware breakpoint type. Can be either ‘r’ (readwrite), ‘w’ (write) or ‘x’ (execute). When not specified, ‘x’ is assumed.
- `[arg3]`: Hardware breakpoint size. Can be either ‘1’, ‘2’, ‘4’ or ‘8’ (x64 only). Per default, ‘1’ is assumed. The address you’re putting the hardware breakpoint on must be aligned to the specified size.

**Response**: This command does not set any result variables.

### Command: DeleteHardwareBreakpoint

**Description**: Delete a hardware breakpoint set using the SetHardwareBreakpoint command.

**Syntax**: `DeleteHardwareBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: Name or address of the hardware breakpoint to delete. If this argument is not specified, all hardware breakpoints will be deleted.

**Response**: This command does not set any result variables.

### Command: EnableHardwareBreakpoint

**Description**: Enable a previously disabled hardware breakpoint.

**Syntax**: `EnableHardwareBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: Address of the hardware breakpoint to enable. If this argument is not specified, as many as possible hardware breakpoints will be enabled.

**Response**: This command does not set any result variables.

### Command: DisableHardwareBreakpoint

**Description**: Disable a hardware breakpoint.

**Syntax**: `DisableHardwareBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: Address of the hardware breakpoint to disable. If this argument is not specified, all hardware breakpoints will be disabled.

**Response**: This command does not set any result variables.

### Command: SetMemoryBPX

**Description**: Set a memory breakpoint (GUARD_PAGE) on the whole memory region the provided address is in.

**Syntax**: `SetMemoryBPX arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: Address of or inside a memory region that will be watched.
- `[arg2]`: 1/0 restore the memory breakpoint once it’s hit? When this value is not equal to ‘1’ or ‘0’, it’s assumed to be arg3. This means “bpm eax,r” would be the same command as: “bpm eax,0,r”.
- `[arg3]`: Breakpoint type, it can be ‘a’ (read+write+execute) ‘r’ (read), ’w’ (write) or ‘x’ (execute). Per default, it’s ‘a’ (read+write+execute)

**Response**: This command does not set any result variables.

### Command: SetMemoryRangeBPX

**Description**: Set a memory breakpoint (GUARD_PAGE) on a specific memory range.

**Syntax**: `SetMemoryRangeBPX`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: DeleteMemoryBPX

**Description**: Delete a memory breakpoint set using the SetMemoryBPX command.

**Syntax**: `DeleteMemoryBPX [arg1]`

**Arguments**:

- `[arg1]`: Name or (base) address of the memory breakpoint to delete. If this argument is not specified, all memory breakpoints will be deleted.

**Response**: This command does not set any result variables.

### Command: EnableMemoryBreakpoint

**Description**: Enable a previously disabled memory breakpoint.

**Syntax**: `EnableMemoryBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: Address of the memory breakpoint to enable. If this argument is not specified, all memory breakpoints will be enabled.

**Response**: This command does not set any result variables.

### Command: DisableMemoryBreakpoint

**Description**: Disable a memory breakpoint.

**Syntax**: `DisableMemoryBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: Address of the memory breakpoint to disable. If this argument is not specified, all memory breakpoints will be disabled.

**Response**: This command does not set any result variables.

### Command: LibrarianSetBreakpoint

**Description**: Set a singleshoot breakpoint on DLL load/unload.

**Syntax**: `LibrarianSetBreakpoint arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: DLL Name to break on.
- `[arg2]`: `a` means on load and unload, `l` means on load, `u` means on unload. When not specified, x64dbg will break on both load and unload.
- `[arg3]`: When specified, the breakpoint will be singleshoot. When not specified the breakpoint will not be removed after it has been hit.

**Response**: This command does not set any result variables.

### Command: LibrarianRemoveBreakpoint

**Description**: Remove a DLL breakpoint.

**Syntax**: `LibrarianRemoveBreakpoint arg1`

**Arguments**:

- `arg1`: DLL Name to remove the breakpoint from.

**Response**: This command does not set any result variables.

### Command: LibrarianEnableBreakpoint

**Description**: Enable a DLL breakpoint set using the LibrarianSetBreakpoint command.

**Syntax**: `LibrarianEnableBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: DLL Name of the DLL breakpoint to enable. If this argument is not specified, all DLL breakpoints will be enabled.

**Response**: This command does not set any result variables.

### Command: LibrarianDisableBreakpoint

**Description**: Enable a DLL breakpoint set using the LibrarianSetBreakpoint command.

**Syntax**: `LibrarianDisableBreakpoint [arg1]`

**Arguments**:

- `[arg1]`: DLL Name of the DLL breakpoint to disable. If this argument is not specified, all DLL breakpoints will be disabled.

**Response**: This command does not set any result variables.

### Command: SetExceptionBPX

**Description**: Set an exception breakpoint. If an exception breakpoint is active, all the exceptions with the same chance and code will be captured as a breakpoint event and will not be handled by the default exception handling policy.

**Syntax**: `SetExceptionBPX arg1 [arg2]`

**Arguments**:

- `arg1`: Exception name or code of the new exception breakpoint
- `[arg2]`: Chance. Set to Chance. Set to `first`/ `1` to capture first-chance exceptions, `second`/ `2` to capture second-chance exceptions, `all`/ `3` to capture all exceptions. Default value is `first`.

**Response**: This command does not any result variables.

### Command: DeleteExceptionBPX

**Description**: Delete an exception breakpoint set using the SetExceptionBPX command.

**Syntax**: `DeleteExceptionBPX [arg1]`

**Arguments**:

- `[arg1]`: Name, exception name or code of the exception breakpoint to delete. If this argument is not specified, all exception breakpoints will be deleted.

**Response**: This command does not set any result variables.

### Command: EnableExceptionBPX

**Description**: Enable an exception breakpoint set using the SetExceptionBPX command.

**Syntax**: `EnableExceptionBPX [arg1]`

**Arguments**:

- `[arg1]`: Name, exception name or code of the exception breakpoint to enable. If this argument is not specified, all exception breakpoints will be enabled.

**Response**: This command does not set any result variables.

### Command: DisableExceptionBPX

**Description**: Disable an exception breakpoint set using the SetExceptionBPX command.

**Syntax**: `DisableExceptionBPX [arg1]`

**Arguments**:

- `[arg1]`: Name, exception name or code of the exception breakpoint to enable. If this argument is not specified, all exception breakpoints will be disabled.

**Response**: This command does not set any result variables.

### Command: bpgoto

**Description**: Configure the breakpoint so that when the program reaches it, the program will be directed to a new location. It is equivallent to the following commands:

**Syntax**: `bpgoto arg1 arg2`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `arg2`: The new address to execute if the breakpoint is reached.

**Response**: None

### Command: bplist

**Description**: Get a list of breakpoints. This list includes their state (enabled/disabled), their type, their address and (optionally) their names.

**Syntax**: `bplist`

**Arguments**: None

**Response**: This command does not set any result variables. A list entry has the following format: STATE:TYPE:ADDRESS[:NAME] STATEcan be 0 or 1. 0 means disabled, 1 means enabled. Only singleshoot and ‘normal’ breakpoints can be disabled. TYPEcan be one of the following values: BP, SS, HW and GP. BP stands for a normal breakpoint (set using the SetBPX command), SS stands for SINGLESHOT, HW stands for HARDWARE and GP stand for Guard Page, the way of setting memory breakpoints. ADDRESSis the breakpoint address, given in 32 and 64 bits for the x32 and x64 debugger respectively. NAMEis the name assigned to the breakpoint.

### Command: SetBPXOptions

**Description**: Set the default type for the “SetBPX” command.

**Syntax**: `SetBPXOptions arg1`

**Arguments**:

- `arg1`: Default type. This can be “short” (CC), “long” (CD03) or “ud2” (0F0B). Type default type affects both NORMAL and SINGLESHOT breakpoints.

**Response**: This command does not set any result variables.

## General Purpose

### Command: inc

**Description**: Increase a value.

**Syntax**: `inc arg1`

**Arguments**:

- `arg1`: Destination. Destination.

**Response**: This command does not set any result variables.

### Command: dec

**Description**: Decrease a value.

**Syntax**: `dec arg1`

**Arguments**:

- `arg1`: Destination. Destination.

**Response**: This command does not set any result variables.

### Command: add

**Description**: Add two values.

**Syntax**: `add arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: sub

**Description**: Subtract two values.

**Syntax**: `sub arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: mul

**Description**: Multiply two values and store the lower part of result intoarg1.

**Syntax**: `mul arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: mulhi

**Description**: Multiply two unsigned values and store the upper part of result intoarg1.

**Syntax**: `mulhi arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: div

**Description**: Devide two values.

**Syntax**: `div arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: and

**Description**: Binary AND two values.

**Syntax**: `and arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: or

**Description**: Binary OR two values.

**Syntax**: `or arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: xor

**Description**: Binary XOR two values.

**Syntax**: `xor arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: neg

**Description**: Negate a value.

**Syntax**: `neg arg1`

**Arguments**:

- `arg1`: Destination. Destination.

**Response**: This command does not set any result variables.

### Command: not

**Description**: Binary NOT a value.

**Syntax**: `not arg1`

**Arguments**:

- `arg1`: Destination. Destination.

**Response**: This command does not set any result variables.

### Command: bswap

**Description**: Perform abswapoperation: The byte order of the destination is inverted, so the last byte becomes the first.

**Syntax**: `bswap arg1`

**Arguments**:

- `arg1`: Destination. Destination.

**Response**: This command does not set any result variables.

### Command: rol

**Description**: Binary ROL (rotate left) a value.

**Syntax**: `rol arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: ror

**Description**: Binary ROR (rotate right) a value.

**Syntax**: `ror arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: shl

**Description**: Binary SHL/SAL (signed/unsigned shift left) a value.

**Syntax**: `shl arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: shr

**Description**: Binary SHR (unsigned shift right) a value.

**Syntax**: `shr arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: sar

**Description**: Binary SAR (signed shift right) a value.

**Syntax**: `sar arg1 arg2`

**Arguments**:

- `arg1`: Destination. Destination.
- `arg2`: Source. Source.

**Response**: This command does not set any result variables.

### Command: popcnt

**Description**: Evaluate the population count of a value, that is, number of bits set to 1.

**Syntax**: `popcnt arg1`

**Arguments**:

- `arg1`: Value. Value.

**Response**: `arg1` is set to the population count. Additionaly, the internal variable `$_EZ_FLAG` is set to 1 if `arg1` is 0, and set to 0 otherwise. The internal variable `$_BS_FLAG` is set to 0.

### Command: lzcnt

**Description**: Count the number of leading zeros of a value. If the value is 0, then the result is 64 on 64-bit platform and 32 on 32-bit platform.

**Syntax**: `lzcnt arg1`

**Arguments**:

- `arg1`: Value. Value.

**Response**: `arg1` is set to the number of leading zeros. Additionaly, the internal variable `$_EZ_FLAG` is set to 1 if `arg1` is 0, and set to 0 otherwise. The internal variable `$_BS_FLAG` is set to 0.

### Command: push

**Description**: Push a value on the stack.

**Syntax**: `push arg1`

**Arguments**:

- `arg1`: The value to push on the stack.

**Response**: This command does not set any result variables.

### Command: pop

**Description**: Pop a value from the stack.

**Syntax**: `pop [arg1]`

**Arguments**:

- `[arg1]`: The destination. When not specified it will just increase CSP.

**Response**: This command does not set any result variables.

### Command: test

**Description**: Binary TEST a value.

**Syntax**: `test arg1 arg2`

**Arguments**:

- `arg1`: Value to test.
- `arg2`: Tester. Tester.

**Response**: This command sets the internal variables $_EZ_FLAG and $_BS_FLAG. $_EZ_FLAG is set to 1 when arg1 & arg2 == 0. $_BS_FLAG is always set to 0.

### Command: cmp

**Description**: This command compares two expressions. Notice that when you want to check for values being bigger or smaller, the comparison arg1>arg2 is made. If this evaluates to true, the $_BS_FLAG is set to 1, meaning the value is bigger. So you test if arg1 is bigger/smaller than arg2.

**Syntax**: `cmp arg1 arg2`

**Arguments**:

- `arg1`: First expression to compare.
- `arg2`: Second expression to compare.

**Response**: This command sets the internal variables $_EZ_FLAG and $_BS_FLAG. They are checked when a branch is performed.

### Command: mov

**Description**: Set a variable.

**Syntax**: `mov arg1 arg2`

**Arguments**:

- `arg1`: Variable name (optionally prefixed with a $) to set. When the variable does not exist, it will be created. Note that SSE registers are not supported (Instead use Variable name (optionally prefixed with a $) to set. Note that SSE registers are not supported (Instead use movdqu for SSE registers)..
- `arg2`: Value to store in the variable. If you use Value to store in the variable. If you use `#112233#` it will write the bytes `112233` in the process memory at `arg1`.

**Response**: This command does not set any result variables.

### Command: movdqu

**Description**: Read/write an XMM register. The source and destination operands can be either an XMM register, or a memory location. The value of destination operand will be set to source operand. When using a memory location, only the syntax[addr]is supported, whereaddris an expression of the memory address. Unlike other commands, the size of operands are 16 bytes. MM/YMM/ZMM registers are not supported by this command, to access YMM/ZMM registers, usevmovdqucommand.

**Syntax**: `movdqu arg1 arg2`

**Arguments**:

- `arg1`: The destination operand.
- `arg2`: The source operand.

**Response**: This command does not set any result variables.

### Command: vmovdqu

**Description**: Read/write a YMM/ZMM register. The source and destination operands can be either an YMM/ZMM register, or a memory location. The value of destination operand will be set to source operand. When using a memory location, only the syntax[addr]is supported, whereaddris an expression of the memory address. Unlike other commands, the size of operands are 32 bytes for YMM registers and 64 bytes for ZMM registers. To access ZMM registers, the computer and x64dbg version must support AVX-512. To access XMM registers, usemovdqucommand.

**Syntax**: `vmovdqu arg1 arg2`

**Arguments**:

- `arg1`: The destination operand.
- `arg2`: The source operand.

**Response**: This command does not set any result variables.

### Command: kmovd

**Description**: Thekmovd/kmovqcommands are used to access AVX-512 opmask registersK0-K7. These commands are only available when the computer and x64dbg version supports AVX-512.

**Syntax**: `kmovd arg1 arg2`

**Arguments**:

- `arg1`: The destination operand.
- `arg2`: The source operand.

**Response**: This command does not set any result variables.

## Analysis

### Command: analyse

**Description**: Do function analysis.

**Syntax**: `analyse`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: exanalyse

**Description**: Do exception directory analysis. This kind of analysis doesn’t work on 32-bit executables.

**Syntax**: `exanalyse`

**Arguments**: None

**Response**: None

### Command: cfanalyze

**Description**: Do control flow analysis in the module selected in the disassembly view.

**Syntax**: `cfanalyze`

**Arguments**: None

**Response**: None

### Command: analyse_nukem

**Description**: Do function analysis using nukem’s algorithm.

**Syntax**: `analyse_nukem`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: analxrefs

**Description**: Do xrefs analysis in the module selected in the disassembly view.

**Syntax**: `analxrefs`

**Arguments**: None

**Response**: None

### Command: analrecur

**Description**: Do single function analysis.

**Syntax**: `analrecur arg1`

**Arguments**:

- `arg1`: The base address of the function to analyze.

**Response**: None

### Command: analadv

**Description**: Do function analysis, embedded data analysis and xref analysis.

**Syntax**: `analadv`

**Arguments**: None

**Response**: None

### Command: virtualmod

**Description**: Tell the debugger to treat a memory range as a virtual module.

**Syntax**: `virtualmod arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: the user-supplied module name.
- `arg2`: the base of the memory range.
- `[arg3]`: the size of the memory range.

**Response**: This command does not set any result variables.

### Command: symdownload

**Description**: Attempt to download a symbol from a Symbol Store.

**Syntax**: `symdownload [arg1] [arg2]`

**Arguments**:

- `[arg1]`: Module name (with or without extension) to attempt to download symbols for. When not specified, an attempt will be done to download symbols for all loaded modules.
- `[arg2]`: Symbol Store URL. When not specified, the default store will be used.

**Response**: This command does not set any result variables.

### Command: symload

**Description**: Attempt to load a symbol from disk.

**Syntax**: `symload arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: Module name (with or without extension) to attempt to load symbols for.
- `arg2`: Path to the symbol file.
- `[arg3]`: Force load. Set to Force load. Set to `1` to skip symbol validation.

**Response**: This command does not set any result variables.

### Command: symunload

**Description**: Unload a symbol.

**Syntax**: `symunload arg1`

**Arguments**:

- `arg1`: Module name (with or without extension) to unload symbols from.

**Response**: This command does not set any result variables.

### Command: imageinfo

**Description**: Output the image information for a module. The information describes the Characteristics and DLL Characteristics fields in the PE header structure.

**Syntax**: `imageinfo [arg1]`

**Arguments**:

- `[arg1]`: The base of the module. If not specified the module at CIP will be used.

**Response**: None

### Command: GetRelocSize

**Description**: Get the correct size of a relocation table. This is useful while unpacking and restoring the original relocation table.

**Syntax**: `GetRelocSize arg1`

**Arguments**:

- `arg1`: The address of the relocation table to analyze.

**Response**: None

### Command: exhandlers

**Description**: Print all exception handlers, including SEH(StructuredExceptionHandler), VEH(VectoredExceptionHandler),

**Syntax**: `exhandlers`

**Arguments**: None

**Response**: None

### Command: exinfo

**Description**: Print theEXCEPTION_DEBUG_INFOstructure from the last exception.

**Syntax**: `exinfo`

**Arguments**: None

**Response**: None

### Command: traceexecute

**Description**: Tell the debugger that an address has been traced.

**Syntax**: `traceexecute arg1`

**Arguments**:

- `arg1`: The address. The address.

**Response**: This command does not set any result variables.

## User Database

### Command: dbsave

**Description**: Save a program database from memory to disk.

**Syntax**: `dbsave [arg1]`

**Arguments**:

- `[arg1]`: Path to save the database to. If not specified your current program database is used.

**Response**: This command does not set any result variables.

### Command: dbload

**Description**: Load a program database from disk in memory.

**Syntax**: `dbload [arg1]`

**Arguments**:

- `[arg1]`: Path to load the database from. If specified your current data will not be automatically cleared (import). If not specified all your data will be cleared and the current program database is reloaded from disk.

**Response**: This command does not set any result variables.

### Command: dbclear

**Description**: Clear the program database from memory (not from disk).

**Syntax**: `dbclear`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: commentset

**Description**: Set a comment.

**Syntax**: `commentset arg1 arg2`

**Arguments**:

- `arg1`: Address to set the comment at (preferably inside a module).
- `arg2`: Comment text. Comment text.

**Response**: This command does not set any result variables.

### Command: commentdel

**Description**: Delete a comment.

**Syntax**: `commentdel arg1`

**Arguments**:

- `arg1`: Address of the comment to delete.

**Response**: This command does not set any result variables.

### Command: commentlist

**Description**: List user-defined comments in reference view.

**Syntax**: `commentlist`

**Arguments**: None

**Response**: `$result` will be set to the number of user-defined comments.

### Command: commentclear

**Description**: Delete all comments in all modules.

**Syntax**: `commentclear`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: labelset

**Description**: Set a label.

**Syntax**: `labelset arg1 arg2`

**Arguments**:

- `arg1`: Address to set the label at (preferably inside a module).
- `arg2`: Label text. You can use Label text. You can use String Formatting here.

**Response**: This command does not set any result variables.

### Command: labeldel

**Description**: Delete a label.

**Syntax**: `labeldel arg1`

**Arguments**:

- `arg1`: Address of the label to delete.

**Response**: This command does not set any result variables.

### Command: labellist

**Description**: List user-defined labels in reference view.

**Syntax**: `labellist`

**Arguments**: None

**Response**: `$result` will be set to the number of user-defined labels.

### Command: labelclear

**Description**: Delete all labels in all modules.

**Syntax**: `labelclear`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: bookmarkset

**Description**: Set a bookmark.

**Syntax**: `bookmarkset arg1`

**Arguments**:

- `arg1`: Address to set the bookmark at (preferably inside a module).

**Response**: This command does not set any result variables.

### Command: bookmarkdel

**Description**: Delete a bookmark.

**Syntax**: `bookmarkdel arg1`

**Arguments**:

- `arg1`: Address of the bookmark to delete.

**Response**: This command does not set any result variables.

### Command: bookmarklist

**Description**: List user-defined bookmarks in reference view.

**Syntax**: `bookmarklist`

**Arguments**: None

**Response**: `$result` will be set to the number of user-defined bookmarks.

### Command: bookmarkclear

**Description**: Delete all bookmarks in all modules.

**Syntax**: `bookmarkclear`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: functionadd

**Description**: Add a function.

**Syntax**: `functionadd arg1 arg2`

**Arguments**:

- `arg1`: Function range start.
- `arg2`: Function range end.

**Response**: This command does not set any result variables.

### Command: functiondel

**Description**: Delete a function.

**Syntax**: `functiondel arg1`

**Arguments**:

- `arg1`: Address inside the function range to delete.

**Response**: This command does not set any result variables.

### Command: functionlist

**Description**: List user-defined functions in reference view.

**Syntax**: `functionlist`

**Arguments**: None

**Response**: `$result` will be set to the number of user-defined functions.

### Command: functionclear

**Description**: Delete all functions in all modules.

**Syntax**: `functionclear`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: argumentadd

**Description**: Add a argument.

**Syntax**: `argumentadd arg1 arg2`

**Arguments**:

- `arg1`: argument range start.
- `arg2`: argument range end.

**Response**: This command does not set any result variables.

### Command: argumentdel

**Description**: Delete a argument.

**Syntax**: `argumentdel arg1`

**Arguments**:

- `arg1`: Address inside the argument range to delete.

**Response**: This command does not set any result variables.

### Command: argumentlist

**Description**: List user-defined arguments in reference view.

**Syntax**: `argumentlist`

**Arguments**: None

**Response**: `$result` will be set to the number of user-defined arguments.

### Command: argumentclear

**Description**: Delete all arguments in all modules.

**Syntax**: `argumentclear`

**Arguments**: None

**Response**: This command does not set any result variables.

## Script Commands

### Command: call

**Description**: A call works exactly the same as an uncondentional branch, but it places it’s address on the script stack.

**Syntax**: `call arg1`

**Arguments**:

- `arg1`: The label to jump to.

**Response**: This command does not set any result variables.

### Command: invalid

**Description**: Invalid command to throw an error message. This command will halt the script execution.

**Syntax**: `invalid`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: error

**Description**: Show an error message and terminate the script.

**Syntax**: `error arg1`

**Arguments**:

- `arg1`: The error message to show.

**Response**: This command does not set any result variables.

### Command: Jxx

**Description**: There are various branches that can react on the flags set by thecmp(and maybe other) command(s):

**Syntax**: `Jxx arg1`

**Arguments**:

- `arg1`: The label to jump to.

**Response**: This command does not set any result variables.

### Command: log

**Description**: Put information in the log.

**Syntax**: `log [arg1]`

**Arguments**:

- `[arg1]`: Format string (see Format string (see String Formatting). When not specified, a newline will be logged. When using a format string it is recommended to use quotes to avoid ambiguity with the `;` (command separator): `log"{mem;8@rax}"`.

**Response**: This command does not set any result variables.

### Command: msg

**Description**: Display a message box.

**Syntax**: `msg arg1`

**Arguments**:

- `arg1`: Message box text. You can use Message box text. You can use String Formatting here.

**Response**: This command does not set any result variables.

### Command: msgyn

**Description**: Display a message box, asking the user to answer yes or no.

**Syntax**: `msgyn arg1`

**Arguments**:

- `arg1`: Message box text. You can use Message box text. You can use String Formatting here.

**Response**: The `$result` variable will be set to 1 when the user answered yes. Otherwise it’s set to 0.

### Command: pause

**Description**: Halt the script execution. The user can resume the script after this command.

**Syntax**: `pause`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: printstack[,logstack]

**Description**: Print the stack trace in the log.

**Syntax**: `printstack[,logstack]`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: ret

**Description**: When called without an entry on the stack, this command will end the script and set the script IP to the first line. When ‘call’ was executed before, ret will return from that call.

**Syntax**: `ret`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: scriptload

**Description**: Load a script file.

**Syntax**: `scriptload arg1`

**Arguments**:

- `arg1`: Script file to load.

**Response**: This command does not set any result variables.

### Command: scriptdll

**Description**: Execute a script DLL.

**Syntax**: `scriptdll arg1`

**Arguments**:

- `arg1`: The filename and path of the script DLL. If a full path is not provided x64dbg will look in the The filename and path of the script DLL. If a full path is not provided x64dbg will look in the `scripts` directory for the DLL.

**Response**: None

### Command: scriptcmd

**Description**: Execute a command in the context of a running script.

**Syntax**: `scriptcmd`

**Arguments**: None

**Response**: This command does not set any result variables.

## Miscellaneous

### Command: chd

**Description**: Change current directory (SetCurrentDirectory).

**Syntax**: `chd arg1`

**Arguments**:

- `arg1`: Path of a directory to change to.

**Response**: This command does not set any result variables.

### Command: zzz

**Description**: Halt execution for some time (equivalent of calling kernel32.Sleep).

**Syntax**: `zzz [arg1]`

**Arguments**:

- `[arg1]`: Time (in milliseconds) to sleep. If not specified this is set to 100ms (0.1 second). Keep in mind that input is in hex per default so Time (in milliseconds) to sleep. Keep in mind that input is in hex per default so `Sleep100` will actually sleep 256 milliseconds (use `Sleep.100` instead)..

**Response**: This command does not set any result variables.

### Command: HideDebugger

**Description**: Hide the debugger from (very) simple detection methods. The PEB will be modified so thatIsDebuggerPresent()will return false.

**Syntax**: `HideDebugger`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: loadlib

**Description**: Load a DLL into debugged program memory.

**Syntax**: `loadlib arg1`

**Arguments**:

- `arg1`: The name/path of the module to load.

**Response**: The `$result` variable will be set to the address of the loaded library.

### Command: asm

**Description**: Assemble an instruction.

**Syntax**: `asm arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: Address to place the assembled instruction at.
- `arg2`: Instruction text. You can use Instruction text. You can use String Formatting here.
- `[arg3]`: When specified the remainder of the previous instruction will be filled with NOPs.

**Response**: $result will be set to the assembled instruction size. 0 on failure.

### Command: gpa

**Description**: Get the address of an export inside a DLL.

**Syntax**: `gpa arg1 [arg2]`

**Arguments**:

- `arg1`: Export name. Export name.
- `[arg2]`: DLL name. DLL name.

**Response**: The $result variable is set to the export address. When the export is not found, $result will be set to 0.

### Command: setjit

**Description**: Set the Just-In-Time Debugger in Windows. In WIN64 systems there are two JIT entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash: Windows attach the x32 debugger stored in the x32-JIT entry.

**Syntax**: `setjit`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: getjit

**Description**: Get the Just-In-Time Debugger in Windows. In WIN64 systems there are two JIT entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash: Windows attach the x32 debugger stored in the x32-JIT entry.

**Syntax**: `getjit`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: getjitauto

**Description**: Get the Auto Just-In-Time Debugger FLAG in Windows. if this flag value its TRUE Windows runs the debugger without user confirmation when a process crash. In WIN64 systems there are two JIT AUTO FLAG entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash with AUTO FLAG = FALSE: Windows confirm before attach the x32 debugger stored in the x32-JIT entry.

**Syntax**: `getjitauto`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: setjitauto

**Description**: Set the Auto Just-In-Time Debugger FLAG in Windows. if this flag value its TRUE Windows runs the debugger without user confirmation when a process crash. In WIN64 systems there are two JIT AUTO FLAG entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash with AUTO FLAG = FALSE: Windows confirm before attach the x32 debugger stored in the x32-JIT entry.

**Syntax**: `setjitauto`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: getcommandline

**Description**: It gets the actual command line.

**Syntax**: `getcommandline`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: setcommandline

**Description**: It changes the command line data.

**Syntax**: `setcommandline arg1`

**Arguments**:

- `arg1`: New command line.

**Response**: This command does not set any result variables.

### Command: mnemonichelp

**Description**: Output the detailed help information about an assembly mnemonic to the log.

**Syntax**: `mnemonichelp arg1`

**Arguments**:

- `arg1`: the mnemonic name

**Response**: This command does not set any result variables.

### Command: mnemonicbrief

**Description**: Output the brief help information about an assembly mnemonic to the log.

**Syntax**: `mnemonicbrief arg1`

**Arguments**:

- `arg1`: the mnemonic name

**Response**: This command does not set any result variables.

### Command: config

**Description**: Get or set the configuration of x64dbg. It can also be used to load and store configuration specific to the script in the configuration file of x64dbg.

**Syntax**: `config arg1 arg2 [arg3]`

**Arguments**:

- `arg1`: Section name of the INI file.
- `arg2`: Key name of the INI file.
- `[arg3]`: Optional new value of the configuration. If this argument is set to a number, it will be stored in the configuration file and Optional new value of the configuration. If this argument is set to a number, it will be stored in the configuration file and `$result` is not updated. If this argument is not set, the current configuration will be read into `$result`.

**Response**: None

## GUI

### Command: disasm

**Description**: Disassemble at a certain position.

**Syntax**: `disasm [arg1]`

**Arguments**:

- `[arg1]`: The address to disassemble at. When not specified, there will be disassembled at CIP.

**Response**: This command does not set any result variables.

### Command: dump

**Description**: Dump at a certain position.

**Syntax**: `dump arg1`

**Arguments**:

- `arg1`: The address to dump at.

**Response**: This command does not set any result variables.

### Command: sdump

**Description**: Dump the stack at a certain position.

**Syntax**: `sdump [arg1]`

**Arguments**:

- `[arg1]`: The address to dump at (must be inside the thread stack range). If not specified, The address to dump at (must be inside the thread stack range). If not specified, `csp` will be used.

**Response**: This command does not set any result variables.

### Command: memmapdump

**Description**: Follow an address in the memory map.

**Syntax**: `memmapdump arg1`

**Arguments**:

- `arg1`: The address to follow.

**Response**: This command does not set any result variables.

### Command: graph

**Description**: Graph the control flow of function in the graph view.

**Syntax**: `graph [arg1]`

**Arguments**:

- `[arg1]`: The address of the function. The default value is EIP or RIP. `[arg2]` Options. If it contains “force” the graph will be reanalyzed, if it contains “silent” no messages will be printed on the console..

**Response**: None

### Command: guiupdateenable

**Description**: Enables GUI update afterguiupdatedisableis executed.

**Syntax**: `guiupdateenable [arg0]`

**Arguments**:

- `[arg0]`: If not 0, tells the debugger to update its GUI immediately.

**Response**: This command does not set any result variables.

### Command: guiupdatedisable

**Description**: Disable GUI update. This can speed up script execution.

**Syntax**: `guiupdatedisable`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: setfreezestack

**Description**: Set if the stack should be frozen.

**Syntax**: `setfreezestack arg1`

**Arguments**:

- `arg1`: ‘0’ for unfrozen, ‘1’ for frozen.

**Response**: This command does not set any result variables.

### Command: refinit

**Description**: Initialize reference view for command usage.

**Syntax**: `refinit [arg1]`

**Arguments**:

- `[arg1]`: The title of the new reference view. You can use The title of the new reference view. You can use String Formatting here.

**Response**: This command does not set any result variables.

### Command: refadd

**Description**: Add an entry to the reference view. You need to call ‘refinit’ before using refadd.

**Syntax**: `refadd arg1 arg2`

**Arguments**:

- `arg1`: Address to put in the reference view.
- `arg2`: Text to put after the address. You can use Text to put after the address. You can use String Formatting here.

**Response**: This command does not set any result variables.

### Command: refget

**Description**: Retrieve the address of a reference.

**Syntax**: `refget arg1`

**Arguments**:

- `arg1`: Zero-based index of the reference address to retrieve.

**Response**: The `$result` variable will be set to the address of the requested reference (zero on failure).

### Command: EnableLog

**Description**: Enable the log output.

**Syntax**: `EnableLog`

**Arguments**: None

**Response**: None

### Command: DisableLog

**Description**: Disable the log output. New log messages will not be appended to the log view, but they will still be saved in the log file if log redirection is enabled in the log view.

**Syntax**: `DisableLog`

**Arguments**: None

**Response**: None

### Command: ClearLog

**Description**: Clear the log window.

**Syntax**: `ClearLog`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: AddFavouriteTool

**Description**: Add a tool in the favourites menu.

**Syntax**: `AddFavouriteTool arg1 [arg2]`

**Arguments**:

- `arg1`: The path of the tool.
- `[arg2]`: The optional description of the tool. When this is set, it is displayed in the menu instead of the full path.

**Response**: None

### Command: AddFavouriteCommand

**Description**: Add a command in the favourites menu.

**Syntax**: `AddFavouriteCommand arg1 [arg2]`

**Arguments**:

- `arg1`: The command to add.
- `[arg2]`: The optional shortcut key for the command.

**Response**: None

### Command: AddFavouriteToolShortcut

**Description**: Set the shortcut key for an existing favourite tool.

**Syntax**: `AddFavouriteToolShortcut arg1 arg2`

**Arguments**:

- `arg1`: The full path of an existing favourite tool.
- `arg2`: The shortcut key for it.

**Response**: None

### Command: FoldDisassembly

**Description**: Fold the disassembly within the specified range.

**Syntax**: `FoldDisassembly arg1 arg2`

**Arguments**:

- `arg1`: The start address of the range.
- `arg2`: The length of the range.

**Response**: None

## Types

### Command: DataUnknown

**Description**: Mark data at address as Unknown.

**Syntax**: `DataUnknown arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataByte

**Description**: Mark data at address as Byte.

**Syntax**: `DataByte arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataWord

**Description**: Mark data at address as Word.

**Syntax**: `DataWord arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataDword

**Description**: Mark data at address as Dword.

**Syntax**: `DataDword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataFword

**Description**: Mark data at address as Fword.

**Syntax**: `DataFword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataQword

**Description**: Mark data at address as Qword.

**Syntax**: `DataQword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataTbyte

**Description**: Mark data at address as Tbyte.

**Syntax**: `DataTbyte arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataOword

**Description**: Mark data at address as Oword.

**Syntax**: `DataOword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataMmword

**Description**: Mark data at address as Mmword.

**Syntax**: `DataMmword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataXmmword

**Description**: Mark data at address as Xmmword.

**Syntax**: `DataXmmword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataYmmword

**Description**: Mark data at address as Ymmword.

**Syntax**: `DataYmmword arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataFloat

**Description**: Mark data at address as Float.

**Syntax**: `DataFloat arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataDouble

**Description**: Mark data at address as Double.

**Syntax**: `DataDouble arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataLongdouble

**Description**: Mark data at address as Long double.

**Syntax**: `DataLongdouble arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataAscii

**Description**: Mark data at address as Ascii.

**Syntax**: `DataAscii arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataUnicode

**Description**: Mark data at address as Unicode.

**Syntax**: `DataUnicode arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataCode

**Description**: Mark data at address as Code.

**Syntax**: `DataCode arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataJunk

**Description**: Mark data at address as Junk.

**Syntax**: `DataJunk arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: DataMiddle

**Description**: Mark data at address as Middle.

**Syntax**: `DataMiddle arg1 [arg2]`

**Arguments**:

- `arg1`: The address you want to mark.
- `[arg2]`: Size (in bytes) to mark, when not set this defaults to 1.

**Response**: This command does not set any result variables.

### Command: AddType

**Description**: Add a type alias.

**Syntax**: `AddType arg1 arg2`

**Arguments**:

- `arg1`: An existing type.
- `arg2`: The new type alias.

**Response**: This command does not set any result variables.

### Command: AddStruct

**Description**: Add a new struct.

**Syntax**: `AddStruct arg1`

**Arguments**:

- `arg1`: The type name of the struct.

**Response**: This command does not set any result variables.

### Command: AddUnion

**Description**: Add a new union.

**Syntax**: `AddUnion arg1`

**Arguments**:

- `arg1`: The type name of the union.

**Response**: This command does not set any result variables.

### Command: AddMember

**Description**: Add a new member to the end of a struct/union.

**Syntax**: `AddMember arg1 arg2 arg3 [arg4] [arg5]`

**Arguments**:

- `arg1`: The type name of the struct/union (parent).
- `arg2`: The type of the new member.
- `arg3`: The name of the new member.
- `[arg4]`: The array size. A value greater than zero will make this member an array.
- `[arg5]`: Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is not allowed.

**Response**: This command does not set any result variables.

### Command: AppendMember

**Description**: Add a new member to the end of the last manipulated struct/union.

**Syntax**: `AppendMember arg1 arg2 [arg3] [arg4]`

**Arguments**:

- `arg1`: The type of the new member.
- `arg2`: The name of the new member.
- `[arg3]`: The array size. A value greater than zero will make this member an array.
- `[arg4]`: Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is not allowed.

**Response**: This command does not set any result variables.

### Command: AddFunction

**Description**: Add a new function.

**Syntax**: `AddFunction arg1 arg2 [arg3] [arg4]`

**Arguments**:

- `arg1`: The type name of the function.
- `arg2`: The return type.
- `[arg3]`: Calling convention, choose between Calling convention, choose between `cdecl`, `stdcall`, `thiscall` and `delphi`.
- `[arg4]`: Set to nonzero to mark this function as Set to nonzero to mark this function as `noreturn`.

**Response**: This command does not set any result variables.

### Command: AddArg

**Description**: Add a new argument to the end of a function.

**Syntax**: `AddArg arg1 arg2 arg3`

**Arguments**:

- `arg1`: The type name of the function (parent).
- `arg2`: The type of the new argument.
- `arg3`: The name of the new argument.

**Response**: This command does not set any result variables.

### Command: AppendArg

**Description**: Add a new argument to the end of the last manipulated function.

**Syntax**: `AppendArg arg1 arg2`

**Arguments**:

- `arg1`: The type of the new argument.
- `arg2`: The name of the new argument.

**Response**: This command does not set any result variables.

### Command: SizeofType

**Description**: Get the size of a type.

**Syntax**: `SizeofType arg1`

**Arguments**:

- `arg1`: Name of the type.

**Response**: This command will set `$result` to the size of the type.

### Command: VisitType

**Description**: Visit a type and print its members.

**Syntax**: `VisitType arg1 [arg2] [arg3]`

**Arguments**:

- `arg1`: The type to visit.
- `[arg2]`: Address to print from. If not specified (or zero) the type will be printed without values.
- `[arg3]`: Maximum pointer resolution depth (default is 0). This can be used to also display structures (and values) pointed to by members of the type you are visiting.

**Response**: This command does not set any result variables.

### Command: ClearTypes

**Description**: Clear all types.

**Syntax**: `ClearTypes [arg1]`

**Arguments**:

- `[arg1]`: The owner to clear. Leave this empty unless you know what you’re doing.

**Response**: This command does not set any result variables.

### Command: RemoveType

**Description**: Remove a type.

**Syntax**: `RemoveType arg1`

**Arguments**:

- `arg1`: The type to remove.

**Response**: This command does not set any result variables.

### Command: EnumTypes

**Description**: Enumerate all types.

**Syntax**: `EnumTypes`

**Arguments**: None

**Response**: This command does not set any result variables.

### Command: LoadTypes

**Description**: Load types from a JSON file.

**Syntax**: `LoadTypes arg1`

**Arguments**:

- `arg1`: The path to the JSON file. The owner of the loaded types will be the filename of the JSON file. Any types previously defined with this owner will be removed.

**Response**: This command does not set any result variables.

### Command: ParseTypes

**Description**: Parse and load types from a header file.

**Syntax**: `ParseTypes arg1`

**Arguments**:

- `arg1`: The path to the header file. The owner of the loaded types will be the filename of the header file. Any types previously defined with this owner will be removed.

**Response**: This command does not set any result variables.

## Conditional Breakpoint Control

### Command: SetBreakpointName

**Description**: Sets the name of a software breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

**Syntax**: `SetBreakpointName arg1 [arg2]`

**Arguments**:

- `arg1`: The address of an existing software breakpoint.
- `[arg2]`: The name of the breakpoint (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetBreakpointCondition

**Description**: Sets the software breakpoint condition. When this condition is set, it is evaluated every time the breakpoint hits and the debugger would stop only if condition is not 0.

**Syntax**: `SetBreakpointCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The condition expression.

**Response**: This command does not set any result variables.

### Command: SetBreakpointLog

**Description**: Sets log text when a software breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetBreakpointLog arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The log format string (see introduction/formatting).

**Response**: This command does not set any result variables.

### Command: SetBreakpointLogCondition

**Description**: Sets the logging condition of a software breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetBreakpointLogCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The logging condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetBreakpointCommand

**Description**: Sets the command to execute when a software breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetBreakpointCommand arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The command (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetBreakpointCommandCondition

**Description**: Sets the command condition of a software breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetBreakpointCommandCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The command condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetBreakpointFastResume

**Description**: Sets the fast resume flag of a software breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

**Syntax**: `SetBreakpointFastResume arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetBreakpointSingleshoot

**Description**: Sets the singleshoot flag of a software breakpoint. If this flag is set the breakpoint will be removed on the first hit.

**Syntax**: `SetBreakpointSingleshoot arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetBreakpointSilent

**Description**: Sets the silent flag of a software breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

**Syntax**: `SetBreakpointSilent arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: GetBreakpointHitCount

**Description**: Gets the hit counter of a software breakpoint.

**Syntax**: `GetBreakpointHitCount arg1`

**Arguments**:

- `arg1`: The address of the breakpoint.

**Response**: `$result` will be set to the current value of the hit counter.

### Command: ResetBreakpointHitCount

**Description**: Resets the hit counter of a software breakpoint.

**Syntax**: `ResetBreakpointHitCount arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The new hit count (zero when not specified).

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointName

**Description**: Sets the name of a hardware breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

**Syntax**: `SetHardwareBreakpointName arg1 [arg2]`

**Arguments**:

- `arg1`: The address of an existing hardware breakpoint.
- `[arg2]`: The name of the breakpoint (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointCondition

**Description**: Sets the hardware breakpoint condition. When this condition is set, it is evaluated every time the breakpoint hits and the debugger would stop only if condition is not 0.

**Syntax**: `SetHardwareBreakpointCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The condition expression.

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointLog

**Description**: Sets log text when a hardware breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetHardwareBreakpointLog arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The log format string (see introduction/formatting).

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointLogCondition

**Description**: Sets the logging condition of a hardware breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetHardwareBreakpointLogCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The logging condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointCommand

**Description**: Sets the command to execute when a hardware breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetHardwareBreakpointCommand arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The command (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointCommandCondition

**Description**: Sets the command condition of a hardware breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetHardwareBreakpointCommandCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The command condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointFastResume

**Description**: Sets the fast resume flag of a hardware breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

**Syntax**: `SetHardwareBreakpointFastResume arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointSingleshoot

**Description**: Sets the singleshoot flag of a hardware breakpoint. If this flag is set the breakpoint will be removed on the first hit.

**Syntax**: `SetHardwareBreakpointSingleshoot arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetHardwareBreakpointSilent

**Description**: Sets the silent flag of a hardware breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

**Syntax**: `SetHardwareBreakpointSilent arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: GetHardwareBreakpointHitCount

**Description**: Gets the hit counter of a hardware breakpoint.

**Syntax**: `GetHardwareBreakpointHitCount arg1`

**Arguments**:

- `arg1`: The address of the breakpoint.

**Response**: `$result` will be set to the current value of the hit counter.

### Command: ResetHardwareBreakpointHitCount

**Description**: Resets the hit counter of a hardware breakpoint.

**Syntax**: `ResetHardwareBreakpointHitCount arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The new hit count (zero when not specified).

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointName

**Description**: Sets the name of a memory breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

**Syntax**: `SetMemoryBreakpointName arg1 [arg2]`

**Arguments**:

- `arg1`: The address of an existing memory breakpoint.
- `[arg2]`: The name of the breakpoint (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointCondition

**Description**: Sets the memory breakpoint condition. When this condition is set, it is evaluated every time the breakpoint hits and the debugger would stop only if condition is not 0.

**Syntax**: `SetMemoryBreakpointCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The condition expression.

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointLog

**Description**: Sets log text when a memory breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetMemoryBreakpointLog arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The log format string (see introduction/formatting).

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointLogCondition

**Description**: Sets the logging condition of a memory breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetMemoryBreakpointLogCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The logging condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointCommand

**Description**: Sets the command to execute when a memory breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetMemoryBreakpointCommand arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The command (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointCommandCondition

**Description**: Sets the command condition of a memory breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetMemoryBreakpointCommandCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The command condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointFastResume

**Description**: Sets the fast resume flag of a memory breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

**Syntax**: `SetMemoryBreakpointFastResume arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointSingleshoot

**Description**: Sets the singleshoot flag of a memory breakpoint. If this flag is set the breakpoint will be removed on the first hit.

**Syntax**: `SetMemoryBreakpointSingleshoot arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetMemoryBreakpointSilent

**Description**: Sets the silent flag of a memory breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

**Syntax**: `SetMemoryBreakpointSilent arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: GetMemoryBreakpointHitCount

**Description**: Gets the hit counter of a memory breakpoint.

**Syntax**: `GetMemoryBreakpointHitCount arg1`

**Arguments**:

- `arg1`: The address of the breakpoint.

**Response**: `$result` will be set to the current value of the hit counter.

### Command: ResetMemoryBreakpointHitCount

**Description**: Resets the hit counter of a memory breakpoint.

**Syntax**: `ResetMemoryBreakpointHitCount arg1 [arg2]`

**Arguments**:

- `arg1`: The address of the breakpoint.
- `[arg2]`: The new hit count (zero when not specified).

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointName

**Description**: Sets the name of a librarian breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

**Syntax**: `SetLibrarianBreakpointName arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The name of the breakpoint (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointCondition

**Description**: Sets the librarian breakpoint condition. When this condition is set, it is evaluated every time the breakpoint occurs and the debugger would stop only if condition is not 0.

**Syntax**: `SetLibrarianBreakpointCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The condition expression.

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointLog

**Description**: Sets log text when a librarian breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetLibrarianBreakpointLog arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The log format string (see introduction/formatting).

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointLogCondition

**Description**: Sets the logging condition of a librarian breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetLibrarianBreakpointLogCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The logging condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointCommand

**Description**: Sets the command to execute when a librarian breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetLibrarianBreakpointCommand arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The command (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointCommandCondition

**Description**: Sets the command condition of a librarian breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetLibrarianBreakpointCommandCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The command condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointFastResume

**Description**: Sets the fast resume flag of a librarian breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

**Syntax**: `SetLibrarianBreakpointFastResume arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointSingleshoot

**Description**: Sets the singleshoot flag of a librarian breakpoint. If this flag is set the librarian breakpoint will be removed on the first hit.

**Syntax**: `SetLibrarianBreakpointSingleshoot arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetLibrarianBreakpointSilent

**Description**: Sets the silent flag of a librarian breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

**Syntax**: `SetLibrarianBreakpointSilent arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: GetLibrarianBreakpointHitCount

**Description**: Gets the hit counter of a librarian breakpoint.

**Syntax**: `GetLibrarianBreakpointHitCount arg1`

**Arguments**:

- `arg1`: The DLL name.

**Response**: `$result` will be set to the current value of the hit counter.

### Command: ResetLibrarianBreakpointHitCount

**Description**: Resets the hit counter of a librarian breakpoint.

**Syntax**: `ResetLibrarianBreakpointHitCount arg1 [arg2]`

**Arguments**:

- `arg1`: The DLL name.
- `[arg2]`: The new hit count (zero when not specified).

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointName

**Description**: Sets the name of an exception breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

**Syntax**: `SetExceptionBreakpointName arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The name of the breakpoint (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointCondition

**Description**: Sets the exception breakpoint condition. When this condition is set, it is evaluated every time the exception occurs (chance must match) and the debugger would stop only if condition is not 0.

**Syntax**: `SetExceptionBreakpointCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The condition expression.

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointLog

**Description**: Sets log text when an exception breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetExceptionBreakpointLog arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The log format string (see introduction/formatting).

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointLogCondition

**Description**: Sets the logging condition of an exception breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

**Syntax**: `SetExceptionBreakpointLogCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The logging condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointCommand

**Description**: Sets the command to execute when an exception breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetExceptionBreakpointCommand arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The command (empty when not specified).

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointCommandCondition

**Description**: Sets the command condition of an exception breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

**Syntax**: `SetExceptionBreakpointCommandCondition arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The command condition (default condition when not specified).

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointFastResume

**Description**: Sets the fast resume flag of an exception breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

**Syntax**: `SetExceptionBreakpointFastResume arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointSingleshoot

**Description**: Sets the singleshoot flag of an exception breakpoint. If this flag is set the exception breakpoint will be removed on the first hit.

**Syntax**: `SetExceptionBreakpointSingleshoot arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: SetExceptionBreakpointSilent

**Description**: Sets the silent flag of an exception breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

**Syntax**: `SetExceptionBreakpointSilent arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.
- `[arg2]`: The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

**Response**: This command does not set any result variables.

### Command: GetExceptionBreakpointHitCount

**Description**: Gets the hit counter of an exception breakpoint.

**Syntax**: `GetExceptionBreakpointHitCount arg1`

**Arguments**:

- `arg1`: The name, exception name or code of the exception breakpoint.

**Response**: `$result` will be set to the current value of the hit counter.

### Command: ResetExceptionBreakpointHitCount

**Description**: Resets the hit counter of an exception breakpoint.

**Syntax**: `ResetExceptionBreakpointHitCount arg1 [arg2]`

**Arguments**:

- `arg1`: The name, exception code or name of the exception breakpoint.
- `[arg2]`: The new hit count (zero when not specified).

**Response**: This command does not set any result variables.

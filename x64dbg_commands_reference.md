# x64dbg Command Reference

## Operating System Control

DisablePrivilege - Revoke the privilege.

`arg1` - The name of the privilege. Example: The name of the privilege. Example: `SeDebugPrivilege`

Response: None

EnablePrivilege - Permit the privilege.

`arg1` - The name of the privilege. Example: The name of the privilege. Example: `SeDebugPrivilege`

Response: None

GetPrivilegeState - Query whether the privilege is enabled on the debuggee.

`arg1` - The name of the privilege. Example: The name of the privilege. Example: `SeDebugPrivilege`.

Response: None

handleclose - Close a remote handle so that its system resources can be released.

`arg1` - The handle value of the handle, in the context of the debuggee. The handle value of the handle, in the context of the debuggee.

Response: None

## Memory Operations

alloc - Allocate memory in the debuggee (using VirtualAllocEx). The memory is allocated with PAGE_EXECUTE_READWRITE protection.

`[arg1]` - Size of the memory to allocate. When not specified, a default size of 0x1000 is used. Size of the memory to allocate. When not specified, a default size of 0x1000 is used.
`[arg2]` - Address to allocate the memory at. Unspecified or zero means a random address. Address to allocate the memory at. Unspecified or zero means a random address.

Response: This command sets $result to the allocated memory address. It also sets the $lastalloc variable to the allocated memory address when VirtualAllocEx succeeded.

Fill - Set memory of the debuggee to a specified byte.

`arg1` - Memory address to start setting bytes. Memory address to start setting bytes.
`arg2` - Value (byte) to set memory with. Value (byte) to set memory with.
`[arg3]` - Size to set. When not specified the rest of the page is used. Size to set. When not specified the rest of the page is used.

Response: This command does not set any result variables.

memcpy - Copy memory in the context of the debuggee, without applying patches.

`arg1` - Destination address. Destination address.
`arg2` - Source address. Source address.
`arg3` - Size to copy. Size to copy.

Response: This command sets `$result` to the total amount of bytes written at the destination. The condition `$result==arg3` is true if all memory was copied.

free - Free memory in the debuggee (using VirtualFreeEx).

`[arg1]` - Address of the memory to free. When not specified, the value at $lastalloc is used. Address of the memory to free. When not specified, the value at $lastalloc is used.

Response: This command sets $result to 1 if VirtualFreeEx succeeded, otherwise it’s set to 0. $lastalloc is set to zero when the address specified is equal to $lastalloc.

getpagerights - Get the rights of a memory page.

`arg1` - Memory Address of page (it fix the address if this arg is not the top address of a page). Memory Address of page (it fix the address if this arg is not the top address of a page).

Response: This command does not set any result variables.

setpagerights - Change the rights of a memory page.

`arg1` - Memory Address of page (it fix the address if this arg is not the top address of a page). Memory Address of page (it fix the address if this arg is not the top address of a page).
`arg2` - New Rights, this can be one of the following values: “Execute”, “ExecuteRead”, “ExecuteReadWrite”, “ExecuteWriteCopy”, “NoAccess”, “ReadOnly”, “ReadWrite”, “WriteCopy”. You can add a G at first for add PAGE GUARD. example: “GReadOnly”. Read the MSDN for more info. New Rights, this can be one of the following values: “Execute”, “ExecuteRead”, “ExecuteReadWrite”, “ExecuteWriteCopy”, “NoAccess”, “ReadOnly”, “ReadWrite”, “WriteCopy”. You can add a G at first for add PAGE GUARD. example: “GReadOnly”. Read the MSDN for more info.

Response: This command does not set any result variables.

savedata - Save a memory region to disk.

`arg1` - The filename. If you use The filename. If you use `:memdump:` as name it will save a file as `memdump_pid_addr_size.bin` in the x64dbg directory. You can use String Formatting here.
`arg2` - The address of the memory region. The address of the memory region.
`arg3` - The size of the memory region. The size of the memory region.

Response: None

minidump - Create aminidumpwith full memory and handle information from the debuggee.

`arg1` - The filename of the The filename of the `.dmp`.

Response: None

## Thread Control

createthread[,threadcreate,newthread,threadnew] - Create a new thread at the specified entry.

`arg1` - The entry of the new thread. The entry of the new thread.
`[arg2]` - The argument of the new thread. If the argument is not specified, the default argument is 0. The argument of the new thread. If the argument is not specified, the default argument is 0.

Response: None

switchthread - Switch the internal current thread to another thread (resulting in different callstack + different registers displayed).

`[arg1]` - ThreadId of the thread to switch to (see the Threads tab). When not specified, the main thread is used. ThreadId of the thread to switch to (see the Threads tab). When not specified, the main thread is used.

Response: This command does not set any result variables.

suspendthread - Suspend a thread in the debuggee.

`[arg1]` - ThreadId of the thread to suspend (see the Threads tab). When not specified, the main thread is used. ThreadId of the thread to suspend (see the Threads tab). When not specified, the main thread is used.

Response: This command does not set any result variables.

resumethread - Resume a thread in the debuggee.

`[arg1]` - ThreadId of the thread to resume (see the Threads tab). When not specified, the main thread is used. ThreadId of the thread to resume (see the Threads tab). When not specified, the main thread is used.

Response: This command does not set any result variables.

killthread - Kill a thread in the debuggee.

`[arg1]` - ThreadId of the thread to kill (see the Threads tab). When not specified, the main thread is used. ThreadId of the thread to kill (see the Threads tab). When not specified, the main thread is used.
`[arg2]` - Thread exit code. When not specified, 0 will be used. Thread exit code. When not specified, 0 will be used.

Response: This command does not set any result variables.

suspendallthreads - Suspend all threads in the debuggee.

Takes no arguments.

Response: This command does not set any result variables.

resumeallthreads - Resume all threads in the debuggee.

Takes no arguments.

Response: This command does not set any result variables.

setthreadpriority - Set thread priority in the debuggee.

`arg1` - ThreadId of the thread to change the priority of (see the Threads tab). ThreadId of the thread to change the priority of (see the Threads tab).
`arg2` - Priority value, this can be the integer of a valid thread priority (see MSDN) or one of the following values: “Normal”, “AboveNormal”, “TimeCritical”, “Idle”, “BelowNormal”, “Highest”, “Lowest”. Priority value, this can be the integer of a valid thread priority (see MSDN) or one of the following values: “Normal”, “AboveNormal”, “TimeCritical”, “Idle”, “BelowNormal”, “Highest”, “Lowest”.

Response: This command does not set any result variables.

setthreadname - Set thread name (only for the debugger, nothing changes in the debuggee).

`arg1` - ThreadId of the thread to change the priority of (see the Threads tab). ThreadId of the thread to change the priority of (see the Threads tab).
`arg2` - New thread name. Leave empty to remove the current name. New thread name. Leave empty to remove the current name.

Response: This command does not set any result variables.

## Watch Control

AddWatch - Add a watch item.

`arg1` - The expression to watch. The expression to watch.
`[arg2]` - The data type of the watch item. The data type of the watch item. `uint` displays hexadecimal value, `int` displays signed decimal value, `ascii` displays the ASCII string pointed by the value. `unicode` displays the Unicode string pointed by the value. `uint` is the default type.

Response: None

DelWatch - Delete a watch item.

`arg1` - The id of the watch item to delete. The id of the watch item to delete.

Response: This command does not set any result variables.

SetWatchdog - Set the watchdog mode of a watch item.

`arg1` - The id of the watch item. The id of the watch item.
`[arg2]` - The watchdog mode. Possible values: The watchdog mode. Possible values:

Response: None

SetWatchExpression - Change the expression of an existing watch item.

`arg1` - The id of the watch item. The id of the watch item.
`arg2` - The new expression to watch. The new expression to watch.
`arg3` - The new data type of the watch item. The new data type of the watch item.

Response: None

SetWatchName - Rename a watch item.

`arg1` - The id of the watch item to rename. The id of the watch item to rename.
`arg2` - The new name. The new name.

Response: None

CheckWatchdog - Evaluate all the watch items, trigger or reset watchdog when appropiate.

Takes no arguments.

Response: None

## Variables

var - Declare a new variable.

`arg1` - Variable name (will be prefixed with ‘$’ if not done). Variable name (will be prefixed with ‘$’ if not done).
`[arg2]` - Initial variable value (see console input for details). Initial variable value (see console input for details).

Response: This command does not set any result variables.

vardel - Delete a user-defined variable.

`arg1` - Name of the variable to delete ($ will be prepended when not present). Name of the variable to delete ($ will be prepended when not present).

Response: This command does not set any result variables.

varlist - Get a list of all variables and their values.

`[arg1]` - Filter (USER, SYSTEM, READONLY). Filter (USER, SYSTEM, READONLY).

Response: This command does not set any result variables.

## Tracing

TraceIntoConditional - Trace the program byStepInto, until the specified condition is satisfied, or maximum number of steps reached.

`arg1` - The condition used. When this is evaluated to be a value other than 0, tracing will stop. The condition used. When this is evaluated to be a value other than 0, tracing will stop.
`[arg2]` - The maximum step count to trace before the debugger gives up. The maximum step count to trace before the debugger gives up.

Response: None

TraceOverConditional - Trace the program byStepOver, until the specified condition is satisfied, or maximum number of steps reached.

`arg1` - The condition used. When this is evaluated to be a value other than 0, tracing will stop. The condition used. When this is evaluated to be a value other than 0, tracing will stop.
`[arg2]` - The maximum step count to trace before the debugger gives up. The maximum step count to trace before the debugger gives up.

Response: None

TraceIntoBeyondTraceCoverage - PerformStepIntountil the program reaches somewhere outside the trace coverage. This is similar toticndtr.hitcount(cip)==0&&arg1,arg2except that it achieves higher performance by avoiding the expression function invocation.

`[arg1]` - The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
`[arg2]` - The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000. The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

Response: This command does not set any result variables.

TraceOverBeyondTraceCoverage,TraceOverBeyondTraceRecord - Perform StepOver until the program reaches somewhere outside the trace coverage.

`[arg1]` - The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
`[arg2]` - The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000. The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

Response: This command does not set any result variables.

TraceIntoIntoTraceCoverage - Perform StepInto until the program reaches somewhere inside the trace coverage.

`[arg1]` - The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
`[arg2]` - The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000. The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

Response: This command does not set any result variables.

TraceOverIntoTraceCoverage - Perform StepOver until the program reaches somewhere inside the trace coverage.

`[arg1]` - The break condition of tracing. When this condition is satisfied, tracing will stop regardless of The break condition of tracing. When this condition is satisfied, tracing will stop regardless of `EIP`/ `RIP` location. If this argument is not specified then tracing will be unconditional.
`[arg2]` - The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000. The maximun steps before the debugger gives up. If this argument is not specified, the default value will be 50000.

Response: This command does not set any result variables.

RunToParty - Run the program until the program reaches somewhere belonging to the party number. This works by putting temporary memory breakpoints on all memory pages with matching party number.

`arg1` - The party number. This value cannot be an expression. Note: The party number. This value cannot be an expression. Note: `0` is user module, `1` is system module.

Response: None

RunToUserCode - Run until user code is reached. It is equivallent toRunToParty0.

Takes no arguments.

Response: None

TraceSetLog - Change the trace log text and condition during tracing. SeeConditional Tracingfor more information.

`[arg1]` - Log text. If not specified the current text/condition is cleared. Log text. If not specified the current text/condition is cleared.
`[arg2]` - Log condition. If not specified the default condition is used. Log condition. If not specified the default condition is used.

Response: None

TraceSetCommand - Change the trace command text and condition during tracing. SeeConditional Tracingfor more information.

`[arg1]` - Command text. If not specified the current text/condition is cleared. Command text. If not specified the current text/condition is cleared.
`[arg2]` - Command condition. If not specified the default condition is used. Command condition. If not specified the default condition is used.

Response: None

TraceSetLogFile - Redirect the trace log to a file.

`arg1` - File name to redirect the trace log to. This file will be cleared and overwritten when the trace starts. File name to redirect the trace log to. This file will be cleared and overwritten when the trace starts. This does nothing if you don’t set the log text!

Response: None

StartTraceRecording - Start recording a trace to the specified file. The file will also be opened in the trace view. Note you need to useTraceIntoConditionalor other command to actually trace the program and record instructions.

`arg1` - The file name. Default file extension “trace32” or “trace64” is not added automatically. The file name. Default file extension “trace32” or “trace64” is not added automatically.

Response: This command does not set any result variables.

StopTraceRecording - Stops trace recording and closes the file.

Takes no arguments.

Response: This command does not set any result variables.

## Searching

find - Find a pattern in a memory page. If you want to find all occurrences of a pattern in a memory page usefindall.

`arg1` - The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first. If you want to find all occurrences of a pattern in the entire memory map use The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first. If you want to find all occurrences of a pattern in the entire memory map use findallmem.
`arg2` - The byte pattern to search for. This byte pattern can contain wildcards (?) for example: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`. You can use String Formatting here.
`[arg3]` - The size of the data to search in. Default is the size of the memory region. The size of the data to search in. Default is the size of the memory region.

Response: The `$result` variable is set to the virtual address of the address that matches the byte pattern. `$result` will be 0 when the pattern could not be matched.

findall - Find all occurrences of a pattern in a memory page.

`arg1` - The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first. You can use The address to start searching from. Notice that the searching will stop when the end of the memory page this address resides in has been reached. This means you cannot search the complete process memory without enumerating the memory pages first. You can use findallmem to search for a pattern in the whole memory.
`arg2` - The byte pattern to search for. This byte pattern can contain wildcards (?) for example: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`. You can use String Formatting here.
`[arg3]` - The size of the data to search in. Default is the size of the memory region. The size of the data to search in. Default is the size of the memory region.

Response: `$result` is set to the number of occurrences.

findallmem - Find all occurrences of a pattern in the entire memory map.

`arg1` - The address to start searching from. The address to start searching from.
`arg2` - The byte pattern to search for. This byte pattern can contain wildcards (?) for example: The byte pattern to search for. This byte pattern can contain wildcards (?) for example: `EB0?90??8D`. You can use String Formatting here.
`[arg3]` - The size of the data to search in. Default is the entire memory map ( The size of the data to search in. Default is the entire memory map ( `-1`).
`[arg4]` - Set to Set to `user`/ `system`/ `module` to only include (user/system) modules in the search.

Response: `$result` is set to the number of occurrences.

findasm - Find assembled instruction.

`arg1` - Instruction to look for (make sure to use quoted “mov eax, ebx” to ensure you actually search for that instruction). You can use Instruction to look for (make sure to use quoted “mov eax, ebx” to ensure you actually search for that instruction). You can use String Formatting here.
`[arg2]` - Address of/inside a memory page to look in. When not specified CIP will be used. Address of/inside a memory page to look in. When not specified CIP will be used.
`[arg3]` - The size of the data to search in. Default is the size of the memory region. The size of the data to search in. Default is the size of the memory region.

Response: The `$result` variable is set to the number of references found.

findguid - Find references to GUID. The referenced GUID must be registered in the system, otherwise it will not be found.

`[arg1]` - The base of the memory range. If not specified, The base of the memory range. If not specified, `RIP` or `EIP` will be used.
`[arg2]` - The size of the memory range. The size of the memory range.
`[arg3]` - The region to search. The region to search. `0` is current region (specified with arg1 and arg2). `1` is current module (the module specified with arg1). `2` is all modules.

Response: None

reffind - Find references to a certain value.

`arg1` - The value to look for. The value to look for.
`[arg2]` - Address of/inside a memory page to look in. When not specified CIP will be used. Address of/inside a memory page to look in. When not specified CIP will be used.
`[arg3]` - The size of the data to search in. The size of the data to search in.

Response: The `$result` variable is set to the number of references found.

reffindrange - Find references to a certain range of values.

`arg1` - Start of the range (will be included in the results when found). Start of the range (will be included in the results when found).
`[arg2]` - End of range (will be included in the results when found). When not specified the first argument will be used. End of range (will be included in the results when found). When not specified the first argument will be used.
`[arg3]` - Address of/inside a memory page to look in. When not specified CIP will be used. Address of/inside a memory page to look in. When not specified CIP will be used.
`[arg4]` - The size of the data to search in. The size of the data to search in.

Response: The `$result` variable is set to the number of references found.

refstr - Find referenced text strings.

`[arg1]` - Address of/inside a memory page to find referenced text strings in. When not specified CIP will be used. Address of/inside a memory page to find referenced text strings in. When not specified CIP will be used.
`[arg2]` - The size of the data to search in. The size of the data to search in.

Response: The `$result` variable is set to the number of string references found.

modcallfind - Find all inter-modular calls.

`[arg1]` - Address of/inside a memory page to find inter-modular calls in. When not specified EIP/RIP will be used. Address of/inside a memory page to find inter-modular calls in. When not specified EIP/RIP will be used.
`[arg2]` - The size of the data to search in. The size of the data to search in.

Response: The `$result` variable is set to the number of inter-modular calls found.

setmaxfindresult - Set the maximum number of occurences found.

`arg1` - The maximum number of occurences. The default value is 5000. The maximum number of occurences. The default value is 5000.

Response: None

## Debug Control

InitDebug - Initializes the debugger. This command will load the executable (do some basic checks), set breakpoints on TLS callbacks (if present), set a breakpoint at the process entry point and break at the system breakpoint before giving back control to the user.

`arg1` - Path to the executable file to debug. If no full path is given, the Path to the executable file to debug. If no full path is given, the `GetCurrentDirectory` API will be called to retrieve a full path. Use quotation marks to include spaces in your path.
`[arg2]` - Commandline to create the process with. Commandline to create the process with.
`[arg3]` - Current folder (passed to the Current folder (passed to the `CreateProcess` API) (this is also sometimes called ‘working directory’ or ‘current directory’)

Response: This command will give control back to the user after the system breakpoint is reached. It will set `$pid` and `$hp`/`$hProcess` variables.

StopDebug - Terminate the current debuggee and stop debugging it.

Takes no arguments.

Response: This command does not set any result variables.

AttachDebugger - Attach the debugger to a running process.

`arg1` - Process Identifier (PID) of the running process. Process Identifier (PID) of the running process.
`[arg2]` - Handle to an Event Object to signal (this is for internal use only). Handle to an Event Object to signal (this is for internal use only).
`[arg3]` - Thread Identifier (TID) of the thread to resume after attaching (this is for internal use only). Thread Identifier (TID) of the thread to resume after attaching (this is for internal use only).

Response: This command will give control back to the user after the system breakpoint is reached. It will set `$pid` and `$hp`/`$hProcess` variables.

DetachDebugger - Detach the debugger from the currently-debugged process.

Takes no arguments.

Response: None

run - Free the lock and allow the program to run.

`[arg1]` - When specified, place a single-shot breakpoint at this location before running. When specified, place a single-shot breakpoint at this location before running.

Response: None

erun - Free the lock and allow the program to run,passing all first-chance exceptions to the debuggee.

`[arg1]` - When specified, place a single-shot breakpoint at this location before running. When specified, place a single-shot breakpoint at this location before running.

Response: None

serun - Free the lock and allow the program to run,swallowing the current exception, skipping exception dispatching in the debuggee.

`[arg1]` - When specified, place a single-shot breakpoint at this location before running. When specified, place a single-shot breakpoint at this location before running.

Response: None

pause - Pause the debuggee or stop animation if animation is in progress.

Takes no arguments.

Response: This command does not set any result variables.

DebugContinue - Set debugger continue status.

`[arg1]` - When set (to anything), the exception will be handled by the program. Otherwise the exception will be swallowed. When set (to anything), the exception will be handled by the program. Otherwise the exception will be swallowed.

Response: This command does not set any result variables.

StepInto - Single Step (using Trap-Flag).

`[arg1]` - The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

Response: This command does not set any result variables.

eStepInto - Single Step (using Trap-Flag),passing all first-chance exceptions to the debuggee.

`[arg1]` - The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

Response: This command does not set any result variables.

seStepInto - Single Step (using Trap-Flag),swallowing the current exception, skipping exception dispatching in the debuggee.

`[arg1]` - The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

Response: This command does not set any result variables.

StepOver - Step over calls. When the instruction at EIP/RIP isn’t a call, a StepInto is performed.

Takes no arguments.

Response: None

eStepOver - Step over calls,passing all first-chance exceptions to the debuggee. When the instruction at EIP/RIP isn’t a call, aeStepIntois performed.

`[arg1]` - The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

Response: This command does not set any result variables.

seStepOver - Step over calls,swallowing the current exception, skipping exception dispatching in the debuggee. When the instruction at EIP/RIP isn’t a call, aeStepIntois performed.

`[arg1]` - The number of steps to take. If not specified The number of steps to take. If not specified `1` is used.

Response: This command does not set any result variables.

StepOut - Return from function by calling StepOver until the current instruction is a RET.

`[arg1]` - The number of times to step out. If not specified The number of times to step out. If not specified `1` is used.

Response: This command does not set any result variables.

eStepOut - Return from function by calling eStepOver until the current instruction is a RET. This commandpasses all first-chance exceptions to the debuggee.

`[arg1]` - The number of times to step out. If not specified The number of times to step out. If not specified `1` is used.

Response: This command does not set any result variables.

skip - Skip the next instruction. This command swallows the current exception (if present). Useful if you want to continue after an INT3 command.

`[arg1]` - The number of instructions to skip. If not specified The number of instructions to skip. If not specified `1` is used.

Response: This command does not set any result variables.

InstrUndo - Undo last instruction stepped. This command is only valid if some instructions are stepped in. Stepping over, running or tracing will clear the history context.

Takes no arguments.

Response: None

StepUser - Step into until reaching a user module.

Takes no arguments.

Response: None

StepSystem - Step into until reaching a system module.

Takes no arguments.

Response: None

## Plugins

StartScylla - Start the Scylla plugin auto-selecting the currently debugged DLL/EXE and EIP/RIP as entry point.

Takes no arguments.

Response: This command does not set any result variables.

plugload - Load a plugin.

`arg1` - Name of the plugin. Name of the plugin.

Response: This command does not set any result variables.

plugunload - Unload a plugin.

`arg1` - Name of the plugin. Name of the plugin.

Response: This command does not set any result variables.

## Breakpoint Control

SetBPX - Set an INT3 (SHORT/LONG) or UD2 breakpoint and optionally assign a name to it.

`arg1` - Address to put a breakpoint on. This can be an API name. Address to put a breakpoint on. This can be an API name.
`[arg2]` - Name of the breakpoint, use quotation marks to include spaces. This name can be used by the EnableBPX, DisableBPX and DeleteBPX functions as alias, but is mainly intended to provide a single line of information about the currently-hit breakpoint. When arg2 equals to a valid type (arg3) the type is used and arg2 is ignored. Name of the breakpoint, use quotation marks to include spaces. This name can be used by the EnableBPX, DisableBPX and DeleteBPX functions as alias, but is mainly intended to provide a single line of information about the currently-hit breakpoint. When arg2 equals to a valid type (arg3) the type is used and arg2 is ignored.
`[arg3]` - Breakpoint type. Can be one of the following options in random order: “ss” (single shot breakpoint), “long” (CD03), “ud2” (0F0B) and “short” (CC). You can combine the “ss” option with one of the type options in one string. Example: “SetBPX 00401000,”entrypoint”,ssud2” will set a single shot UD2 breakpoint at 00401000 with the name “entrypoint”. When specifying no type or just the type “ss” the default type will be used. Per default this equals to the “short” type. You can change the default type using the “SetBPXOptions” command. Breakpoint type. Can be one of the following options in random order: “ss” (single shot breakpoint), “long” (CD03), “ud2” (0F0B) and “short” (CC). You can combine the “ss” option with one of the type options in one string. Example: “SetBPX 00401000,”entrypoint”,ssud2” will set a single shot UD2 breakpoint at 00401000 with the name “entrypoint”. When specifying no type or just the type “ss” the default type will be used. Per default this equals to the “short” type. You can change the default type using the “SetBPXOptions” command.

Response: This command does not any result variables.

DeleteBPX - Delete a breakpoint set using the SetBPX command.

`[arg1]` - Name or address of the breakpoint to delete. If this argument is not specified, all breakpoints will be deleted. Name or address of the breakpoint to delete. If this argument is not specified, all breakpoints will be deleted.

Response: This command does not set any result variables.

EnableBPX - Enable a breakpoint set using the SetBPX command.

`[arg1]` - Name or address of the breakpoint to enable. If this argument is not specified, all breakpoints will be enabled. Name or address of the breakpoint to enable. If this argument is not specified, all breakpoints will be enabled.

Response: This command does not set any result variables.

DisableBPX - Disable a breakpoint set using the SetBPX command.

`[arg1]` - Name or address of the breakpoint to disable. If this argument is not specified, all breakpoints will be disabled. Name or address of the breakpoint to disable. If this argument is not specified, all breakpoints will be disabled.

Response: This command does not set any result variables.

SetHardwareBreakpoint - Set a hardware breakpoint (using debug registers).

`arg1` - Address of the hardware breakpoint. Address of the hardware breakpoint.
`[arg2]` - Hardware breakpoint type. Can be either ‘r’ (readwrite), ‘w’ (write) or ‘x’ (execute). When not specified, ‘x’ is assumed. Hardware breakpoint type. Can be either ‘r’ (readwrite), ‘w’ (write) or ‘x’ (execute). When not specified, ‘x’ is assumed.
`[arg3]` - Hardware breakpoint size. Can be either ‘1’, ‘2’, ‘4’ or ‘8’ (x64 only). Per default, ‘1’ is assumed. The address you’re putting the hardware breakpoint on must be aligned to the specified size. Hardware breakpoint size. Can be either ‘1’, ‘2’, ‘4’ or ‘8’ (x64 only). Per default, ‘1’ is assumed. The address you’re putting the hardware breakpoint on must be aligned to the specified size.

Response: This command does not set any result variables.

DeleteHardwareBreakpoint - Delete a hardware breakpoint set using the SetHardwareBreakpoint command.

`[arg1]` - Name or address of the hardware breakpoint to delete. If this argument is not specified, all hardware breakpoints will be deleted. Name or address of the hardware breakpoint to delete. If this argument is not specified, all hardware breakpoints will be deleted.

Response: This command does not set any result variables.

EnableHardwareBreakpoint - Enable a previously disabled hardware breakpoint.

`[arg1]` - Address of the hardware breakpoint to enable. If this argument is not specified, as many as possible hardware breakpoints will be enabled. Address of the hardware breakpoint to enable. If this argument is not specified, as many as possible hardware breakpoints will be enabled.

Response: This command does not set any result variables.

DisableHardwareBreakpoint - Disable a hardware breakpoint.

`[arg1]` - Address of the hardware breakpoint to disable. If this argument is not specified, all hardware breakpoints will be disabled. Address of the hardware breakpoint to disable. If this argument is not specified, all hardware breakpoints will be disabled.

Response: This command does not set any result variables.

SetMemoryBPX - Set a memory breakpoint (GUARD_PAGE) on the whole memory region the provided address is in.

`arg1` - Address of or inside a memory region that will be watched. Address of or inside a memory region that will be watched.
`[arg2]` - 1/0 restore the memory breakpoint once it’s hit? When this value is not equal to ‘1’ or ‘0’, it’s assumed to be arg3. This means “bpm eax,r” would be the same command as: “bpm eax,0,r”. 1/0 restore the memory breakpoint once it’s hit? When this value is not equal to ‘1’ or ‘0’, it’s assumed to be arg3. This means “bpm eax,r” would be the same command as: “bpm eax,0,r”.
`[arg3]` - Breakpoint type, it can be ‘a’ (read+write+execute) ‘r’ (read), ’w’ (write) or ‘x’ (execute). Per default, it’s ‘a’ (read+write+execute) Breakpoint type, it can be ‘a’ (read+write+execute) ‘r’ (read), ’w’ (write) or ‘x’ (execute). Per default, it’s ‘a’ (read+write+execute)

Response: This command does not set any result variables.

SetMemoryRangeBPX - Set a memory breakpoint (GUARD_PAGE) on a specific memory range.

`start` - Start of the memory range. Start of the memory range.
`size` - Size of the memory range. Size of the memory range.
`[type]` - Breakpoint type, it can be ‘a’ (read+write+execute) ‘r’ (read), ’w’ (write) or ‘x’ (execute). Per default, it’s ‘a’ (read+write+execute). Append Breakpoint type, it can be ‘a’ (read+write+execute) ‘r’ (read), ’w’ (write) or ‘x’ (execute). Per default, it’s ‘a’ (read+write+execute). Append `ss` for a singleshot breakpoint (you can also use SetMemoryBreakpointSingleshoot to do this).

Response: This command does not set any result variables.

DeleteMemoryBPX - Delete a memory breakpoint set using the SetMemoryBPX command.

`[arg1]` - Name or (base) address of the memory breakpoint to delete. If this argument is not specified, all memory breakpoints will be deleted. Name or (base) address of the memory breakpoint to delete. If this argument is not specified, all memory breakpoints will be deleted.

Response: This command does not set any result variables.

EnableMemoryBreakpoint - Enable a previously disabled memory breakpoint.

`[arg1]` - Address of the memory breakpoint to enable. If this argument is not specified, all memory breakpoints will be enabled. Address of the memory breakpoint to enable. If this argument is not specified, all memory breakpoints will be enabled.

Response: This command does not set any result variables.

DisableMemoryBreakpoint - Disable a memory breakpoint.

`[arg1]` - Address of the memory breakpoint to disable. If this argument is not specified, all memory breakpoints will be disabled. Address of the memory breakpoint to disable. If this argument is not specified, all memory breakpoints will be disabled.

Response: This command does not set any result variables.

LibrarianSetBreakpoint - Set a singleshoot breakpoint on DLL load/unload.

`arg1` - DLL Name to break on. DLL Name to break on.
`[arg2]` - `a` means on load and unload, `l` means on load, `u` means on unload. When not specified, x64dbg will break on both load and unload.
`[arg3]` - When specified, the breakpoint will be singleshoot. When not specified the breakpoint will not be removed after it has been hit. When specified, the breakpoint will be singleshoot. When not specified the breakpoint will not be removed after it has been hit.

Response: This command does not set any result variables.

LibrarianRemoveBreakpoint - Remove a DLL breakpoint.

`arg1` - DLL Name to remove the breakpoint from. DLL Name to remove the breakpoint from.

Response: This command does not set any result variables.

LibrarianEnableBreakpoint - Enable a DLL breakpoint set using the LibrarianSetBreakpoint command.

`[arg1]` - DLL Name of the DLL breakpoint to enable. If this argument is not specified, all DLL breakpoints will be enabled. DLL Name of the DLL breakpoint to enable. If this argument is not specified, all DLL breakpoints will be enabled.

Response: This command does not set any result variables.

LibrarianDisableBreakpoint - Enable a DLL breakpoint set using the LibrarianSetBreakpoint command.

`[arg1]` - DLL Name of the DLL breakpoint to disable. If this argument is not specified, all DLL breakpoints will be disabled. DLL Name of the DLL breakpoint to disable. If this argument is not specified, all DLL breakpoints will be disabled.

Response: This command does not set any result variables.

SetExceptionBPX - Set an exception breakpoint. If an exception breakpoint is active, all the exceptions with the same chance and code will be captured as a breakpoint event and will not be handled by the default exception handling policy.

`arg1` - Exception name or code of the new exception breakpoint Exception name or code of the new exception breakpoint
`[arg2]` - Chance. Set to Chance. Set to `first`/ `1` to capture first-chance exceptions, `second`/ `2` to capture second-chance exceptions, `all`/ `3` to capture all exceptions. Default value is `first`.

Response: This command does not any result variables.

DeleteExceptionBPX - Delete an exception breakpoint set using the SetExceptionBPX command.

`[arg1]` - Name, exception name or code of the exception breakpoint to delete. If this argument is not specified, all exception breakpoints will be deleted. Name, exception name or code of the exception breakpoint to delete. If this argument is not specified, all exception breakpoints will be deleted.

Response: This command does not set any result variables.

EnableExceptionBPX - Enable an exception breakpoint set using the SetExceptionBPX command.

`[arg1]` - Name, exception name or code of the exception breakpoint to enable. If this argument is not specified, all exception breakpoints will be enabled. Name, exception name or code of the exception breakpoint to enable. If this argument is not specified, all exception breakpoints will be enabled.

Response: This command does not set any result variables.

DisableExceptionBPX - Disable an exception breakpoint set using the SetExceptionBPX command.

`[arg1]` - Name, exception name or code of the exception breakpoint to enable. If this argument is not specified, all exception breakpoints will be disabled. Name, exception name or code of the exception breakpoint to enable. If this argument is not specified, all exception breakpoints will be disabled.

Response: This command does not set any result variables.

bpgoto - Configure the breakpoint so that when the program reaches it, the program will be directed to a new location. It is equivallent to the following commands:

`arg1` - The address of the breakpoint. The address of the breakpoint.
`arg2` - The new address to execute if the breakpoint is reached. The new address to execute if the breakpoint is reached.

Response: None

bplist - Get a list of breakpoints. This list includes their state (enabled/disabled), their type, their address and (optionally) their names.

Takes no arguments.

Response: This command does not set any result variables. A list entry has the following format: STATE:TYPE:ADDRESS[:NAME] STATEcan be 0 or 1. 0 means disabled, 1 means enabled. Only singleshoot and ‘normal’ breakpoints can be disabled. TYPEcan be one of the following values: BP, SS, HW and GP. BP stands for a normal breakpoint (set using the SetBPX command), SS stands for SINGLESHOT, HW stands for HARDWARE and GP stand for Guard Page, the way of setting memory breakpoints. ADDRESSis the breakpoint address, given in 32 and 64 bits for the x32 and x64 debugger respectively. NAMEis the name assigned to the breakpoint.

SetBPXOptions - Set the default type for the “SetBPX” command.

`arg1` - Default type. This can be “short” (CC), “long” (CD03) or “ud2” (0F0B). Type default type affects both NORMAL and SINGLESHOT breakpoints. Default type. This can be “short” (CC), “long” (CD03) or “ud2” (0F0B). Type default type affects both NORMAL and SINGLESHOT breakpoints.

Response: This command does not set any result variables.

## General Purpose

inc - Increase a value.

`arg1` - Destination. Destination.

Response: This command does not set any result variables.

dec - Decrease a value.

`arg1` - Destination. Destination.

Response: This command does not set any result variables.

add - Add two values.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

sub - Subtract two values.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

mul - Multiply two values and store the lower part of result intoarg1.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

mulhi - Multiply two unsigned values and store the upper part of result intoarg1.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

div - Devide two values.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

and - Binary AND two values.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

or - Binary OR two values.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

xor - Binary XOR two values.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

neg - Negate a value.

`arg1` - Destination. Destination.

Response: This command does not set any result variables.

not - Binary NOT a value.

`arg1` - Destination. Destination.

Response: This command does not set any result variables.

bswap - Perform abswapoperation: The byte order of the destination is inverted, so the last byte becomes the first.

`arg1` - Destination. Destination.

Response: This command does not set any result variables.

rol - Binary ROL (rotate left) a value.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

ror - Binary ROR (rotate right) a value.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

shl - Binary SHL/SAL (signed/unsigned shift left) a value.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

shr - Binary SHR (unsigned shift right) a value.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

sar - Binary SAR (signed shift right) a value.

`arg1` - Destination. Destination.
`arg2` - Source. Source.

Response: This command does not set any result variables.

popcnt - Evaluate the population count of a value, that is, number of bits set to 1.

`arg1` - Value. Value.

Response: `arg1` is set to the population count. Additionaly, the internal variable `$_EZ_FLAG` is set to 1 if `arg1` is 0, and set to 0 otherwise. The internal variable `$_BS_FLAG` is set to 0.

lzcnt - Count the number of leading zeros of a value. If the value is 0, then the result is 64 on 64-bit platform and 32 on 32-bit platform.

`arg1` - Value. Value.

Response: `arg1` is set to the number of leading zeros. Additionaly, the internal variable `$_EZ_FLAG` is set to 1 if `arg1` is 0, and set to 0 otherwise. The internal variable `$_BS_FLAG` is set to 0.

push - Push a value on the stack.

`arg1` - The value to push on the stack. The value to push on the stack.

Response: This command does not set any result variables.

pop - Pop a value from the stack.

`[arg1]` - The destination. When not specified it will just increase CSP. The destination. When not specified it will just increase CSP.

Response: This command does not set any result variables.

test - Binary TEST a value.

`arg1` - Value to test. Value to test.
`arg2` - Tester. Tester.

Response: This command sets the internal variables $_EZ_FLAG and $_BS_FLAG. $_EZ_FLAG is set to 1 when arg1 & arg2 == 0. $_BS_FLAG is always set to 0.

cmp - This command compares two expressions. Notice that when you want to check for values being bigger or smaller, the comparison arg1>arg2 is made. If this evaluates to true, the $_BS_FLAG is set to 1, meaning the value is bigger. So you test if arg1 is bigger/smaller than arg2.

`arg1` - First expression to compare. First expression to compare.
`arg2` - Second expression to compare. Second expression to compare.

Response: This command sets the internal variables $_EZ_FLAG and $_BS_FLAG. They are checked when a branch is performed.

mov - Set a variable.

`arg1` - Variable name (optionally prefixed with a $) to set. When the variable does not exist, it will be created. Note that SSE registers are not supported (Instead use Variable name (optionally prefixed with a $) to set. When the variable does not exist, it will be created. Note that SSE registers are not supported (Instead use movdqu for SSE registers).
`arg2` - Value to store in the variable. If you use Value to store in the variable. If you use `#112233#` it will write the bytes `112233` in the process memory at `arg1`.

Response: This command does not set any result variables.

movdqu - Read/write an XMM register. The source and destination operands can be either an XMM register, or a memory location. The value of destination operand will be set to source operand. When using a memory location, only the syntax[addr]is supported, whereaddris an expression of the memory address. Unlike other commands, the size of operands are 16 bytes. MM/YMM/ZMM registers are not supported by this command, to access YMM/ZMM registers, usevmovdqucommand.

`arg1` - The destination operand. The destination operand.
`arg2` - The source operand. The source operand.

Response: This command does not set any result variables.

vmovdqu - Read/write a YMM/ZMM register. The source and destination operands can be either an YMM/ZMM register, or a memory location. The value of destination operand will be set to source operand. When using a memory location, only the syntax[addr]is supported, whereaddris an expression of the memory address. Unlike other commands, the size of operands are 32 bytes for YMM registers and 64 bytes for ZMM registers. To access ZMM registers, the computer and x64dbg version must support AVX-512. To access XMM registers, usemovdqucommand.

`arg1` - The destination operand. The destination operand.
`arg2` - The source operand. The source operand.

Response: This command does not set any result variables.

kmovd - Thekmovd/kmovqcommands are used to access AVX-512 opmask registersK0-K7. These commands are only available when the computer and x64dbg version supports AVX-512.

`arg1` - The destination operand. The destination operand.
`arg2` - The source operand. The source operand.

Response: This command does not set any result variables.

## Analysis

analyse - Do function analysis.

Takes no arguments.

Response: This command does not set any result variables.

exanalyse - Do exception directory analysis. This kind of analysis doesn’t work on 32-bit executables.

Takes no arguments.

Response: None

cfanalyze - Do control flow analysis in the module selected in the disassembly view.

Takes no arguments.

Response: None

analyse_nukem - Do function analysis using nukem’s algorithm.

Takes no arguments.

Response: This command does not set any result variables.

analxrefs - Do xrefs analysis in the module selected in the disassembly view.

Takes no arguments.

Response: None

analrecur - Do single function analysis.

`arg1` - The base address of the function to analyze. The base address of the function to analyze.

Response: None

analadv - Do function analysis, embedded data analysis and xref analysis.

Takes no arguments.

Response: None

virtualmod - Tell the debugger to treat a memory range as a virtual module.

`arg1` - the user-supplied module name. the user-supplied module name.
`arg2` - the base of the memory range. the base of the memory range.
`[arg3]` - the size of the memory range. the size of the memory range.

Response: This command does not set any result variables.

symdownload - Attempt to download a symbol from a Symbol Store.

`[arg1]` - Module name (with or without extension) to attempt to download symbols for. When not specified, an attempt will be done to download symbols for all loaded modules. Module name (with or without extension) to attempt to download symbols for. When not specified, an attempt will be done to download symbols for all loaded modules.
`[arg2]` - Symbol Store URL. When not specified, the default store will be used. Symbol Store URL. When not specified, the default store will be used.

Response: This command does not set any result variables.

symload - Attempt to load a symbol from disk.

`arg1` - Module name (with or without extension) to attempt to load symbols for. Module name (with or without extension) to attempt to load symbols for.
`arg2` - Path to the symbol file. Path to the symbol file.
`[arg3]` - Force load. Set to Force load. Set to `1` to skip symbol validation.

Response: This command does not set any result variables.

symunload - Unload a symbol.

`arg1` - Module name (with or without extension) to unload symbols from. Module name (with or without extension) to unload symbols from.

Response: This command does not set any result variables.

imageinfo - Output the image information for a module. The information describes the Characteristics and DLL Characteristics fields in the PE header structure.

`[arg1]` - The base of the module. If not specified the module at CIP will be used. The base of the module. If not specified the module at CIP will be used.

Response: None

GetRelocSize - Get the correct size of a relocation table. This is useful while unpacking and restoring the original relocation table.

`arg1` - The address of the relocation table to analyze. The address of the relocation table to analyze.

Response: None

exhandlers - Print all exception handlers, including SEH(StructuredExceptionHandler), VEH(VectoredExceptionHandler),
VCH(VectoredContinueHandler) and UnhandledExceptionFilter, into the log.

Takes no arguments.

Response: None

exinfo - Print theEXCEPTION_DEBUG_INFOstructure from the last exception.

Takes no arguments.

Response: None

traceexecute - Tell the debugger that an address has been traced.

`arg1` - The address. The address.

Response: This command does not set any result variables.

## User Database

dbsave - Save a program database from memory to disk.

`[arg1]` - Path to save the database to. If not specified your current program database is used. Path to save the database to. If not specified your current program database is used.

Response: This command does not set any result variables.

dbload - Load a program database from disk in memory.

`[arg1]` - Path to load the database from. If specified your current data will not be automatically cleared (import). If not specified all your data will be cleared and the current program database is reloaded from disk. Path to load the database from. If specified your current data will not be automatically cleared (import). If not specified all your data will be cleared and the current program database is reloaded from disk.

Response: This command does not set any result variables.

dbclear - Clear the program database from memory (not from disk).

Takes no arguments.

Response: This command does not set any result variables.

commentset - Set a comment.

`arg1` - Address to set the comment at (preferably inside a module). Address to set the comment at (preferably inside a module).
`arg2` - Comment text. Comment text.

Response: This command does not set any result variables.

commentdel - Delete a comment.

`arg1` - Address of the comment to delete. Address of the comment to delete.

Response: This command does not set any result variables.

commentlist - List user-defined comments in reference view.

Takes no arguments.

Response: `$result` will be set to the number of user-defined comments.

commentclear - Delete all comments in all modules.

Takes no arguments.

Response: This command does not set any result variables.

labelset - Set a label.

`arg1` - Address to set the label at (preferably inside a module). Address to set the label at (preferably inside a module).
`arg2` - Label text. You can use Label text. You can use String Formatting here.

Response: This command does not set any result variables.

labeldel - Delete a label.

`arg1` - Address of the label to delete. Address of the label to delete.

Response: This command does not set any result variables.

labellist - List user-defined labels in reference view.

Takes no arguments.

Response: `$result` will be set to the number of user-defined labels.

labelclear - Delete all labels in all modules.

Takes no arguments.

Response: This command does not set any result variables.

bookmarkset - Set a bookmark.

`arg1` - Address to set the bookmark at (preferably inside a module). Address to set the bookmark at (preferably inside a module).

Response: This command does not set any result variables.

bookmarkdel - Delete a bookmark.

`arg1` - Address of the bookmark to delete. Address of the bookmark to delete.

Response: This command does not set any result variables.

bookmarklist - List user-defined bookmarks in reference view.

Takes no arguments.

Response: `$result` will be set to the number of user-defined bookmarks.

bookmarkclear - Delete all bookmarks in all modules.

Takes no arguments.

Response: This command does not set any result variables.

functionadd - Add a function.

`arg1` - Function range start. Function range start.
`arg2` - Function range end. Function range end.

Response: This command does not set any result variables.

functiondel - Delete a function.

`arg1` - Address inside the function range to delete. Address inside the function range to delete.

Response: This command does not set any result variables.

functionlist - List user-defined functions in reference view.

Takes no arguments.

Response: `$result` will be set to the number of user-defined functions.

functionclear - Delete all functions in all modules.

Takes no arguments.

Response: This command does not set any result variables.

argumentadd - Add a argument.

`arg1` - argument range start. argument range start.
`arg2` - argument range end. argument range end.

Response: This command does not set any result variables.

argumentdel - Delete a argument.

`arg1` - Address inside the argument range to delete. Address inside the argument range to delete.

Response: This command does not set any result variables.

argumentlist - List user-defined arguments in reference view.

Takes no arguments.

Response: `$result` will be set to the number of user-defined arguments.

argumentclear - Delete all arguments in all modules.

Takes no arguments.

Response: This command does not set any result variables.

## Script Commands

call - A call works exactly the same as an uncondentional branch, but it places it’s address on the script stack.

`arg1` - The label to jump to. The label to jump to.

Response: This command does not set any result variables.

invalid - Invalid command to throw an error message. This command will halt the script execution.

Takes no arguments.

Response: This command does not set any result variables.

error - Show an error message and terminate the script.

`arg1` - The error message to show. The error message to show.

Response: This command does not set any result variables.

Jxx - There are various branches that can react on the flags set by thecmp(and maybe other) command(s):

`arg1` - The label to jump to. The label to jump to.

Response: This command does not set any result variables.

log - Put information in the log.

`[arg1]` - Format string (see Format string (see String Formatting). When not specified, a newline will be logged. When using a format string it is recommended to use quotes to avoid ambiguity with the `;` (command separator): `log"{mem;8@rax}"`.

Response: This command does not set any result variables.

msg - Display a message box.

`arg1` - Message box text. You can use Message box text. You can use String Formatting here.

Response: This command does not set any result variables.

msgyn - Display a message box, asking the user to answer yes or no.

`arg1` - Message box text. You can use Message box text. You can use String Formatting here.

Response: The `$result` variable will be set to 1 when the user answered yes. Otherwise it’s set to 0.

pause - Halt the script execution. The user can resume the script after this command.

Takes no arguments.

Response: This command does not set any result variables.

printstack[,logstack] - Print the stack trace in the log.

Takes no arguments.

Response: This command does not set any result variables.

ret - When called without an entry on the stack, this command will end the script and set the script IP to the first line. When ‘call’ was executed before, ret will return from that call.

Takes no arguments.

Response: This command does not set any result variables.

scriptload - Load a script file.

`arg1` - Script file to load. Script file to load.

Response: This command does not set any result variables.

scriptdll - Execute a script DLL.

`arg1` - The filename and path of the script DLL. If a full path is not provided x64dbg will look in the The filename and path of the script DLL. If a full path is not provided x64dbg will look in the `scripts` directory for the DLL.

Response: None

scriptcmd - Execute a command in the context of a running script.

`scriptcmd` - directly to the command processor. directly to the command processor.
`scriptcmdaddrax,0x1245` - will execute the command will execute the command `addrax,0x1234`.

Response: This command does not set any result variables.

## Miscellaneous

chd - Change current directory (SetCurrentDirectory).

`arg1` - Path of a directory to change to. Path of a directory to change to.

Response: This command does not set any result variables.

zzz - Halt execution for some time (equivalent of calling kernel32.Sleep).

`[arg1]` - Time (in milliseconds) to sleep. If not specified this is set to 100ms (0.1 second). Keep in mind that input is in hex per default so Time (in milliseconds) to sleep. If not specified this is set to 100ms (0.1 second). Keep in mind that input is in hex per default so `Sleep100` will actually sleep 256 milliseconds (use `Sleep.100` instead).

Response: This command does not set any result variables.

HideDebugger - Hide the debugger from (very) simple detection methods. The PEB will be modified so thatIsDebuggerPresent()will return false.

Takes no arguments.

Response: This command does not set any result variables.

loadlib - Load a DLL into debugged program memory.

`arg1` - The name/path of the module to load. The name/path of the module to load.

Response: The `$result` variable will be set to the address of the loaded library.

asm - Assemble an instruction.

`arg1` - Address to place the assembled instruction at. Address to place the assembled instruction at.
`arg2` - Instruction text. You can use Instruction text. You can use String Formatting here.
`[arg3]` - When specified the remainder of the previous instruction will be filled with NOPs. When specified the remainder of the previous instruction will be filled with NOPs.

Response: $result will be set to the assembled instruction size. 0 on failure.

gpa - Get the address of an export inside a DLL.

`arg1` - Export name. Export name.
`[arg2]` - DLL name. DLL name.

Response: The $result variable is set to the export address. When the export is not found, $result will be set to 0.

setjit - Set the Just-In-Time Debugger in Windows. In WIN64 systems there are two JIT entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash: Windows attach the x32 debugger stored in the x32-JIT entry.

`arg1` -

Response: This command does not set any result variables.

getjit - Get the Just-In-Time Debugger in Windows. In WIN64 systems there are two JIT entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash: Windows attach the x32 debugger stored in the x32-JIT entry.

`arg2` -

Response: This command does not set any result variables.

getjitauto - Get the Auto Just-In-Time Debugger FLAG in Windows. if this flag value its TRUE Windows runs the debugger without user confirmation when a process crash. In WIN64 systems there are two JIT AUTO FLAG entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash with AUTO FLAG = FALSE: Windows confirm before attach the x32 debugger stored in the x32-JIT entry.

`arg1` -

Response: This command does not set any result variables.

setjitauto - Set the Auto Just-In-Time Debugger FLAG in Windows. if this flag value its TRUE Windows runs the debugger without user confirmation when a process crash. In WIN64 systems there are two JIT AUTO FLAG entries: one for a x32 debugger and other for a x64 debugger. In a WIN64 system when a x32 process crash with AUTO FLAG = FALSE: Windows confirm before attach the x32 debugger stored in the x32-JIT entry.

`arg1` -

Response: This command does not set any result variables.

getcommandline - It gets the actual command line.

Takes no arguments.

Response: This command does not set any result variables.

setcommandline - It changes the command line data.

`arg1` - New command line. New command line.

Response: This command does not set any result variables.

mnemonichelp - Output the detailed help information about an assembly mnemonic to the log.

`arg1` - the mnemonic name the mnemonic name

Response: This command does not set any result variables.

mnemonicbrief - Output the brief help information about an assembly mnemonic to the log.

`arg1` - the mnemonic name the mnemonic name

Response: This command does not set any result variables.

config - Get or set the configuration of x64dbg. It can also be used to load and store configuration specific to the script in the configuration file of x64dbg.

`arg1` - Section name of the INI file. Section name of the INI file.
`arg2` - Key name of the INI file. Key name of the INI file.
`[arg3]` - Optional new value of the configuration. If this argument is set to a number, it will be stored in the configuration file and Optional new value of the configuration. If this argument is set to a number, it will be stored in the configuration file and `$result` is not updated. If this argument is not set, the current configuration will be read into `$result`.

Response: None

## GUI

disasm - Disassemble at a certain position.

`[arg1]` - The address to disassemble at. When not specified, there will be disassembled at CIP. The address to disassemble at. When not specified, there will be disassembled at CIP.

Response: This command does not set any result variables.

dump - Dump at a certain position.

`arg1` - The address to dump at. The address to dump at.

Response: This command does not set any result variables.

sdump - Dump the stack at a certain position.

`[arg1]` - The address to dump at (must be inside the thread stack range). If not specified, The address to dump at (must be inside the thread stack range). If not specified, `csp` will be used.

Response: This command does not set any result variables.

memmapdump - Follow an address in the memory map.

`arg1` - The address to follow. The address to follow.

Response: This command does not set any result variables.

graph - Graph the control flow of function in the graph view.

`[arg1]` - The address of the function. The default value is EIP or RIP. The address of the function. The default value is EIP or RIP. `[arg2]` Options. If it contains “force” the graph will be reanalyzed, if it contains “silent” no messages will be printed on the console.

Response: None

guiupdateenable - Enables GUI update afterguiupdatedisableis executed.

`[arg0]` - If not 0, tells the debugger to update its GUI immediately. If not 0, tells the debugger to update its GUI immediately.

Response: This command does not set any result variables.

guiupdatedisable - Disable GUI update. This can speed up script execution.

Takes no arguments.

Response: This command does not set any result variables.

setfreezestack - Set if the stack should be frozen.

`arg1` - ‘0’ for unfrozen, ‘1’ for frozen. ‘0’ for unfrozen, ‘1’ for frozen.

Response: This command does not set any result variables.

refinit - Initialize reference view for command usage.

`[arg1]` - The title of the new reference view. You can use The title of the new reference view. You can use String Formatting here.

Response: This command does not set any result variables.

refadd - Add an entry to the reference view. You need to call ‘refinit’ before using refadd.

`arg1` - Address to put in the reference view. Address to put in the reference view.
`arg2` - Text to put after the address. You can use Text to put after the address. You can use String Formatting here.

Response: This command does not set any result variables.

refget - Retrieve the address of a reference.

`arg1` - Zero-based index of the reference address to retrieve. Zero-based index of the reference address to retrieve.

Response: The `$result` variable will be set to the address of the requested reference (zero on failure).

EnableLog - Enable the log output.

Takes no arguments.

Response: None

DisableLog - Disable the log output. New log messages will not be appended to the log view, but they will still be saved in the log file if log redirection is enabled in the log view.

Takes no arguments.

Response: None

ClearLog - Clear the log window.

Takes no arguments.

Response: This command does not set any result variables.

AddFavouriteTool - Add a tool in the favourites menu.

`arg1` - The path of the tool. The path of the tool.
`[arg2]` - The optional description of the tool. When this is set, it is displayed in the menu instead of the full path. The optional description of the tool. When this is set, it is displayed in the menu instead of the full path.

Response: None

AddFavouriteCommand - Add a command in the favourites menu.

`arg1` - The command to add. The command to add.
`[arg2]` - The optional shortcut key for the command. The optional shortcut key for the command.

Response: None

AddFavouriteToolShortcut - Set the shortcut key for an existing favourite tool.

`arg1` - The full path of an existing favourite tool. The full path of an existing favourite tool.
`arg2` - The shortcut key for it. The shortcut key for it.

Response: None

FoldDisassembly - Fold the disassembly within the specified range.

`arg1` - The start address of the range. The start address of the range.
`arg2` - The length of the range. The length of the range.

Response: None

## Types

DataUnknown - Mark data at address as Unknown.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataByte - Mark data at address as Byte.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataWord - Mark data at address as Word.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataDword - Mark data at address as Dword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataFword - Mark data at address as Fword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataQword - Mark data at address as Qword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataTbyte - Mark data at address as Tbyte.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataOword - Mark data at address as Oword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataMmword - Mark data at address as Mmword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataXmmword - Mark data at address as Xmmword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataYmmword - Mark data at address as Ymmword.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataFloat - Mark data at address as Float.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataDouble - Mark data at address as Double.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataLongdouble - Mark data at address as Long double.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataAscii - Mark data at address as Ascii.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataUnicode - Mark data at address as Unicode.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataCode - Mark data at address as Code.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataJunk - Mark data at address as Junk.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

DataMiddle - Mark data at address as Middle.

`arg1` - The address you want to mark. The address you want to mark.
`[arg2]` - Size (in bytes) to mark, when not set this defaults to 1. Size (in bytes) to mark, when not set this defaults to 1.

Response: This command does not set any result variables.

AddType - Add a type alias.

`arg1` - An existing type. An existing type.
`arg2` - The new type alias. The new type alias.

Response: This command does not set any result variables.

AddStruct - Add a new struct.

`arg1` - The type name of the struct. The type name of the struct.

Response: This command does not set any result variables.

AddUnion - Add a new union.

`arg1` - The type name of the union. The type name of the union.

Response: This command does not set any result variables.

AddMember - Add a new member to the end of a struct/union.

`arg1` - The type name of the struct/union (parent). The type name of the struct/union (parent).
`arg2` - The type of the new member. The type of the new member.
`arg3` - The name of the new member. The name of the new member.
`[arg4]` - The array size. A value greater than zero will make this member an array. The array size. A value greater than zero will make this member an array.
`[arg5]` - Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is not allowed.

Response: This command does not set any result variables.

AppendMember - Add a new member to the end of the last manipulated struct/union.

`arg1` - The type of the new member. The type of the new member.
`arg2` - The name of the new member. The name of the new member.
`[arg3]` - The array size. A value greater than zero will make this member an array. The array size. A value greater than zero will make this member an array.
`[arg4]` - Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is Offset from the start of the structure, only use this for implicitly padded structures. Overlapping with other members is not allowed.

Response: This command does not set any result variables.

AddFunction - Add a new function.

`arg1` - The type name of the function. The type name of the function.
`arg2` - The return type. The return type.
`[arg3]` - Calling convention, choose between Calling convention, choose between `cdecl`, `stdcall`, `thiscall` and `delphi`.
`[arg4]` - Set to nonzero to mark this function as Set to nonzero to mark this function as `noreturn`.

Response: This command does not set any result variables.

AddArg - Add a new argument to the end of a function.

`arg1` - The type name of the function (parent). The type name of the function (parent).
`arg2` - The type of the new argument. The type of the new argument.
`arg3` - The name of the new argument. The name of the new argument.

Response: This command does not set any result variables.

AppendArg - Add a new argument to the end of the last manipulated function.

`arg1` - The type of the new argument. The type of the new argument.
`arg2` - The name of the new argument. The name of the new argument.

Response: This command does not set any result variables.

SizeofType - Get the size of a type.

`arg1` - Name of the type. Name of the type.

Response: This command will set `$result` to the size of the type.

VisitType - Visit a type and print its members.

`arg1` - The type to visit. The type to visit.
`[arg2]` - Address to print from. If not specified (or zero) the type will be printed without values. Address to print from. If not specified (or zero) the type will be printed without values.
`[arg3]` - Maximum pointer resolution depth (default is 0). This can be used to also display structures (and values) pointed to by members of the type you are visiting. Maximum pointer resolution depth (default is 0). This can be used to also display structures (and values) pointed to by members of the type you are visiting.

Response: This command does not set any result variables.

ClearTypes - Clear all types.

`[arg1]` - The owner to clear. Leave this empty unless you know what you’re doing. The owner to clear. Leave this empty unless you know what you’re doing.

Response: This command does not set any result variables.

RemoveType - Remove a type.

`arg1` - The type to remove. The type to remove.

Response: This command does not set any result variables.

EnumTypes - Enumerate all types.

Takes no arguments.

Response: This command does not set any result variables.

LoadTypes - Load types from a JSON file.

`arg1` - The path to the JSON file. The owner of the loaded types will be the filename of the JSON file. Any types previously defined with this owner will be removed. The path to the JSON file. The owner of the loaded types will be the filename of the JSON file. Any types previously defined with this owner will be removed.

Response: This command does not set any result variables.

ParseTypes - Parse and load types from a header file.

`arg1` - The path to the header file. The owner of the loaded types will be the filename of the header file. Any types previously defined with this owner will be removed. The path to the header file. The owner of the loaded types will be the filename of the header file. Any types previously defined with this owner will be removed.

Response: This command does not set any result variables.

## Conditional Breakpoint Control

SetBreakpointName - Sets the name of a software breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

`arg1` - The address of an existing software breakpoint. The address of an existing software breakpoint.
`[arg2]` - The name of the breakpoint (empty when not specified). The name of the breakpoint (empty when not specified).

Response: This command does not set any result variables.

SetBreakpointCondition - Sets the software breakpoint condition. When this condition is set, it is evaluated every time the breakpoint hits and the debugger would stop only if condition is not 0.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The condition expression. The condition expression.

Response: This command does not set any result variables.

SetBreakpointLog - Sets log text when a software breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The log format string (see introduction/formatting). The log format string (see introduction/formatting).

Response: This command does not set any result variables.

SetBreakpointLogCondition - Sets the logging condition of a software breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The logging condition (default condition when not specified). The logging condition (default condition when not specified).

Response: This command does not set any result variables.

SetBreakpointCommand - Sets the command to execute when a software breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The command (empty when not specified). The command (empty when not specified).

Response: This command does not set any result variables.

SetBreakpointCommandCondition - Sets the command condition of a software breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The command condition (default condition when not specified). The command condition (default condition when not specified).

Response: This command does not set any result variables.

SetBreakpointFastResume - Sets the fast resume flag of a software breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetBreakpointSingleshoot - Sets the singleshoot flag of a software breakpoint. If this flag is set the breakpoint will be removed on the first hit.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetBreakpointSilent - Sets the silent flag of a software breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

Response: This command does not set any result variables.

GetBreakpointHitCount - Gets the hit counter of a software breakpoint.

`arg1` - The address of the breakpoint. The address of the breakpoint.

Response: `$result` will be set to the current value of the hit counter.

ResetBreakpointHitCount - Resets the hit counter of a software breakpoint.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The new hit count (zero when not specified). The new hit count (zero when not specified).

Response: This command does not set any result variables.

SetHardwareBreakpointName - Sets the name of a hardware breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

`arg1` - The address of an existing hardware breakpoint. The address of an existing hardware breakpoint.
`[arg2]` - The name of the breakpoint (empty when not specified). The name of the breakpoint (empty when not specified).

Response: This command does not set any result variables.

SetHardwareBreakpointCondition - Sets the hardware breakpoint condition. When this condition is set, it is evaluated every time the breakpoint hits and the debugger would stop only if condition is not 0.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The condition expression. The condition expression.

Response: This command does not set any result variables.

SetHardwareBreakpointLog - Sets log text when a hardware breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The log format string (see introduction/formatting). The log format string (see introduction/formatting).

Response: This command does not set any result variables.

SetHardwareBreakpointLogCondition - Sets the logging condition of a hardware breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The logging condition (default condition when not specified). The logging condition (default condition when not specified).

Response: This command does not set any result variables.

SetHardwareBreakpointCommand - Sets the command to execute when a hardware breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The command (empty when not specified). The command (empty when not specified).

Response: This command does not set any result variables.

SetHardwareBreakpointCommandCondition - Sets the command condition of a hardware breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The command condition (default condition when not specified). The command condition (default condition when not specified).

Response: This command does not set any result variables.

SetHardwareBreakpointFastResume - Sets the fast resume flag of a hardware breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetHardwareBreakpointSingleshoot - Sets the singleshoot flag of a hardware breakpoint. If this flag is set the breakpoint will be removed on the first hit.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetHardwareBreakpointSilent - Sets the silent flag of a hardware breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

Response: This command does not set any result variables.

GetHardwareBreakpointHitCount - Gets the hit counter of a hardware breakpoint.

`arg1` - The address of the breakpoint. The address of the breakpoint.

Response: `$result` will be set to the current value of the hit counter.

ResetHardwareBreakpointHitCount - Resets the hit counter of a hardware breakpoint.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The new hit count (zero when not specified). The new hit count (zero when not specified).

Response: This command does not set any result variables.

SetMemoryBreakpointName - Sets the name of a memory breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

`arg1` - The address of an existing memory breakpoint. The address of an existing memory breakpoint.
`[arg2]` - The name of the breakpoint (empty when not specified). The name of the breakpoint (empty when not specified).

Response: This command does not set any result variables.

SetMemoryBreakpointCondition - Sets the memory breakpoint condition. When this condition is set, it is evaluated every time the breakpoint hits and the debugger would stop only if condition is not 0.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The condition expression. The condition expression.

Response: This command does not set any result variables.

SetMemoryBreakpointLog - Sets log text when a memory breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The log format string (see introduction/formatting). The log format string (see introduction/formatting).

Response: This command does not set any result variables.

SetMemoryBreakpointLogCondition - Sets the logging condition of a memory breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The logging condition (default condition when not specified). The logging condition (default condition when not specified).

Response: This command does not set any result variables.

SetMemoryBreakpointCommand - Sets the command to execute when a memory breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The command (empty when not specified). The command (empty when not specified).

Response: This command does not set any result variables.

SetMemoryBreakpointCommandCondition - Sets the command condition of a memory breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The command condition (default condition when not specified). The command condition (default condition when not specified).

Response: This command does not set any result variables.

SetMemoryBreakpointFastResume - Sets the fast resume flag of a memory breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetMemoryBreakpointSingleshoot - Sets the singleshoot flag of a memory breakpoint. If this flag is set the breakpoint will be removed on the first hit.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetMemoryBreakpointSilent - Sets the silent flag of a memory breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

Response: This command does not set any result variables.

GetMemoryBreakpointHitCount - Gets the hit counter of a memory breakpoint.

`arg1` - The address of the breakpoint. The address of the breakpoint.

Response: `$result` will be set to the current value of the hit counter.

ResetMemoryBreakpointHitCount - Resets the hit counter of a memory breakpoint.

`arg1` - The address of the breakpoint. The address of the breakpoint.
`[arg2]` - The new hit count (zero when not specified). The new hit count (zero when not specified).

Response: This command does not set any result variables.

SetLibrarianBreakpointName - Sets the name of a librarian breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The name of the breakpoint (empty when not specified). The name of the breakpoint (empty when not specified).

Response: This command does not set any result variables.

SetLibrarianBreakpointCondition - Sets the librarian breakpoint condition. When this condition is set, it is evaluated every time the breakpoint occurs and the debugger would stop only if condition is not 0.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The condition expression. The condition expression.

Response: This command does not set any result variables.

SetLibrarianBreakpointLog - Sets log text when a librarian breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The log format string (see introduction/formatting). The log format string (see introduction/formatting).

Response: This command does not set any result variables.

SetLibrarianBreakpointLogCondition - Sets the logging condition of a librarian breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The logging condition (default condition when not specified). The logging condition (default condition when not specified).

Response: This command does not set any result variables.

SetLibrarianBreakpointCommand - Sets the command to execute when a librarian breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The command (empty when not specified). The command (empty when not specified).

Response: This command does not set any result variables.

SetLibrarianBreakpointCommandCondition - Sets the command condition of a librarian breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The command condition (default condition when not specified). The command condition (default condition when not specified).

Response: This command does not set any result variables.

SetLibrarianBreakpointFastResume - Sets the fast resume flag of a librarian breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetLibrarianBreakpointSingleshoot - Sets the singleshoot flag of a librarian breakpoint. If this flag is set the librarian breakpoint will be removed on the first hit.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetLibrarianBreakpointSilent - Sets the silent flag of a librarian breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

Response: This command does not set any result variables.

GetLibrarianBreakpointHitCount - Gets the hit counter of a librarian breakpoint.

`arg1` - The DLL name. The DLL name.

Response: `$result` will be set to the current value of the hit counter.

ResetLibrarianBreakpointHitCount - Resets the hit counter of a librarian breakpoint.

`arg1` - The DLL name. The DLL name.
`[arg2]` - The new hit count (zero when not specified). The new hit count (zero when not specified).

Response: This command does not set any result variables.

SetExceptionBreakpointName - Sets the name of an exception breakpoint. It will be displayed in the breakpoints view and in the log when the breakpoint is hit.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The name of the breakpoint (empty when not specified). The name of the breakpoint (empty when not specified).

Response: This command does not set any result variables.

SetExceptionBreakpointCondition - Sets the exception breakpoint condition. When this condition is set, it is evaluated every time the exception occurs (chance must match) and the debugger would stop only if condition is not 0.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The condition expression. The condition expression.

Response: This command does not set any result variables.

SetExceptionBreakpointLog - Sets log text when an exception breakpoint is hit. When log condition is not specified, it will always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The log format string (see introduction/formatting). The log format string (see introduction/formatting).

Response: This command does not set any result variables.

SetExceptionBreakpointLogCondition - Sets the logging condition of an exception breakpoint. When log condition is not specified, log text always be logged regardless of the break condition, otherwise it will be logged when the logging condition is satisfied.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The logging condition (default condition when not specified). The logging condition (default condition when not specified).

Response: This command does not set any result variables.

SetExceptionBreakpointCommand - Sets the command to execute when an exception breakpoint is hit. If the command condition is not specified, it will be executed when the debugger breaks, otherwise it will be executed when the condition is satisfied.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The command (empty when not specified). The command (empty when not specified).

Response: This command does not set any result variables.

SetExceptionBreakpointCommandCondition - Sets the command condition of an exception breakpoint. When command condition is not specified, the command will be executed when the debugger would break, otherwise it will be executed when the condition is satisfied.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The command condition (default condition when not specified). The command condition (default condition when not specified).

Response: This command does not set any result variables.

SetExceptionBreakpointFastResume - Sets the fast resume flag of an exception breakpoint. If this flag is set and the break condition doesn’t evaluate to break, no GUI, plugin, logging or any other action will be performed, except for incrementing the hit counter.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled The fast resume flag. If it is 0 (default), fast resume is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetExceptionBreakpointSingleshoot - Sets the singleshoot flag of an exception breakpoint. If this flag is set the exception breakpoint will be removed on the first hit.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled The singleshoot flag. If it is 0 (default), singleshoot is disabled, otherwise it is enabled

Response: This command does not set any result variables.

SetExceptionBreakpointSilent - Sets the silent flag of an exception breakpoint. If this flag is set, the default log message will not appear. User-defined log is not affected.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.
`[arg2]` - The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled The silent flag. If it is 0 (default), silent is disabled, otherwise it is enabled

Response: This command does not set any result variables.

GetExceptionBreakpointHitCount - Gets the hit counter of an exception breakpoint.

`arg1` - The name, exception name or code of the exception breakpoint. The name, exception name or code of the exception breakpoint.

Response: `$result` will be set to the current value of the hit counter.

ResetExceptionBreakpointHitCount - Resets the hit counter of an exception breakpoint.

`arg1` - The name, exception code or name of the exception breakpoint. The name, exception code or name of the exception breakpoint.
`[arg2]` - The new hit count (zero when not specified). The new hit count (zero when not specified).

Response: This command does not set any result variables.

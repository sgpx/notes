## Quick Comparison

| Feature | `nohup` | `disown` |
|---------|---------|---------|
| **Purpose** | Runs a command immune to hangups (terminal disconnect) | Removes a job from the shell's job list |
| **Protects from** | SIGHUP signal when terminal closes | Shell termination (but NOT terminal disconnect) |
| **Output** | Redirects to `nohup.out` by default | Goes to terminal (gets lost if terminal closes) |
| **Use case** | Starting long-running processes you want to survive terminal closure | Managing already-running background jobs |
| **Syntax** | `nohup command &` | `disown %jobid` or `disown -a` |

---

## The Simple Breakdown

**`nohup`** stands for "no hangup." It's a **protective wrapper** you put around a command before you run it. When you close your terminal, the command doesn't die—it keeps running. This works because `nohup` ignores the SIGHUP signal (the "hangup" signal sent when a terminal closes).

**`disown`** is a **shell built-in** that removes a running background job from your shell's job table. Once disowned, the shell won't track it anymore and won't send signals to it if the shell exits. However, it won't protect the job if *your terminal* closes—only if the shell itself exits.

---

## When to Use Each

- Use **`nohup`** when you're starting a new process and want it to survive your terminal closing (e.g., `nohup ./myscript.sh &`)
- Use **`disown`** when you've already started a background job and want to detach it from the shell (e.g., start a job, then type `disown %1`)

The key difference: `nohup` is **preventative** (before you run the command), while `disown` is **reactive** (after the job is running).

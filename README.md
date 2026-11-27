# System Process Logger with Scheduling

A set of Python command-line scripts for listing running processes and logging their process ID, name, and username. The main `ProcInfoLog.py` script can also email the generated log file.

## Requirements

- Python 3
- `psutil`
- A Gmail account with an App Password if you want to send email

The other imported modules are part of Python's standard library.

## Setup on Windows

Open Command Prompt in the project directory and optionally create a virtual environment:

```cmd
py -m venv .venv
.venv\Scripts\activate
python -m pip install psutil
```

## Usage

Run commands from the project directory:

```cmd
python ProcInfo_1.py
```

Lists running processes and writes the results to a log file.

```cmd
python ProcInfo_2.py notepad.exe
```

Searches for the specified process name and logs matching process details.

```cmd
python ProcInfo_3.py ProcessLogs
```

Creates the specified directory if needed and writes running process information to `ProcessLog.log` inside it.

```cmd
python ProcInfoLog.py ProcessLogs recipient@example.com
```

Creates `ProcessLogs\ProcessLog.log` with running process information and emails it to the recipient. The recipient address is required for this script.

The scripts also accept `--h` for usage help and `--u` for a short usage message.

## Email configuration

`MailModule.py` reads the sender credentials from the `SMTP_EMAIL` and `SMTP_PASSWORD` environment variables. It connects to Gmail over SSL on port 465. Use a Gmail App Password for `SMTP_PASSWORD`, not your regular Google account password.

In Command Prompt, set the variables before running the email script:

```cmd
set "SMTP_EMAIL=sender@gmail.com"
set "SMTP_PASSWORD=your-gmail-app-password"
python ProcInfoLog.py ProcessLogs recipient@example.com
```

These values remain available only in that Command Prompt window. Set them again in a new window. Do not put credentials in the source code or commit them to the repository. If an App Password is exposed, revoke it and create a replacement.

## Scheduling

The repository does not include a scheduler script or scheduling configuration. To run a script periodically on Windows, configure it in Task Scheduler. Set the task action to run your Python interpreter with the script path and arguments shown above, and set **Start in** to the project directory. For scheduled email runs, ensure the task account has the `SMTP_EMAIL` and `SMTP_PASSWORD` environment variables configured; variables set with the CMD `set` command are not automatically available to a separately launched task.

## Project files

- `ProcInfo_1.py`: lists all running processes.
- `ProcInfo_2.py`: searches for a named process.
- `ProcInfo_3.py`: writes process information to a log in a chosen directory.
- `ProcInfoLog.py`: logs running processes and emails the log.
- `ProcessModule.py`: process enumeration and lookup helpers using `psutil`.
- `Logger.py`: creates log directories and configures logging.
- `MailModule.py`: builds and sends the email with the log attachment.

# Passing the first stage

The entry point for your `shell` implementation is in `src/main.rs`.

# Stage 2

Note: This section is for stages 2 and beyond.

1. Ensure you have `cargo (1.70)` installed locally
1. Run `./your_shell.sh` to run your program, which is implemented in
   `src/main.rs`. This command compiles your Rust project, so it might be slow
   the first time you run it. Subsequent runs will be fast.

I used WSL and I chose to use “Ubuntu”:
```sh
bash
wsl --install -d Ubuntu
```
To choose the distro:
```sh
wsl --list --online
```

# Stage 3
To start the shell, run:
```sh
bash
exec cargo run --quiet --release --target-dir=/tmp/codecrafters-shell-target
```

# What is possible to do
Running the help command provides a detailed description of the various commands available:

## ./your_program_name.sh {command} file_name.daw

You can replace `your_program_name.sh` with the actual name of your program, which functions as both a compiler and an interpreter. After deciding on the file name, you can chain together two commands:

- **tokenize**: This command returns the tokens generated during the scanning phase, effectively breaking down the input characters into manageable pieces.
- **evaluate**: This command returns the result of evaluating expressions and processing the tokens after the `tokenize` command. (Note: Running `evaluate` automatically triggers `tokenize` first.)

Additionally, the supported languages have the following file extensions: `.daw` and `.lox` (reference to the volume).

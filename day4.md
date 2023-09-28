# Basic Python Course - Session 4

## Review Exercises

- [ ] Create a program that creates copies of itself:
      It takes from sys.argv a list of names of copies, and copies itself to each name
      - print out to the screen all the words you read from sys.argv
      - put each word from sys.argv in a for loop - do something with each word
      - copy yourself (who are you by the way?) to the Path(argument)


- [ ] Find all the *.py files in a directory that do `import pathlib`

- [ ] Find all the files in a given directory whose size is larger than 1MB

- [ ] Two words are an anagram if they have the same letters (possibly in different order). Write a python function that takes a list of words and return a list of sets of anagrams. For example:

```
anagrams(['add', 'dad', 'help', 'more', 'rome']) == 
[{'add', 'dad'}, {'help'}, {'more', 'rome'}]
```

- [ ] https://projecteuler.net/problem=4

- [ ] https://adventofcode.com/2022/day/1

- [ ] https://adventofcode.com/2021/day/4
    - Create a class `BingoCaller`. We'll create it from the first line in the file: `caller = BingoCaller(f)`
    - Figure out how to create a board from a file: `boards.append(BingoBoard(f))`.
      This should read lines from the file and add them to the board, until it encounters an empty line.
      If there's no data at all, you can raise an Exception
    - Create a loop that reads Bingo Boards from the file until no more are left, and at the end print all the boards
    - In `BingoBoard` implement the methods: `play(number: int)`, `is_winner()`.
    - In `BingoCaller` implement the method: `next_number` that returns the next number if exists, otherwise raise a StopIteration exception
    - Write a loop that calls `caller.next_number()`, and pass each number to all the boards' `play` method. Then check if you have a winner
    - Modify your board's `play` method to do nothing if the board already won
    - Use the classes you created to solve the exercise


## A Glimpse of Qt
- [ ] Create a GUI app in Python
- [ ] Use the designer
- [ ] Connect UI events to python code



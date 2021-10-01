# guessing_game
Built-in unit test module demo used to test a simple guessing game

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Examples of Use](#examples-of-use)
* [Status](#status)
* [Sources](#sources)

## General Info
This project is a demonstration of Unit Test. Class TestGame is created as a child of unittest.TestCase. TestGame.assertEqual is used to test response to various user inputs:

- incorrect guess
- correct guess
- out of range minus
- zero
- non-decimal
- empty string
- out of range +ve
- wrong type (list)

## Technologies
This project is created with

Python 3.8

unittest

## Setup
To run this project install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## Features
* A simple guessing game (main.py)
* A test module (test.py) which tries 9 different user input edge cases and confirms correct result.

### To do:
* Reuse this code to more extensively test a website

## Examples of Use

Usage: 

Run the guessing game from command line. Try to guess the random number between 1-10.

Code example:

Command line
`$ python3 main.py`

To run the test module:

Command line
`$ python3 test.py`

The test module imports main and runs 9 tests to confirm correct operation.

## Status
Complete.

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery

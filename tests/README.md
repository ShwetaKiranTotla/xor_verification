# Testplan

## Design Specification

* DUT: 2 Input OR Gate
* Interface: RDY/EN protocol  
Producers/ Consumers assert RDY when they have data to offer/ consume and keep it asserted until EN is asserted.  
EN is asserted when both Producer and Consumer RDY are asserted.  
Producers/ Consumers can take 0-20 cycles to produce/ consume data.

## Logistics

* Machine: Laptop
* Repository: Github (https://github.com/Dyumnin-Interns/interfaces-ShwetaKiranTotla)
* Regression: Github actions
* Issue Tracking: Github issues
* Software: Python 3.10 (or any Python>3.6), iverilog, cocotb, cocotb-bus, cocotb-coverage, xcelium/vcs/questasim (for code coverage)
* Licenses: Simulator License for code coverage
* BFM: None

## Environment

* Unit Level: OR Gate which has two inputs A and B and an output Y.  
* There are generators for A and B which generate the data and drivers for A,B and Y.
* A monitor is added to send data to the scoreboard (can also be sent throught the Y driver). 
* Data from the generator is sent to the scoreboard.

## Test cases

### Test case 1:
* Feature: OR gate Datapath test.
* Description: Give inputs to the A and B pins of the DUT and check whether the expected value matches the ouput at pin Y of the DUT.
* Scenario: Directed truth table test
* Given: Unit test Environment
* When input is (0, 0), (0,1), (1, 0), (1, 1)
* Then output is (0, 1, 1, 1)
* Coverage: A = [0, 1], B = [0, 1], Y = [0, 1]  
Cross between A & B.
### Test case 2:
* Feature: OR gate Datapath Randomized test.
* Description: Give random inputs to the A and B pins of the DUT and check whether the expected value matches the ouput at pin Y of the DUT.
* Scenario: Random Test
* Given: Unit test Environment 
* When input A and B are 10 samples of random.randint(0,1).
* Then output is A|B.
* Coverage: A = [0, 1], B = [0, 1], Y = [0, 1]  
Cross between A & B.

## Goals: Code Coverage and Functional Coverage

* 100% Code, Branch and Toggle Coverage
* 100% Functional Coverage

## Datapath

+ Bins:
	* A = [0, 1]
	* B = [0, 1]
	* Y = [0, 1]
+ Cross:
	+ A * B

## Protocol

### States:

| Data       | EN      | RDY     | Description |
| :-----:    | :-----: | :-----: | :-----:     |
| Don't care | 0       | 0       | Idle	       |
| Valid data | 0       | 1       | Ready	     |
| Valid data | 0       | 1       | Transaction |

The case where EN is 1 and RDY is 0 cannot occur.  
Need to verify all state transactions.

### State transition verification

| Previous State | Current State |
| :-----:        | :------:      |
| Idle  	       | Idle          |
| Idle  	       | Ready	       |
| Idle  	       | Transaction   |

+ Bins:
	* Current State = [Idle, Ready, Transaction]
	* Previous State = [Idle, Ready, Transaction]

+ Cross
	* Current State * Previous State

## Delay

+ Bins
	* Delay = [Min, Max, Low, High] # 0, 20, 1-10, 11-19

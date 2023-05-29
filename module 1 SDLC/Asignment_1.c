/*

1    What is software? What is software engineering? 
--->  Software is a collection of instructions or data. In a general sense, they are required to run an application in a device like a mobile, computer, tablet.

2    Explain types of software
--->  1.Application software
      2.System software
      3.Driver software
      4.Pograming software

3    What is SDLC? Explain each phase of SDLC
--->  An SDLC- Software Development Life Cycle.
      SDLC phase --
      1. Incepation phase-  Requirement of the project,Goals,and Scope.
      2. Elaboration phase- the design of functional product architecture.
      3. Construction phase- Coding of the architecture.
      4. Transition phase- Releasing the product to a production environment.          

4    What is DFD? Create a DFD diagram on Flipkart 
--->  An DFD- Deta Flow Diagram
      1.Select a data flow diagram template. 
      2.Name the data flow diagram.
      3.Add an external entity that starts the process.
      4.Add a Process to the DFD.
      5.Add a data store to the diagram.
      6.Continue to add items to the DFD.
      7.Add data flow to the DFD. 
      8.Name the data flow.
      9.Customize the DFD with colors and fonts.    
      10.Add a title and share your data flow diagram.

5    What is Flow chart? Create a flowchart to make addition of two numbers 
---> A flowchart is the connection between different types of phases of parts  of a system. 
------->flowchart to make addition of two number?
--->     [Start]  (Starting of the program!)
            |
            |
    ["Enter integer A"] (read input variable A)
         [Get A]
            |
            |
    ["Enter integer B"] (read input variable B)
         [Get B]
            |
            |
         [C=A+B] (Performed addition of the variables and store it in C variable)
            |
            |       
    [PUT"The Sum is."%c;] (Print variable C)
            |
            |
          [End] (end of program)

6    What is Use case Diagram? Create a use-case on bill payment on paytm.
---> Use case diagrams consists of actors, use cases and their relationships. The diagram is used to model the system/subsystem of an application. A single use case diagram captures a particular functionality of a system. Hence to model the entire system, a number of use case diagrams are used.  

    Create a use-case on bill payment on paytm.
--->                          System
                                |
                                |
M                        <Include>               S                                       
A  ----------[Buy stock]----------[Make payment] U  
N                                                P
G                                                P -----Supply  Stock
E  ----------[Generate sale report]              L
R                                                I
                                                 E -----Receive Payment
                                                 R
INVENTARY SYSTEM----------[Update inventary]                                 

CASHIER----------------------------------------[Select items]
                                                      |
                                                      |
                                  |--------------|----|
                                  |<Include>     | <Include>
                                  |              |-------|
                              [Payment]                [scan items]
                                  |
                                  |
              |-------------------|--------------------|
              |<Extend>           |<Extend>            |<Extend>
              |                   |                    |
          [By cash]             [By credit]        [By debit]




*/